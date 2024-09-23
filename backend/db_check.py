import os
from dotenv import load_dotenv

load_dotenv()

print(f"DB_NAME: {os.environ.get('DB_NAME')}")
print(f"DB_USER: {os.environ.get('DB_USER')}")
print(f"DB_PASSWORD: {os.environ.get('DB_PASSWORD')}")
print(f"DB_HOST: {os.environ.get('DB_HOST')}")
