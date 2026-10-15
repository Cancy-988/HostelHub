from pymongo import MongoClient

client = MongoClient(
    "mongodb://localhost:27017/",
    serverSelectionTimeoutMS=5000
)

try:
    client.admin.command("ping")
    print("MongoDB connected successfully!")

    db = client["HostelHub"]
    students= db["students"]
    rooms= db["rooms"]
    maintenance_staff= db["maintenance_staff"]
    complaints=db["complaints"]
    print("Database:", db.name)
    print("Collections ready!")


   

except Exception as e:
    print("Connection error:", e)

