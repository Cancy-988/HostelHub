from database import students, rooms, maintenance_staff, complaints
from datetime import datetime, timedelta
import random

from database import students, rooms, maintenance_staff, complaints
from datetime import datetime, timedelta
import random


# ==========================================
# CLEAR OLD DATA BEFORE SEEDING
# ==========================================

students.delete_many({})
rooms.delete_many({})
maintenance_staff.delete_many({})
complaints.delete_many({})

print("Old data cleared successfully!")


#  STUDENT DATA


students_data = [
    {
        "studentId": "ST001",
        "name": "Aarav Sharma",
        "email": "aarav@gmail.com",
        "phone": "9876500001",
        "department": "CSE",
        "year": 3,
        "roomNumber": "A101"
    },
    {
        "studentId": "ST002",
        "name": "Ananya Verma",
        "email": "ananya@gmail.com",
        "phone": "9876500002",
        "department": "ECE",
        "year": 2,
        "roomNumber": "A102"
    },
    {
        "studentId": "ST003",
        "name": "Rahul Kumar",
        "email": "rahul@gmail.com",
        "phone": "9876500003",
        "department": "CSE",
        "year": 4,
        "roomNumber": "A103"
    },
    {
        "studentId": "ST004",
        "name": "Priya Singh",
        "email": "priya@gmail.com",
        "phone": "9876500004",
        "department": "IT",
        "year": 3,
        "roomNumber": "A104"
    },
    {
        "studentId": "ST005",
        "name": "Rohan Gupta",
        "email": "rohan@gmail.com",
        "phone": "9876500005",
        "department": "ME",
        "year": 2,
        "roomNumber": "A105"
    },
    {
        "studentId": "ST006",
        "name": "Sneha Patel",
        "email": "sneha@gmail.com",
        "phone": "9876500006",
        "department": "CSE",
        "year": 3,
        "roomNumber": "B101"
    },
    {
        "studentId": "ST007",
        "name": "Aditya Singh",
        "email": "aditya@gmail.com",
        "phone": "9876500007",
        "department": "ECE",
        "year": 4,
        "roomNumber": "B102"
    },
    {
        "studentId": "ST008",
        "name": "Isha Mehta",
        "email": "isha@gmail.com",
        "phone": "9876500008",
        "department": "IT",
        "year": 2,
        "roomNumber": "B103"
    },
    {
        "studentId": "ST009",
        "name": "Karan Malhotra",
        "email": "karan@gmail.com",
        "phone": "9876500009",
        "department": "CSE",
        "year": 4,
        "roomNumber": "B104"
    },
    {
        "studentId": "ST010",
        "name": "Simran Kaur",
        "email": "simran@gmail.com",
        "phone": "9876500010",
        "department": "CE",
        "year": 3,
        "roomNumber": "B105"
    },
    {
        "studentId": "ST011",
        "name": "Arjun Sharma",
        "email": "arjun@gmail.com",
        "phone": "9876500011",
        "department": "CSE",
        "year": 2,
        "roomNumber": "C101"
    },
    {
        "studentId": "ST012",
        "name": "Nisha Gupta",
        "email": "nisha@gmail.com",
        "phone": "9876500012",
        "department": "ECE",
        "year": 3,
        "roomNumber": "C102"
    },
    {
        "studentId": "ST013",
        "name": "Vivek Kumar",
        "email": "vivek@gmail.com",
        "phone": "9876500013",
        "department": "IT",
        "year": 4,
        "roomNumber": "C103"
    },
    {
        "studentId": "ST014",
        "name": "Mehak Sharma",
        "email": "mehak@gmail.com",
        "phone": "9876500014",
        "department": "CSE",
        "year": 3,
        "roomNumber": "C104"
    },
    {
        "studentId": "ST015",
        "name": "Yash Raj",
        "email": "yash@gmail.com",
        "phone": "9876500015",
        "department": "ME",
        "year": 2,
        "roomNumber": "C105"
    },
    {
        "studentId": "ST016",
        "name": "Kriti Sharma",
        "email": "kriti@gmail.com",
        "phone": "9876500016",
        "department": "CSE",
        "year": 4,
        "roomNumber": "A101"
    },
    {
        "studentId": "ST017",
        "name": "Mohit Verma",
        "email": "mohit@gmail.com",
        "phone": "9876500017",
        "department": "ECE",
        "year": 3,
        "roomNumber": "A102"
    },
    {
        "studentId": "ST018",
        "name": "Riya Kapoor",
        "email": "riya@gmail.com",
        "phone": "9876500018",
        "department": "IT",
        "year": 2,
        "roomNumber": "B101"
    },
    {
        "studentId": "ST019",
        "name": "Dev Kumar",
        "email": "dev@gmail.com",
        "phone": "9876500019",
        "department": "CSE",
        "year": 4,
        "roomNumber": "B102"
    },
    {
        "studentId": "ST020",
        "name": "Pooja Singh",
        "email": "pooja@gmail.com",
        "phone": "9876500020",
        "department": "CE",
        "year": 3,
        "roomNumber": "C101"
    }
]

students.insert_many(students_data)


# --------------------------------
# 3. ROOM DATA
# --------------------------------

rooms_data = [
    {
        "roomNumber": "A101",
        "block": "A",
        "floor": 1,
        "capacity": 2,
        "occupied": 2,
        "roomType": "Double"
    },
    {
        "roomNumber": "A102",
        "block": "A",
        "floor": 1,
        "capacity": 2,
        "occupied": 2,
        "roomType": "Double"
    },
    {
        "roomNumber": "A103",
        "block": "A",
        "floor": 1,
        "capacity": 2,
        "occupied": 1,
        "roomType": "Double"
    },
    {
        "roomNumber": "A104",
        "block": "A",
        "floor": 1,
        "capacity": 2,
        "occupied": 1,
        "roomType": "Double"
    },
    {
        "roomNumber": "A105",
        "block": "A",
        "floor": 1,
        "capacity": 3,
        "occupied": 1,
        "roomType": "Triple"
    },
    {
        "roomNumber": "B101",
        "block": "B",
        "floor": 1,
        "capacity": 2,
        "occupied": 2,
        "roomType": "Double"
    },
    {
        "roomNumber": "B102",
        "block": "B",
        "floor": 1,
        "capacity": 2,
        "occupied": 2,
        "roomType": "Double"
    },
    {
        "roomNumber": "B103",
        "block": "B",
        "floor": 1,
        "capacity": 3,
        "occupied": 1,
        "roomType": "Triple"
    },
    {
        "roomNumber": "B104",
        "block": "B",
        "floor": 1,
        "capacity": 2,
        "occupied": 1,
        "roomType": "Double"
    },
    {
        "roomNumber": "B105",
        "block": "B",
        "floor": 1,
        "capacity": 3,
        "occupied": 1,
        "roomType": "Triple"
    },
    {
        "roomNumber": "C101",
        "block": "C",
        "floor": 1,
        "capacity": 2,
        "occupied": 2,
        "roomType": "Double"
    },
    {
        "roomNumber": "C102",
        "block": "C",
        "floor": 1,
        "capacity": 2,
        "occupied": 1,
        "roomType": "Double"
    },
    {
        "roomNumber": "C103",
        "block": "C",
        "floor": 1,
        "capacity": 3,
        "occupied": 1,
        "roomType": "Triple"
    }
]

rooms.insert_many(rooms_data)


# 4. MAINTENANCE STAFF


staff_data = [
    {
        "staffId": "M001",
        "name": "Amit Kumar",
        "specialization": "Electrical",
        "phone": "9811100001",
        "available": True
    },
    {
        "staffId": "M002",
        "name": "Rajesh Singh",
        "specialization": "Plumbing",
        "phone": "9811100002",
        "available": True
    },
    {
        "staffId": "M003",
        "name": "Suresh Kumar",
        "specialization": "Cleaning",
        "phone": "9811100003",
        "available": True
    },
    {
        "staffId": "M004",
        "name": "Manoj Sharma",
        "specialization": "Furniture",
        "phone": "9811100004",
        "available": False
    },
    {
        "staffId": "M005",
        "name": "Vijay Verma",
        "specialization": "Internet",
        "phone": "9811100005",
        "available": True
    }
]

maintenance_staff.insert_many(staff_data)



# 5. COMPLAINT DATA


categories = [
    "Electrical",
    "Plumbing",
    "Cleaning",
    "Furniture",
    "Internet"
]

priorities = [
    "Low",
    "Medium",
    "High"
]

statuses = [
    "Pending",
    "In Progress",
    "Resolved"
]

staff_ids = [
    "M001",
    "M002",
    "M003",
    "M004",
    "M005"
]

student_list = students_data
room_numbers = [room["roomNumber"] for room in rooms_data]

complaints_data = []

for i in range(1, 31):

    student = random.choice(student_list)
    category = random.choice(categories)
    priority = random.choice(priorities)
    status = random.choice(statuses)

    created_date = datetime.now() - timedelta(
        days=random.randint(1, 60)
    )

    complaint = {
        "complaintId": f"C{i:03d}",
        "studentId": student["studentId"],
        "roomNumber": student["roomNumber"],
        "category": category,
        "description": f"{category} issue reported in room {student['roomNumber']}",
        "priority": priority,
        "status": status,
        "assignedTo": random.choice(staff_ids),
        "createdAt": created_date
    }

    if status == "Resolved":
        complaint["resolvedAt"] = created_date + timedelta(
            days=random.randint(1, 5)
        )
    else:
        complaint["resolvedAt"] = None

    complaints_data.append(complaint)


complaints.insert_many(complaints_data)



# 6. SUCCESS MESSAGE



print("HostelHub data inserted successfully!")


print("Students:", students.count_documents({}))
print("Rooms:", rooms.count_documents({}))
print("Staff:", maintenance_staff.count_documents({}))
print("Complaints:", complaints.count_documents({}))