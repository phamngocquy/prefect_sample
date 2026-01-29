import logging

from prefect import flow, task

logging.basicConfig(level=logging.INFO)

_logger = logging.getLogger(__name__)

@task()
def spawn_elevator_floors():
    return 20

@task
def stop_at_floor(floor: int) -> int:
    _logger.info(f"elevator moving to floor {floor}")
    _logger.info(f"elevator stops on floor {floor}")
    return floor

@task
def total_floors(order_floors: list[int]) -> list[int]:
    return order_floors


@flow
def elevator():
    res = []
    total_floors_count = spawn_elevator_floors()
    futs = stop_at_floor.map(range(total_floors_count, 0, -1))
    for f in futs:
        res.append(f.result())
    aa = total_floors(res)
    _logger.info(f"Total floors visited: {aa}")

if __name__ == "__main__":
    elevator()
