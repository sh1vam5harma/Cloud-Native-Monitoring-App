Deploying a Cloud Native Monitoring Application on Kubernetes through AWS 

Prereqs: 
Create IAM access key 
Install kubectl (cmd line tool for kubernetes)- lets you see if pods/nodes are up 

Step 1. Build the application:
app.py, index.html, requirements.txt
Runs on local host (flask app) 

Step 2. Containerize it using Docker
Make sure to download the Docker Desktop app 
Download Dockerhub and python image. 


Step 3: Create a Docker file, build the image, then run the container locally 
Docker keeps the application code + the dependencies 
Enter- docker run (to create the container) 


Step 4. Create an ECR (Elastic Container Registry) using Python 
Deploy the Docker container here/push the Docker image to ECR to host inside Kubernetes later
Create the ECR repo through Python code on VSCode 
Push the Docker image to ECR

5. (Deployment Phase) - create an Elastic Kubernetes Cluster with nodes and deploy the application on Kubernetes 
Deploy the containers from ECR in the form of Kubernetes clusters
Create a Kubernetes cluster on EKS
Create a node group within the cluster 
Create a Kubernetes deployment on VSCode - create EKS.py and manage Kubernetes using Python 
Port Forward Kubernetes Service and Access the Application deployed on Kubernetes Pod on the local host 

Use case:

This Cloud Native Monitoring App is designed to help developers monitor and manage containerized applications running on Kubernetes by integrating deployment automation with AWS services like ECR and EKS. It provides real-time visibility into app performance and simplifies infrastructure operations through a web interface.
