#!/bin/bash

$(gcloud beta emulators datastore env-init)
uvicorn application:app --host 0.0.0.0 --port 8000 --workers 2

