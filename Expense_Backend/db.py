# db.py
from motor.motor_asyncio import AsyncIOMotorClient

mongoURL = "mongodb+srv://admin:admin@cluster.xaq58zj.mongodb.net/?appName=Cluster"

client = AsyncIOMotorClient(mongoURL, tls=True,
    tlsAllowInvalidCertificates=True)

database = client["ExpenseDB"]

user_collection = database["users"]
expense_collection = database["expenses"]
