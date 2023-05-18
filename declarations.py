from typing import TypedDict

class User(TypedDict):
  id: int
  name: str
  username: str
  email: str
  address: dict
  phone: str
  website: str
  company: dict
