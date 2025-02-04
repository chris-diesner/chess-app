import os
from pymongo import MongoClient
from dotenv import load_dotenv

# .env laden (lokal), aber GitHub Actions nutzt die Secrets automatisch
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("❌ Fehler: MONGO_URI ist nicht gesetzt!")

client = MongoClient(MONGO_URI)
db = client["chess_db"]

# Collections definieren
users_collection = db["users"]
games_collection = db["games"]
moves_collection = db["moves_history"]

print("✅ Verbindung zu MongoDB hergestellt!")
