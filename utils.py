import random

def generate_random_key(length = 10):
  result = ''

  characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
  
  for _ in range(length):
    result += random.choice(characters)
  
  return result