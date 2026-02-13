# uv run 01_run_flow_directly.py
# flow executed by local (executor) machine
# log, maetadata, etc. will show up in the console and prefect server UI
# a deloyemnt url will be provided to access the flow via a web server
import random

from prefect import flow, task


@task
def get_customer_ids() -> list[str]:
    """get_customer_ids.

    Args:

    Returns:
        list[str]:
    """
    # Fetch customer IDs from a database or API
    return [f"customer{n}" for n in random.choices(range(100), k=50)]


@task
def process_customer(customer_id: str) -> str:
    """process_customer.

    Args:
        customer_id (str): customer_id

    Returns:
        str:
    """
    # Process a single customer
    return f"Processed {customer_id}"


@flow(name="base_flow_03")
def myflow() -> list[str]:
    """main.

    Args:

    Returns:
        list[str]:
    """
    customer_ids = get_customer_ids()
    # Map the process_customer task across all customer IDs
    results = process_customer.map(customer_ids)
    return results  # type: ignore
