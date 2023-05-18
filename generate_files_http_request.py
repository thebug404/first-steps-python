from typing import List
import requests
import json

from declarations import User

from file_service import FileService, Resource, Query

BASE_URL = "https://jsonplaceholder.typicode.com/users"

file_service = FileService()

response = requests.get(BASE_URL)

users: List[User] = response.json()

for user in users:
  name = user["name"].lower().replace(" ", "-")

  filename = f"{name}.json"

  data: Resource = {
    "name": filename,
    "data": json.dumps(user)
  }

  query: Query = {
    "folder": "dump"
  }

  file_service.create(data, query)

print("Files generated successfully.")


