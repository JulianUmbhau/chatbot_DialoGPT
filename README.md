# chatbot_DialoGPT on Azure Web App

## Azure Web App service setup

Create env file with container variables
- subscriptionid=subscriptionid
- resgrp=resource-groupname
- location=location
- registryname=registryname
- serviceplan=serviceplanname
- containername=containername
- NAME=webappname

Source variables
```
source set-env.sh
```

Login
```
az login
```

Set subscription
```
az account set --subscription $subscriptionid
```

Create resource group
```
az group create --name $resgrp --location $location
```

Create container registry
```
az acr create --name $registryname --resource-group $resgrp --sku Basic --admin-enabled true
```

Build image locally
```
docker build --tag image-name Dockerfile-path
```

Run image locally
```
docker run --rm -p 80:80 image-name
```

Tag image for upload to Azure
```
docker tag image-name $registryname.azurecr.io/$containername
```

Login to Azure registry
```
az acr login --name $registryname
```

Push image to registry
```
docker push $registryname.azurecr.io/$containername
```

Create serviceplan
```
az appservice plan create --name $serviceplan --resource-group $resgrp --sku B1 --location $location
```

Create web app service
```
az webapp create --name $NAME --resource-group $resgrp --plan $serviceplan 
```

Deploy image
Unsure of CLI method - Do through portal 




