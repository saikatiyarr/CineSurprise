from kubernetes import client, config

config.load_kube_config()
apps_api = client.AppsV1Api()
core_api = client.CoreV1Api()
deployment_metadata = client.V1ObjectMeta(name="movie-app")
deployment_spec = client.V1DeploymentSpec(
    replicas=1,
    selector=client.V1LabelSelector(match_labels={"app": "movie-app"}),
    template=client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "movie-app"}),
        spec=client.V1PodSpec(
            containers=[
                client.V1Container(
                    name="movie-app-container",
                    image="573829104752.dkr.ecr.us-east-1.amazonaws.com/movie-app-repo:latest",
                    ports=[client.V1ContainerPort(container_port=5000)]
                )
            ]
        )
    )
)
deployment = client.V1Deployment(metadata=deployment_metadata, spec=deployment_spec)
apps_api.create_namespaced_deployment(namespace="default", body=deployment)
service_metadata = client.V1ObjectMeta(name="movie-service")
service_spec = client.V1ServiceSpec(
    selector={"app": "movie-app"},
    ports=[client.V1ServicePort(port=5000)]
)
service = client.V1Service(metadata=service_metadata, spec=service_spec)
core_api.create_namespaced_service(namespace="default", body=service)
