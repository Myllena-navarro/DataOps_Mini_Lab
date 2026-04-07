from __future__ import annotations

from pathlib import Path
from dotenv import load_dotenv
from pymongo import MongoClient
from temporalio import activity
import os
import pandas as pd

load_dotenv()


@activity.defn
async def generate_csv_activity() -> str:
    from app.generate_fake_csv import main
    main()
    return "data/raw/orders_fake_10mb.csv"


@activity.defn
async def load_csv_to_mongodb_activity(csv_path: str) -> str:
    mongodb_uri = os.getenv("MONGODB_URI")

    if not mongodb_uri:
        raise ValueError("MONGODB_URI not found")

    df = pd.read_csv(csv_path)
    records = df.to_dict(orient="records")

    client = MongoClient(mongodb_uri)
    db = client["dataops_lab"]
    collection = db["orders_raw"]

    collection.delete_many({})
    if records:
        collection.insert_many(records)

    count = collection.count_documents({})
    client.close()

    return f"Inserted {count} documents"


@activity.defn
async def aggregate_orders_activity() -> list[dict]:
    mongodb_uri = os.getenv("MONGODB_URI")

    client = MongoClient(mongodb_uri)
    collection = client["dataops_lab"]["orders_raw"]

    pipeline = [
        {"$group": {
            "_id": "$status",
            "total_orders": {"$sum": 1},
            "total_amount": {"$sum": "$amount"}
        }},
        {"$sort": {"total_amount": -1}}
    ]

    result = list(collection.aggregate(pipeline))
    client.close()

    return [
        {
            "status": r["_id"],
            "total_orders": r["total_orders"],
            "total_amount": round(float(r["total_amount"]), 2)
        }
        for r in result
    ]