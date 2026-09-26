# db.py
from motor.motor_asyncio import AsyncIOMotorClient

mongoURL = "mongodb://210120116054:210120116054@<hostname>/?ssl=true&replicaSet=atlas-l9vouv-shard-0&authSource=admin&appName=Project&compressors=zlib"

client = AsyncIOMotorClient(mongoURL, tls=True,
    tlsAllowInvalidCertificates=True)

database = client["ExpenseDB"]

user_collection = database["users"]
expense_collection = database["expenses"]
