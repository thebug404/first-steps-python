# First steps in Python

In this repository you will find simple scripts to learn basic concepts about python.

## Requirements

- [Python](https://www.python.org/downloads/) (version 3 or higher)
- [Git](https://git-scm.com/)
- [VSCode](https://code.visualstudio.com/) (or another code editor of your choice)

## Clone

```bash
git clone https://github.com/thebug404/first-steps-python.git

cd first-steps-python
```

## Configure the virtual environment

Create a new virtual environment:

```bash
python -m venv venv
```

> **Note**: this action may last a few seconds.

Activate the virtual environment:

**For users Windows**

```bash
venv\Scripts\activate
```

**For users Linux/Mac**

```bash
source venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## File generation + Http Request

The file `generate_files_http_request.py` is a script that makes an http request https://jsonplaceholder.typicode.com/users, iterates through the list of users and for each element present in the list it generates a unique file based on the name of the user plus a hash.
