import time

from prefect import flow, task
from prefect.futures import wait

@task
def stop_at_floor(floor: int):
    print(f"elevator moving to floor {floor}")
    time.sleep(floor)
    print(f"elevator stops on floor {floor}")

@flow
def elevator():
    floors = []
    for floor in range(10, 0, -1):
        floors.append(stop_at_floor.submit(floor))
    wait(floors)
