import docker
import yaml


with open("config.yaml", "r") as open_config:
    config = yaml.load(unicode(open_config.read()))

ports = [
    config["ports"]["web_port"]["container"],
    config["ports"]["cluster_port"]["container"],
    config["ports"]["server_port"]["container"]
]

bindings = {
    config["ports"]["web_port"]["container"]: config["ports"]["web_port"]["local"],
    config["ports"]["cluster_port"]["container"]: config["ports"]["cluster_port"]["local"],
    config["ports"]["server_port"]["container"]: config["ports"]["server_port"]["local"]
}

client = docker.Client(base_url="http://127.0.0.1:3945", version="1.7")

if config["build"]:
  client.build(".", tag=config["tag"])

container = client.create_container(config["tag"])
client.start(container)
