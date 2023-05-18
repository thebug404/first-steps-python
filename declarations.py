from typing import TypedDict

class Geo(TypedDict):
  lat: str
  lng: str

class Address(TypedDict):
  street: str
  suite: str
  city: str
  zipcode: str
  geo: Geo

class Company(TypedDict):
  name: str
  catchPhrase: str
  bs: str

class User(TypedDict):
  id: int
  name: str
  username: str
  email: str
  address: Address
  phone: str
  website: str
  company: Company

