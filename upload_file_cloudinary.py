from dotenv import load_dotenv
import json
import os

load_dotenv()

import cloudinary
import cloudinary.uploader
import cloudinary.api

from file_service import FileService, Resource, Query

CLOUDINARY_CLOUDNAME = os.getenv("CLOUDINARY_CLOUDNAME")
CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
CLOUDINARY_SECRET_KEY = os.getenv("CLOUDINARY_SECRET_KEY")

cloudinary.config(
  cloud_name=CLOUDINARY_CLOUDNAME,
  api_key=CLOUDINARY_API_KEY,
  api_secret=CLOUDINARY_SECRET_KEY
)

response = cloudinary.uploader.upload("image.jpg")

file_service = FileService()

payload: Resource = {
  "name": "response.json",
  "data": json.dumps(response)
}

query: Query = {
  "folder": "logs"
}

file_service.create(data=payload, query=query)

print("Upload file successfully!")
