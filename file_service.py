from typing import TypedDict
import os

from utils import generate_unique_filename

class Resource(TypedDict):
  name: str
  ext: str
  size: float
  data: str

class Query(TypedDict):
  folder: str

class FileService():
  def create (self, data: Resource, query: Query):
    folder = query["folder"]

    if not os.path.exists(folder):
      os.mkdir(folder)
    
    filename = generate_unique_filename(data["name"])

    fullpath = f"{folder}/{filename}"

    print(fullpath)

    file = open(file=fullpath, mode="w+")

    file.write(data["data"])

    file.close()
