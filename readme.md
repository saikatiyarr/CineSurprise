# Project Title: CineChoice

## Description:

CineChoice is an innovative movie recommendation system designed to help users discover new films based on their preferences. Using advanced algorithms, CineChoice analyzes user ratings, genres, and viewing history to suggest personalized movie recommendations. With its intuitive interface and seamless integration, CineChoice makes it easy for users to explore a diverse range of movies and find their next cinematic adventure.

This web application is built on Python 3, with the frontend developed using HTML and CSS for a sleek and user-friendly interface. To ensure scalability and portability, CineChoice is containerized using Docker.

After containerization, the Docker image is stored in an AWS Elastic Container Registry (ECR) using Python's boto3 library, providing secure storage and easy access to the application.

In the deployment phase, we leverage AWS Elastic Kubernetes Service (EKS) to create a Kubernetes cluster with nodes. The deployment process, orchestrated with Python scripts, ensures that the application is deployed and accessible from the internet via the Kubernetes cluster.

CineChoice offers a seamless movie discovery experience, combining cutting-edge technology with user-centric design to deliver personalized movie recommendations to users worldwide.
