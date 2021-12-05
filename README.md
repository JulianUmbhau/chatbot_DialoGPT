# chatbot_DialoGPT on Azure Web App


Create env file with container variables

Create resource group
Create container registry
Upload image
Create serveiceplan
Create web app service
Deploy image


source set-env.sh

az login
az account set --subscription $subscriptionid
az group create --name $resgrp --location $location
az acr create --name $registryname --resource-group $resgrp --sku Basic --admin-enabled true

docker build --tag image-name Dockerfile-path \
docker run --rm -p 80:80 image-name \
docker tag image-name $registryname.azurecr.io/$containername \
az acr login --name $registryname \
docker push $registryname.azurecr.io/$containername \

az appservice plan create --name $serviceplan --resource-group $resgrp --sku B1 --location $location
az webapp create --name $NAME --resource-group $resgrp --plan $serviceplan 