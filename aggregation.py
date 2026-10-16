from database import complaints


print("\n--- COMPLAINTS BY CATEGORY ---")

result = complaints.aggregate([
    {
        "$group": {
            "_id": "$category",
            "total": {"$sum": 1}
        }
    },
    {
        "$sort": {
            "total": -1
        }
    }
])

for data in result:
    print(data)


print("\n--- COMPLAINTS BY STATUS ---")

result = complaints.aggregate([
    {
        "$group": {
            "_id": "$status",
            "total": {"$sum": 1}
        }
    }
])

for data in result:
    print(data)


print("\n--- STAFF WORKLOAD ---")

result = complaints.aggregate([
    {
        "$group": {
            "_id": "$assignedTo",
            "totalComplaints": {"$sum": 1}
        }
    },
    {
        "$sort": {
            "totalComplaints": -1
        }
    }
])

for data in result:
    print(data)


print("\n--- HIGH PRIORITY COMPLAINTS BY CATEGORY ---")

result = complaints.aggregate([
    {
        "$match": {
            "priority": "High"
        }
    },
    {
        "$group": {
            "_id": "$category",
            "total": {"$sum": 1}
        }
    }
])

for data in result:
    print(data)