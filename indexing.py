from database import students, complaints


# =====================================
# 1. UNIQUE INDEX ON STUDENT ID
# =====================================

students.create_index(
    "studentId",
    unique=True
)

print("Student ID index created")


# =====================================
# 2. UNIQUE INDEX ON COMPLAINT ID
# =====================================

complaints.create_index(
    "complaintId",
    unique=True
)

print("Complaint ID index created")


# =====================================
# 3. INDEX ON COMPLAINT STATUS
# =====================================

complaints.create_index("status")

print("Status index created")


# =====================================
# 4. INDEX ON CATEGORY
# =====================================

complaints.create_index("category")

print("Category index created")


# =====================================
# 5. COMPOUND INDEX
# =====================================

complaints.create_index(
    [
        ("status", 1),
        ("createdAt", -1)
    ]
)

print("Compound index created")


# =====================================
# 6. DISPLAY INDEXES
# =====================================

print("\n--- STUDENT INDEXES ---")

for index in students.list_indexes():
    print(index)


print("\n--- COMPLAINT INDEXES ---")

for index in complaints.list_indexes():
    print(index)