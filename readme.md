# Project Title: CineSurprise

## Description:

CineSurprise is an innovative movie recommendation system designed to help users discover new films. Using TMDB's database, CineSurprise analyzes worldwise user ratings, genres, and suggests popular movie recommendations. With its intuitive interface and seamless integration, CineSurprise makes it easy for users to explore a diverse range of movies and find their next cinematic adventure.

This web application is built on Python3's Flask module, with the frontend developed using HTML and CSS for a sleek and user-friendly interface. To ensure scalability and portability, CineSurprise is **containerized using Docker**.

After containerization, the Docker image is stored in an **AWS Elastic Container Registry (ECR)** using Python's boto3 library, providing secure storage and easy access to the application.

In the deployment phase, I leveraged **AWS Elastic Kubernetes Service (EKS)** to create a Kubernetes cluster with nodes. The deployment process, orchestrated with Python scripts, ensures that the application is deployed and accessible from the internet via the Kubernetes cluster.

CineSurprise offers a seamless movie discovery experience, combining cutting-edge technology with user-centric design to deliver popular movie recommendations to users worldwide.
