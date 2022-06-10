from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=['http://localhost:3000'],
  allow_methods=['*'],
  allow_headers=['*']
)

redis = get_redis_connection(
  host="redis-14476.c14.us-east-1-3.ec2.cloud.redislabs.com",
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
  return Product.all_pks()

@app.post('/products')
def create(product: Product):
  return product.save()
