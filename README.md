# Cloud Run Hello World Sample

This sample shows how to deploy a Hello World application to Cloud Run.

## Build

```
docker build --tag helloworld:python .
```

## Run Locally

```
docker run --rm -p 9090:8080 -e PORT=8080 helloworld:python
```

## Test

```
pytest
```

_Note: you may need to install `pytest` using `pip install pytest`._

## Deploy

```sh
# Set an environment variable with your GCP Project ID
export GOOGLE_CLOUD_PROJECT=<PROJECT_ID>

# Submit a build using Google Cloud Build
gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/cr-demo-backend

# Deploy to Cloud Run
gcloud run deploy cr-demo-backend \
--image gcr.io/${GOOGLE_CLOUD_PROJECT}/cr-demo-backend
```
