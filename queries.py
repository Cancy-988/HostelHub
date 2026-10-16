from database import students, complaints, rooms


# 1. Find all pending complaints


print("\n--- PENDING COMPLAINTS ---")

for complaint in complaints.find(
    {"status": "Pending"},
    {"_id": 0}
):
    print(complaint)


# 2. Find high priority complaints


print("\n--- HIGH PRIORITY COMPLAINTS ---")

for complaint in complaints.find(
    {"priority": "High"},
    {"_id": 0}
):
    print(complaint)

# 3. Find CSE students


print("\n--- CSE STUDENTS ---")

for student in students.find(
    {"department": "CSE"},
    {"_id": 0}
):
    print(student)

# 4. Find students in 3rd or 4th year


print("\n--- 3rd OR 4th YEAR STUDENTS ---")

for student in students.find(
    {"year": {"$in": [3, 4]}},
    {"_id": 0}
):
    print(student)

# 5. Find high priority pending complaints


print("\n--- HIGH PRIORITY + PENDING ---")

for complaint in complaints.find(
    {
        "$and": [
            {"priority": "High"},
            {"status": "Pending"}
        ]
    },
    {"_id": 0}
):
    print(complaint)


# 6. Find complaints that are NOT resolved


print("\n--- NOT RESOLVED COMPLAINTS ---")

for complaint in complaints.find(
    {"status": {"$ne": "Resolved"}},
    {"_id": 0}
):
    print(complaint)

# 7. Find complaints containing "issue"


print("\n--- COMPLAINTS WITH 'ISSUE' ---")

for complaint in complaints.find(
    {"description": {"$regex": "issue", "$options": "i"}},
    {"_id": 0}
):
    print(complaint)

# 8. Find available rooms


print("\n--- AVAILABLE ROOMS ---")

for room in rooms.find(
    {"$expr": {"$lt": ["$occupied", "$capacity"]}},
    {"_id": 0}
):
    print(room)