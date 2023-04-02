# Flask Application with Docker & Kubernetes

This is a simple Flask application with a Dockerfile and Kubernetes manifests to help you deploy it locally in 3 different ways.
- Python & Flask on localhost.
- Docker container.
- Kubernetes in kind cluster.

## Requirements

- Python 3 installed (if you want to run the application locally)
- Docker installed
- [Kind installed](https://kind.sigs.k8s.io/)
- [Kind ingress configured](https://kind.sigs.k8s.io/docs/user/ingress/)

## Installation

1. Clone the repository to your local machine.
2. Open a terminal and navigate to the root directory of the project.
3. If you want to run the application locally, install the Flask dependencies by running the following command:

```
pip install -r requirements.txt
```

4. To run the application locally, execute the following command from the project root directory:

```
python app/main.py
```

5. To run the application using Docker, you need to first build the Docker image by running the following command from
   the
   project root directory:

```
docker build -t my-flask-app .
```

6. After building the Docker image, you need to tag it by running the following command:

```
docker tag my-flask-app:latest my-registry/my-flask-app:latest
```   

Note: Replace my-registry with your Docker registry name.

7. To run the application using Docker, execute the following command:

```
docker run -p 5001:5000 my-registry/my-flask-app
```

Note: Replace my-registry with your Docker registry name.

8. If you want to run the application in a Kubernetes cluster using Kind, first create a Kind cluster using the ingress
   configuration at https://kind.sigs.k8s.io/docs/user/ingress/


9. After creating the Kind cluster, you need to load the Docker image into the Kind cluster by running the following

```
kind load docker-image my-registry/my-flask-app:latest --name my-cluster
```

Note: Replace my-registry with your Docker registry name.

As an alternative, you can push the image to your personal docker registry.


10. To deploy the application to the Kind cluster, apply the deployment.yaml file by running the following command:

```
kubectl apply -f manifest.yaml
```

The manifest contain the deployment configuration, service and ingress. Verify you have all the resources by running:

```
kubectl get all
kubectl get ingress
```

You should be able to access the application at your `localhost`.