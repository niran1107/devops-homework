# Density DevOps Homework Assignment

In order to access app-a application you will need to install ingress controller on the cluster. 
I used nginx-ingress (https://github.com/helm/charts/tree/master/stable/nginx-ingress)

## Auto-Scale

manifests/hpa.yaml

## Blue Green Deployment ##
In order to install continuous delivery we will create identical environment, test its functionality and performance. Once the testing results are successful, application traffic is routed from the old environment (blue) to the new one (green). 
If there is an issue after green becomes live, traffic can be routed back to blue.

