##Build
`docker build . --tag python-flask-docker`

##Run
`docker run -d -p 5000:8081 python-flask-docker`


# Kubernetes
## Docker images build
## Setup to use docker deamon of minikube to avoid loading images
`docker build . --tag python-flask-kube`

## Apply using kubectl
`minikube image load python-flask-kube:latest`
`kubectl create --filename deployment.yaml`
`kubectl create --filename service.yaml`
`kubectl get all`
`kubectl get services`

`minikube tunnel`
### Use another terminal to get all to see services external ip from pending to 127.0.0.1

# Installing minikube
## Install chocolatey (ensure Power shell in admin mode while using choco or minikube)
https://chocolatey.org/install

`choco install minikube`

`minikube start`


