from prefect import flow, task
from prefect.logging import get_run_logger

# 1. Recommended: Use Prefect's built-in logger to ensure logs
# show up in both the console and the Prefect UI.
@task
def spawn_elevator_floors():
    return list(range(20, 0, -1))

@task
def stop_at_floor(floor: int) -> int:
    logger = get_run_logger()
    logger.info(f"elevator moving to floor {floor}")
    logger.info(f"elevator stops on floor {floor}")
    return floor

@task
def total_floors(order_floors: list[int]) -> list[int]:
    return order_floors

@flow
def elevator():
    logger = get_run_logger()

    # Get the list of floors
    total_floors_count = spawn_elevator_floors()

    # 2. .map() returns a list of PrefectFutures.
    futs = stop_at_floor.map(total_floors_count)

    # 3. Passing the list of futures into another task automatically
    # resolves them into their actual results (values) for that task.

    aa = total_floors(futs)

    # .result() converts the PrefectFutureList into a standard list[int]
    # results = futs.result()

    # aa = total_floors(results)

    logger.info(f"Total floors visited: {aa}")

if __name__ == "__main__":
    elevator()
