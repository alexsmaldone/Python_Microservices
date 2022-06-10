from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel

app = FastAPI()
redis = get_redis_connection(
  host="redis-14476.c14.us-east-1-3.ec2.cloud.redislabs.com:14476",
  port=14476,
  password="rs69yioSEvrpqkmjHJGFQuavL4YrCGf4",
  decode_responses=True
)

class Product(HashModel):
  name: str
  price: float
  quantity: int

  class Meta:
    database = redis

@app.get('/products')
def all():
  return []
