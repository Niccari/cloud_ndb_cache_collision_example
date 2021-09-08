import os

from fastapi import FastAPI
from fastapi import Request
from google.cloud import ndb
from redis_namespace import StrictRedis

app = FastAPI()


class Sample(ndb.Model):
    pass


@app.middleware("http")
async def use_datastore_context(request: Request, call_next):
    datastore_client = \
        ndb.Client(project=os.getenv("DATASTORE_PROJECT_ID"))
    datastore_cache = ndb.RedisCache(StrictRedis(
        host="localhost", port="6379", namespace="ndb:"))
    with datastore_client.context(
            global_cache=datastore_cache,
            global_cache_timeout_policy=24 * 60 * 60):
        response = await call_next(request)
        return response


@app.get("/")
async def test():
    user_id1 = 5761297639538688
    user_id2 = 5704016969334784

    def txn1():
        entity = Sample(id=user_id1)
        entity.put()

    def txn2():
        entity = Sample(id=user_id2)
        entity.put()

    sample1 = Sample.get_by_id(user_id1)
    sample2 = Sample.get_by_id(user_id2)
    if sample1 is None:
        ndb.transaction(txn1)
        sample1 = Sample.get_by_id(user_id1)
    if sample2 is None:
        ndb.transaction(txn2)
        sample2 = Sample.get_by_id(user_id2)

    print(f"sample1: {sample1.key.id()}, sample2: {sample2.key.id()}")

    return {}
