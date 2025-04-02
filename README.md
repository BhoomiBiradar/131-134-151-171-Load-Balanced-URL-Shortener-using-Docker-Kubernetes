# **Load-Balanced URL Shortener using Docker & Kubernetes**  

## **Project Overview**  
This project is a **containerized URL shortener service** that allows users to submit long URLs and receive shortened versions. The system is built using **Python (Flask)** and runs inside a **Docker container**. The goal is to scale the application using **Kubernetes** with a **load balancer** and an in-memory key-value store (Redis or a dictionary).  

##  **Features**  
- Shortens long URLs and stores them in an in-memory key-value store  
- Redirects users from the short URL to the original long URL  
- Containerized using **Docker**  
- Will be deployed using **Kubernetes** (Week 2)  

## **Tech Stack**  
- **Backend**: Python (Flask)
- **Storage**: In-memory key-value store (Redis / Python Dictionary)  
- **Containerization**: Docker  
- **Orchestration**: Kubernetes  
