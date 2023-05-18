from typing import List
import requests
import json

from declarations import User

from file_service import FileService

file_service = FileService()

BASE_URL = "https://jsonplaceholder.typicode.com/users"

response = requests.get(BASE_URL)

users: List[User] = response.json()

for user in users:
  name = user["name"].lower().replace(" ", "-")

  filename = f"{name}.json"

  data = {"name": filename, "data": json.dumps(user)}

  query = {"folder": "dump"}

  file_service.create(data, query)

print("The file has been created successfully!!!")
