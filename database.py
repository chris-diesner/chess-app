from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

db = client["chess_db"]
games_collection = db["games"]
users_collection = db["users"]

print("✅ Verbindung zur MongoDB Atlas hergestellt!")
