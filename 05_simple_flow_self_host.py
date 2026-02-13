from prefect import flow
from prefect.docker.docker_image import DockerImage


@flow(log_prints=True, name="hello-world-flow-slim")
def hello_world(name: str = "world", goodbye: bool = False):
    print(f"Hello {name} from Prefect! 🤗")

    if goodbye:
        print(f"Goodbye {name}!")


if __name__ == "__main__":
    # creates a deployment and starts a long-running
    # process that listens for scheduled work
    hello_world.deploy(name="my-first-deployment2",
        tags=["onboarding"],
        parameters={"goodbye": True},
        interval=60,
        work_pool_name="docker-work-pools",
        image=DockerImage(name="my_docker"),
        push=False
    )
