from typing import List, TypedDict
import requests
import os
import json

from utils import generate_random_key

class User(TypedDict):
  id: int
  name: str
  username: str
  email: str
  address: dict
  phone: str
  website: str
  company: dict

BASE_URL = "https://jsonplaceholder.typicode.com/users"

response = requests.get(BASE_URL)

users: List[User] = response.json()

for user in users:
  hash = generate_random_key()
  name = user["name"].lower().replace(" ", "-")
  filename = f"{name}-{hash}.json"
  directory_name = "dump"

  if not os.path.exists(directory_name):
    os.mkdir(directory_name)

  fullpath = f"{directory_name}/{filename}"

  print(fullpath)

  file = open(f"{directory_name}/{filename}", "w+")

  file.write(json.dumps(user))

  file.close()

  print("The file has been created successfully!!!")
