import random
import os

def generate_unique_filename(filename: str) -> str:
  hash = generate_random_key()

  filename_chunks = os.path.splitext(filename)

  name = filename_chunks[0]
  ext = filename_chunks[1]

  return f"{name}-{hash}{ext}"

def generate_random_key(length = 10):
  result = ''

  characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
  
  for _ in range(length):
    result += random.choice(characters)
  
  return result