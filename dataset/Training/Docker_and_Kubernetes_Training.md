# TechNova Solutions Pvt. Ltd.

# Docker and Kubernetes Training Manual

**Training Version:** 1.0
**Department:** Learning & Development (L&D), DevOps, and Engineering
**Duration:** 6 Weeks
**Target Audience:** DevOps Engineers, Software Engineers, Cloud Engineers, Site Reliability Engineers (SREs), Data Engineers, and Interns

---

# 1. Introduction to Containerization

Containerization is a method of packaging applications along with their dependencies into lightweight, portable containers.

Benefits of containerization include:

* Portability
* Scalability
* Consistency
* Faster deployment
* Resource efficiency
* Isolation

---

# 2. What is Docker?

Docker is an open-source containerization platform used to build, package, and deploy applications.

Docker components include:

* Docker Engine
* Docker Client
* Docker Daemon
* Docker Images
* Docker Containers
* Docker Registry

---

# 3. Installing Docker

Verify Docker installation:

```bash id="t8y2qa"
docker --version
```

Example output:

```text id="b3w6kc"
Docker version 27.2.0
```

Verify Docker service:

```bash id="z4mr1d"
docker info
```

---

# 4. Docker Architecture

Docker architecture consists of:

```text id="f7nc5r"
Docker Client
      ↓
Docker Daemon
      ↓
Docker Host
      ↓
Containers
```

Docker uses a client-server architecture.

---

# 5. Docker Images

Docker images are read-only templates used to create containers.

Search image:

```bash id="r5wj9h"
docker search python
```

Pull image:

```bash id="j8qx3m"
docker pull python:3.12
```

List images:

```bash id="u6vk4p"
docker images
```

---

# 6. Docker Containers

Create container:

```bash id="o3rd8w"
docker run python:3.12
```

Interactive container:

```bash id="n1yb6q"
docker run -it ubuntu bash
```

List containers:

```bash id="w9mc2a"
docker ps
```

List all containers:

```bash id="c7fh5t"
docker ps -a
```

---

# 7. Container Lifecycle

Container states:

* Created
* Running
* Paused
* Stopped
* Removed

Commands:

```bash id="k2je8u"
docker start
docker stop
docker restart
docker rm
```

---

# 8. Dockerfile

Dockerfile defines how to build container images.

Example:

```dockerfile id="q8nt1v"
FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

---

# 9. Building Docker Images

Build image:

```bash id="y5dw4k"
docker build -t employee-app .
```

List images:

```bash id="v2ra7x"
docker images
```

Remove image:

```bash id="m7hj3s"
docker rmi employee-app
```

---

# 10. Running Containers

Run application:

```bash id="x9pc4w"
docker run -p 8000:8000 employee-app
```

Detached mode:

```bash id="h6zf2r"
docker run -d employee-app
```

Container naming:

```bash id="a1vt5y"
docker run --name api-server employee-app
```

---

# 11. Docker Volumes

Volumes store persistent data.

Create volume:

```bash id="b4ne8j"
docker volume create db-volume
```

Attach volume:

```bash id="k8uy1f"
docker run -v db-volume:/data postgres
```

Benefits:

* Persistence
* Backup support
* Data sharing

---

# 12. Docker Networks

Create network:

```bash id="j5lx9m"
docker network create app-network
```

List networks:

```bash id="w3td7k"
docker network ls
```

Types:

* Bridge
* Host
* Overlay
* None

---

# 13. Docker Compose

Docker Compose manages multi-container applications.

Example:

```yaml id="r9kw6d"
version: "3"

services:
  api:
    build: .

  database:
    image: postgres
```

Run compose:

```bash id="u1ms5a"
docker compose up
```

Stop compose:

```bash id="p7vr4x"
docker compose down
```

---

# 14. Docker Registry

Popular registries:

* Docker Hub
* GitHub Container Registry
* AWS ECR
* Azure Container Registry

Login:

```bash id="e8hj3r"
docker login
```

Push image:

```bash id="g4dy7s"
docker push company/api:v1
```

---

# 15. Docker Best Practices

Developers should:

* Use small base images
* Minimize layers
* Avoid root user
* Use environment variables
* Implement health checks
* Scan vulnerabilities

---

# 16. Introduction to Kubernetes

Kubernetes is an open-source container orchestration platform.

Benefits:

* Scalability
* High availability
* Self-healing
* Load balancing
* Automated deployments

---

# 17. Kubernetes Architecture

Components:

## Control Plane

* API Server
* Scheduler
* Controller Manager
* etcd

## Worker Node

* Kubelet
* Container Runtime
* Kube Proxy

Architecture:

```text id="n4xp7c"
Control Plane
      ↓
Worker Nodes
      ↓
Pods
```

---

# 18. Kubernetes Cluster

Check cluster:

```bash id="f7by5u"
kubectl cluster-info
```

View nodes:

```bash id="v1pq4n"
kubectl get nodes
```

---

# 19. Pods

Pods are the smallest deployable unit in Kubernetes.

Create pod:

```yaml id="x8wj2k"
apiVersion: v1
kind: Pod

metadata:
  name: app-pod
```

List pods:

```bash id="h3cr9t"
kubectl get pods
```

---

# 20. Deployments

Deployment example:

```yaml id="o5kt7r"
apiVersion: apps/v1
kind: Deployment

spec:
  replicas: 3
```

Create deployment:

```bash id="z2my8f"
kubectl apply -f deployment.yaml
```

View deployments:

```bash id="u4rh6k"
kubectl get deployments
```

---

# 21. ReplicaSets

ReplicaSets ensure the desired number of pod replicas are running.

Benefits:

* High availability
* Automatic recovery
* Horizontal scaling

---

# 22. Services

Service types:

| Service      | Description |
| ------------ | ----------- |
| ClusterIP    | Internal    |
| NodePort     | External    |
| LoadBalancer | Cloud       |
| ExternalName | DNS mapping |

Example:

```bash id="q1sb5j"
kubectl get services
```

---

# 23. ConfigMaps

ConfigMaps store configuration.

Create ConfigMap:

```bash id="k9yn3m"
kubectl create configmap app-config
```

Benefits:

* Centralized configuration
* Dynamic updates

---

# 24. Secrets

Secrets store sensitive information.

Create secret:

```bash id="g6vf2p"
kubectl create secret generic db-secret
```

Examples:

* API keys
* Database passwords
* Tokens
* Certificates

---

# 25. Ingress

Ingress manages external traffic routing.

Benefits:

* HTTPS support
* Load balancing
* URL routing

Example:

```bash id="w8pk6r"
kubectl apply -f ingress.yaml
```

---

# 26. Horizontal Pod Autoscaler

Create autoscaler:

```bash id="d7sm4q"
kubectl autoscale deployment api
```

Benefits:

* Automatic scaling
* Cost optimization
* Better performance

---

# 27. Rolling Updates

Update deployment:

```bash id="y9vb3x"
kubectl set image deployment/api
```

Monitor rollout:

```bash id="s2mk7j"
kubectl rollout status deployment/api
```

---

# 28. Rollback Deployment

Rollback:

```bash id="c8ph4u"
kubectl rollout undo deployment/api
```

Benefits:

* Fast recovery
* Reduced downtime

---

# 29. Monitoring

Monitoring tools:

* Prometheus
* Grafana
* Datadog
* ELK Stack

Monitor:

* CPU
* Memory
* Network
* Storage
* Errors

---

# 30. Logging

Centralized logging tools:

* Elasticsearch
* Fluentd
* Kibana

Logs collected:

* Application logs
* System logs
* Security logs

---

# 31. Kubernetes Security

Security measures:

* RBAC
* Network policies
* Secret management
* Image scanning
* Pod security policies

---

# 32. Helm

Helm is a Kubernetes package manager.

Install chart:

```bash id="e4zn5t"
helm install myapp chart
```

Benefits:

* Reusable templates
* Version control
* Easy deployment

---

# 33. CI/CD Integration

Common tools:

* Jenkins
* GitHub Actions
* GitLab CI
* ArgoCD

Pipeline stages:

```text id="m7qd4n"
Code
 ↓
Build
 ↓
Test
 ↓
Docker
 ↓
Deploy
 ↓
Monitor
```

---

# 34. Production Best Practices

Teams should:

* Use namespaces
* Configure resource limits
* Enable monitoring
* Implement backups
* Use secrets
* Configure autoscaling
* Enable security policies

---

# 35. Mini Projects

Recommended projects:

* FastAPI Docker deployment
* Kubernetes web application
* CI/CD pipeline
* Monitoring dashboard
* Microservices deployment
* Enterprise RAG deployment

---

# 36. Assessment

Evaluation criteria:

| Component   | Weightage |
| ----------- | --------- |
| Assignments | 20%       |
| Labs        | 30%       |
| Project     | 40%       |
| Viva        | 10%       |

Passing score:

```text id="a3jw8f"
70%
```

---

# 37. Frequently Asked Questions

### Q1. Is Docker mandatory?

Yes.

### Q2. Is Kubernetes required for production?

Yes.

### Q3. Should containers be monitored?

Yes.

### Q4. Are secrets stored in ConfigMaps?

No.

### Q5. Is Helm recommended?

Yes.

---

# 38. Training Ownership

This Docker and Kubernetes Training Manual is maintained jointly by the Learning & Development Department, DevOps Team, Engineering Team, and Site Reliability Engineering Team of TechNova Solutions Pvt. Ltd.
