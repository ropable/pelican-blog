Title: Kubernetes
Date: 2020-11-26 14:15
Slug: kubernetes
Author: Ashley Felton
Summary: Notes related to my learning about Kubernetes

Installation
-----

In an Ubuntu host CLI, we can use snap to install microk8s for testing.
Put the current user in the microk8s group and alias the kubectl command also.

~~~bash
sudo snap install microk8s --classic
sudo usermod -a -G microk8s <username>
echo "alias kubectl='microk8s.kubectl'" >> ~/.bashrc
# Enable CoreDNS:
microk8s.enable dns
# Check status of what is running:
microk8s.status
~~~

Basic interaction, exploring resource types:

~~~bash
kubectl get nodes
kubectl get nodes -o wide
kubectl get nodes -o yaml

kubectl describe nodes/<node name>
# Show available resource types:
kubectl api-resources
kubectl explain <type>
kubectl explain node.kind
kubectl explain node --recursive
~~~

Namespace basics

~~~bash
kubectl get namespaces
kubectl get pods --all-namespaces
kubectl get pods --namespace default
~~~

Run a pod:

~~~bash
# Equivalent to docker run command.
kubectl run pingpong  --image alpine ping 1.1.1.1
kubectl logs pod/pingping --tail 1 --follow
~~~
