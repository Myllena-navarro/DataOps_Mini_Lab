import asyncio
from temporalio.client import Client
from app.workflows import OrdersPipelineWorkflow


async def main():
    client = await Client.connect("localhost:7233")

    result = await client.execute_workflow(
        OrdersPipelineWorkflow.run,
        id="orders-pipeline",
        task_queue="orders-task-queue",
    )

    print("RESULT:")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())