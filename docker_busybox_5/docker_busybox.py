import docker

client = docker.from_env()


container = client.containers.run(
    image="busybox",
    command=["sleep", "1000"],
    detach=True
)
exec_result = container.exec_run("hostname")


hostname = exec_result.output.decode().strip()
print("Container hostname:", hostname)

container.stop()
container.remove()
