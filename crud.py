from database import students, complaints

# CREATE


def add_student(student):
    result = students.insert_one(student)
    print("Student added:", result.inserted_id)

# READ


def get_all_students():
    data = students.find({}, {"_id": 0})

    for student in data:
        print(student)


# UPDATE


def update_complaint_status(complaint_id, new_status):
    result = complaints.update_one(
        {"complaintId": complaint_id},
        {"$set": {"status": new_status}}
    )

    print("Documents updated:", result.modified_count)

# DELETE


def delete_student(student_id):
    result = students.delete_one(
        {"studentId": student_id}
    )

    print("Documents deleted:", result.deleted_count)

# TEST CRUD


print("\nREAD STUDENTS ")
get_all_students()

print("\n ADD STUDENT ")

new_student = {
    "studentId": "ST021",
    "name": "Neha Sharma",
    "email": "neha@gmail.com",
    "phone": "9876500021",
    "department": "CSE",
    "year": 3,
    "roomNumber": "C102"
}

add_student(new_student)

print("\n UPDATE COMPLAINT ")
update_complaint_status("C001", "Resolved")

print("\nDELETE STUDENT ")
delete_student("ST021")