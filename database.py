from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["HostelHub"]

students = db["students"]
rooms = db["rooms"]
maintenance_staff = db["maintenance_staff"]
complaints = db["complaints"]

print("MongoDB connected successfully!")