import logging

from prefect import flow, task

logging.basicConfig(level=logging.INFO)

_logger = logging.getLogger(__name__)

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
    floors = []
    for floor in range(10, 0, -1):
        floors.append(stop_at_floor.submit(floor))

    for f in floors:
        res.append(f.result())

    res = total_floors(res)
    _logger.info(f"Total floors visited: {res}")

if __name__ == "__main__":
    elevator()
