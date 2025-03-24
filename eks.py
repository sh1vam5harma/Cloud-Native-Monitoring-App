from kubernetes import client, config
from kubernetes.client.rest import ApiException

# Load kubeconfig
config.load_kube_config()
api_client = client.ApiClient()

# Define deployment
deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="my-flask-app"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(match_labels={"app": "my-flask-app"}),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels={"app": "my-flask-app"}),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="my-flask-container",
                        image="540494385036.dkr.ecr.us-east-1.amazonaws.com/my-cloud-native-repo:v1",
                        ports=[client.V1ContainerPort(container_port=5000)]
                    )
                ]
            )
        )
    )
)

# Define service
service = client.V1Service(
    metadata=client.V1ObjectMeta(name="my-flask-service"),
    spec=client.V1ServiceSpec(
        selector={"app": "my-flask-app"},
        ports=[client.V1ServicePort(port=5000, target_port=5000)],
        type="LoadBalancer"
    )
)

# Create deployment and service with error handling
try:
    print("Creating deployment...")
    client.AppsV1Api(api_client).create_namespaced_deployment(namespace="default", body=deployment)
    print("Deployment created.")
except ApiException as e:
    print(f"Failed to create deployment: {e}")

try:
    print("Creating service...")
    client.CoreV1Api(api_client).create_namespaced_service(namespace="default", body=service)
    print("Service created.")
except ApiException as e:
    print(f"Failed to create service: {e}")
