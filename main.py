from typing import List, TypedDict
import requests
import json
import os

from declarations import User

from utils import generate_unique_filename

BASE_URL = "https://jsonplaceholder.typicode.com/users"

response = requests.get(BASE_URL)

users: List[User] = response.json()

for user in users:
  name = user["name"].lower().replace(" ", "-")
  directory_name = "dump"

  filename = generate_unique_filename(f"{name}.json")

  if not os.path.exists(directory_name):
    os.mkdir(directory_name)

  fullpath = f"{directory_name}/{filename}"

  file = open(f"{directory_name}/{filename}", "w+")

  file.write(json.dumps(user))

  file.close()

print("The file has been created successfully!!!")
