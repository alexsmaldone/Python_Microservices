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

# This should be a different database
redis = get_redis_connection(
  host="redis-14476.c14.us-east-1-3.ec2.cloud.redislabs.com",
  port=14476,
  password="rs69yioSEvrpqkmjHJGFQuavL4YrCGf4",
  decode_responses=True
)
