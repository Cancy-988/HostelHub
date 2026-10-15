from database import (
    students,
    rooms,
    maintenance_staff,
    complaints
)

# -------------------------
# STUDENTS
# -------------------------

students.insert_many([
    {
        "studentId": "ST101",
        "name": "Priya Sharma",
        "email": "priya@gmail.com",
        "department": "CSE",
        "year": 3,
        "roomNumber": "A-203"
    },
    {
        "studentId": "ST102",
        "name": "Rahul Kumar",
        "email": "rahul@gmail.com",
        "department": "ECE",
        "year": 2,
        "roomNumber": "A-204"
    },
    {
        "studentId": "ST103",
        "name": "Neha Verma",
        "email": "neha@gmail.com",
        "department": "CSE",
        "year": 3,
        "roomNumber": "B-101"
    }
])

# -------------------------
# ROOMS
# -------------------------

rooms.insert_many([
    {
        "roomNumber": "A-203",
        "block": "A",
        "capacity": 3,
        "occupied": 2,
        "roomType": "Triple"
    },
    {
        "roomNumber": "A-204",
        "block": "A",
        "capacity": 2,
        "occupied": 2,
        "roomType": "Double"
    },
    {
        "roomNumber": "B-101",
        "block": "B",
        "capacity": 3,
        "occupied": 1,
        "roomType": "Triple"
    }
])

# -------------------------
# MAINTENANCE STAFF
# -------------------------

maintenance_staff.insert_many([
    {
        "staffId": "M201",
        "name": "Amit Kumar",
        "specialization": "Electrical",
        "available": True
    },
    {
        "staffId": "M202",
        "name": "Rahul Singh",
        "specialization": "Plumbing",
        "available": True
    }
])

# -------------------------
# COMPLAINTS
# -------------------------

complaints.insert_many([
    {
        "complaintId": "C101",
        "studentId": "ST101",
        "roomNumber": "A-203",
        "category": "Electrical",
        "description": "Fan is not working",
        "priority": "High",
        "status": "Pending",
        "assignedTo": "M201"
    },
    {
        "complaintId": "C102",
        "studentId": "ST102",
        "roomNumber": "A-204",
        "category": "Plumbing",
        "description": "Water tap is leaking",
        "priority": "Medium",
        "status": "In Progress",
        "assignedTo": "M202"
    },
    {
        "complaintId": "C103",
        "studentId": "ST101",
        "roomNumber": "A-203",
        "category": "Cleaning",
        "description": "Room cleaning required",
        "priority": "Low",
        "status": "Resolved",
        "assignedTo": None
    }
])

print("Sample data inserted successfully!")