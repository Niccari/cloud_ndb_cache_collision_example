# Cloud NDB: Global Cache collision sample project (as of Sep. 8, 2021)

## Installation
1. install Datastore Emulator and related gcloud components

```bash
$ gcloud components install beta cloud-datastore-emulator app-engine-python app-engine-python-extras
```

2. Create a python virtual environment
```bash
$ pipenv install
$ pipenv shell
```

3. Install redis-server and launch it


## Usage
1. Launch the datastore emulator (in another terminal)
```bash
$ gcloud beta emulators datastore start
```

2. Run the test server (The internal script will set environmental variables automatically)
```bash
$ pipenv run start
```

3. Access to http://localhost:8000/ (at least twice).

### Result example
The below result will be given if the redis cache and the datastore are empty.

In the first result, the IDs of the two samples are different(correct).

However, in the second and subsequent result, they have the same ID(wrong).

```
$ pipenv run start
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started parent process [34729]
INFO:     Started server process [34732]
INFO:     Started server process [34731]
INFO:     Waiting for application startup.
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Application startup complete.
sample1: 5761297639538688, sample2: 5704016969334784
INFO:     127.0.0.1:65521 - "GET / HTTP/1.1" 200 OK
sample1: 5761297639538688, sample2: 5761297639538688
INFO:     127.0.0.1:65521 - "GET / HTTP/1.1" 200 OK
sample1: 5761297639538688, sample2: 5761297639538688
INFO:     127.0.0.1:65522 - "GET / HTTP/1.1" 200 OK
```

