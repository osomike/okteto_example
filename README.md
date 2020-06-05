
# Developing and debugging apps using Okteto

In order to run this example you will need to have:
1. A kubernetes environment ready to use.
2. Kubectl installed and configured for the Kubernetes environment
3. Okteto installed

### Notes:

### 1. Creating a Kubernetes Cluster in Azure
For more details, please refer to this [azure-deployment](https://docs.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster) tutorial.

To list the possible location of your cluster:
```sh
$ az account list-locations
```

To create a resource group called **OscarMikeResourceGroup** in **France**:
```sh
$ az group create --name OscarMikeResourceGroup --location francecentral
```

To create a Cluster on the resrource **OscarMikeResourceGroup** with the name **OscarMikeK8sCluster**:
```sh
$ az aks create --resource-group OscarMikeResourceGroup --name OscarMikeK8sCluster --node-count 3 --enable-addons monitoring --generate-ssh-keys
```

### 2. Configuring your local kubectl with the cluster you just created.
To install azure-cli locally:
```sh
$ pip install azure-cli
```

To login with your azure credentials:
```sh
$ az loging
```

To get your credentials for our Kubernetes cluster:
```sh
$ az aks get-credentials --resource-group OscarMikeResourceGroup --name OscarMikeK8sCluster
```
