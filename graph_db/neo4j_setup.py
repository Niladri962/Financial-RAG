from neo4j import GraphDatabase
from dotenv import load_dotenv
from pathlib import Path
import os

# Load .env explicitly from Financial-RAG root
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")

print("URI:", URI)
print("USERNAME:", USERNAME)

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)