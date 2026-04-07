import asyncio
from temporalio.client import Client
from temporalio.worker import Worker

from app.activities import *
from app.workflows import OrdersPipelineWorkflow


async def main():
    client = await Client.connect("localhost:7233")

    worker = Worker(
        client,
        task_queue="orders-task-queue",
        workflows=[OrdersPipelineWorkflow],
        activities=[
            generate_csv_activity,
            load_csv_to_mongodb_activity,
            aggregate_orders_activity,
        ],
    )

    print("Worker started...")
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())