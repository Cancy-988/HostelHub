import streamlit as st
from database import students, rooms, maintenance_staff, complaints
from datetime import datetime

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="HostelHub",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: white;
}

/* Main title */
h1 {
    font-weight: 700;
}

/* Metric cards */
div[data-testid="metric-container"] {
    background-color: white;
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

/* Buttons */
.stButton > button {
    border-radius: 8px;
    font-weight: 600;
}

/* Tables */
div[data-testid="stDataFrame"] {
    border-radius: 10px;
}

/* Divider */
hr {
    margin-top: 10px;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown(
        "<h1 style='text-align:center;'>🏠 HostelHub</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;'>Hostel Management System</p>",
        unsafe_allow_html=True
    )

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "📊 Dashboard",
            "👨‍🎓 Students",
            "🛏️ Rooms",
            "🛠️ Maintenance Staff",
            "📋 Complaints",
            "📈 Analytics"
        ]
    )

    st.divider()

    st.caption("HostelHub Admin Panel")
    st.caption("MongoDB + PyMongo + Streamlit")


# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

if page == "📊 Dashboard":

    st.title("📊 Hostel Admin Dashboard")
    st.write("Overview of hostel operations and complaint management.")

    # =========================
    # BASIC COUNTS
    # =========================

    total_students = students.count_documents({})
    total_rooms = rooms.count_documents({})
    total_staff = maintenance_staff.count_documents({})

    pending_complaints = complaints.count_documents({
        "status": "Pending"
    })

    in_progress = complaints.count_documents({
        "status": "In Progress"
    })

    resolved_complaints = complaints.count_documents({
        "status": "Resolved"
    })

    total_complaints = complaints.count_documents({})

    # =========================
    # ROOM OCCUPANCY
    # =========================

    room_stats = list(
        rooms.aggregate([
            {
                "$group": {
                    "_id": None,
                    "totalCapacity": {
                        "$sum": "$capacity"
                    },
                    "totalOccupied": {
                        "$sum": "$occupied"
                    }
                }
            }
        ])
    )

    if room_stats:

        total_capacity = room_stats[0]["totalCapacity"]
        total_occupied = room_stats[0]["totalOccupied"]
        available_beds = total_capacity - total_occupied

        occupancy_percentage = (
            total_occupied / total_capacity * 100
            if total_capacity > 0
            else 0
        )

    else:

        total_capacity = 0
        total_occupied = 0
        available_beds = 0
        occupancy_percentage = 0

    # =========================
    # TOP METRICS
    # =========================

    st.subheader("📌 Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "👨‍🎓 Students",
        total_students
    )

    col2.metric(
        "🛏️ Rooms",
        total_rooms
    )

    col3.metric(
        "🛠️ Staff",
        total_staff
    )

    col4.metric(
        "📋 Complaints",
        total_complaints
    )

    st.divider()

    # =========================
    # COMPLAINT STATUS
    # =========================

    st.subheader("📋 Complaint Status")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Pending",
        pending_complaints
    )

    col2.metric(
        "In Progress",
        in_progress
    )

    col3.metric(
        "Resolved",
        resolved_complaints
    )

    st.divider()

    # =========================
    # ROOM OCCUPANCY
    # =========================

    st.subheader("🛏️ Room Occupancy")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Capacity",
        total_capacity
    )

    col2.metric(
        "Occupied Beds",
        total_occupied
    )

    col3.metric(
        "Available Beds",
        available_beds
    )

    st.progress(
        min(occupancy_percentage / 100, 1.0)
    )

    st.write(
        f"Occupancy Rate: **{occupancy_percentage:.1f}%**"
    )

    st.divider()

    # =========================
    # RECENT COMPLAINTS
    # =========================

    st.subheader("🕒 Recent Complaints")

    recent_complaints = list(
        complaints.find(
            {},
            {
                "_id": 0,
                "complaintId": 1,
                "studentId": 1,
                "category": 1,
                "priority": 1,
                "status": 1,
                "createdAt": 1
            }
        ).sort(
            "createdAt",
            -1
        ).limit(5)
    )

    if recent_complaints:

        st.dataframe(
            recent_complaints,
            use_container_width=True
        )

    else:

        st.info("No complaints found.")

    st.divider()

    # =========================
    # QUICK SUMMARY
    # =========================

    st.subheader("📊 Quick Summary")

    col1, col2 = st.columns(2)

    with col1:

        st.write("### Complaint Overview")

        complaint_chart = {
            "Pending": pending_complaints,
            "In Progress": in_progress,
            "Resolved": resolved_complaints
        }

        st.bar_chart(complaint_chart)

    with col2:

        st.write("### Room Overview")

        room_chart = {
            "Occupied": total_occupied,
            "Available": available_beds
        }

        st.bar_chart(room_chart)

    st.title("Dashboard")
    st.write("Welcome back, Admin 👋")

    st.divider()

    # Statistics

    total_students = students.count_documents({})
    total_rooms = rooms.count_documents({})
    total_staff = maintenance_staff.count_documents({})

    pending = complaints.count_documents({
        "status": "Pending"
    })

    resolved = complaints.count_documents({
        "status": "Resolved"
    })

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            "👨‍🎓 Students",
            total_students
        )

    with col2:
        st.metric(
            "🛏️ Rooms",
            total_rooms
        )

    with col3:
        st.metric(
            "🛠️ Staff",
            total_staff
        )

    with col4:
        st.metric(
            "⚠️ Pending",
            pending
        )

    with col5:
        st.metric(
            "✅ Resolved",
            resolved
        )

    st.divider()

    # Recent complaints

    st.subheader("📋 Recent Complaints")

    recent_complaints = list(
        complaints.find(
            {},
            {"_id": 0}
        ).sort(
            "createdAt",
            -1
        ).limit(8)
    )

    if recent_complaints:

        st.dataframe(
            recent_complaints,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info("No complaints found.")


# --------------------------------------------------
# STUDENTS
# --------------------------------------------------

# --------------------------------------------------
# STUDENTS
# --------------------------------------------------

elif page == "👨‍🎓 Students":

    st.title("👨‍🎓 Student Management")

    # -----------------------------
    # SEARCH
    # -----------------------------

    search = st.text_input(
        "🔍 Search student by name or student ID"
    )

    if search:

        student_data = list(
            students.find(
                {
                    "$or": [
                        {
                            "name": {
                                "$regex": search,
                                "$options": "i"
                            }
                        },
                        {
                            "studentId": {
                                "$regex": search,
                                "$options": "i"
                            }
                        }
                    ]
                },
                {"_id": 0}
            )
        )

    else:

        student_data = list(
            students.find(
                {},
                {"_id": 0}
            )
        )

    st.metric(
        "Total Students",
        students.count_documents({})
    )

    st.dataframe(
        student_data,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # -----------------------------
    # ADD STUDENT
    # -----------------------------

    st.subheader("➕ Add Student")

    with st.form("add_student_form"):

        col1, col2 = st.columns(2)

        with col1:

            student_id = st.text_input(
                "Student ID"
            )

            name = st.text_input(
                "Name"
            )

            email = st.text_input(
                "Email"
            )

            phone = st.text_input(
                "Phone"
            )

        with col2:

            department = st.selectbox(
                "Department",
                ["CSE", "ECE", "IT", "CE", "ME"]
            )

            year = st.selectbox(
                "Year",
                [1, 2, 3, 4]
            )

            room_number = st.text_input(
                "Room Number"
            )

        submit = st.form_submit_button(
            "Add Student"
        )

        if submit:

            if not student_id or not name or not email:

                st.error(
                    "Student ID, Name and Email are required."
                )

            elif students.find_one(
                {"studentId": student_id}
            ):

                st.error(
                    "Student ID already exists."
                )

            else:

                students.insert_one({

                    "studentId": student_id,
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "department": department,
                    "year": year,
                    "roomNumber": room_number

                })

                st.success(
                    "Student added successfully! 🎉"
                )

                st.rerun()

    st.divider()

    # -----------------------------
    # DELETE STUDENT
    # -----------------------------

    st.subheader("🗑️ Delete Student")

    delete_id = st.text_input(
        "Enter Student ID to delete"
    )

    if st.button("Delete Student"):

        result = students.delete_one(
            {
                "studentId": delete_id
            }
        )

        if result.deleted_count > 0:

            st.success(
                "Student deleted successfully."
            )

            st.rerun()

        else:

            st.error(
                "Student not found."
            )
            # -----------------------------
# UPDATE STUDENT
# -----------------------------

st.divider()

st.subheader("✏️ Update Student")

update_id = st.text_input(
    "Enter Student ID to update"
)

if st.button("Find Student"):

    student = students.find_one(
        {"studentId": update_id},
        {"_id": 0}
    )

    if student:

        st.session_state["student_to_update"] = student
        st.success("Student found!")

    else:

        st.error("Student not found.")


if "student_to_update" in st.session_state:

    student = st.session_state["student_to_update"]

    with st.form("update_student_form"):

        name = st.text_input(
            "Name",
            value=student.get("name", "")
        )

        email = st.text_input(
            "Email",
            value=student.get("email", "")
        )

        phone = st.text_input(
            "Phone",
            value=student.get("phone", "")
        )

        department = st.selectbox(
            "Department",
            ["CSE", "ECE", "IT", "CE", "ME"],
            index=["CSE", "ECE", "IT", "CE", "ME"].index(
                student.get("department", "CSE")
            )
        )

        year = st.selectbox(
            "Year",
            [1, 2, 3, 4],
            index=[1, 2, 3, 4].index(
                student.get("year", 1)
            )
        )

        room_number = st.text_input(
            "Room Number",
            value=student.get("roomNumber", "")
        )

        update_button = st.form_submit_button(
            "Update Student"
        )

        if update_button:

            students.update_one(
                {"studentId": update_id},
                {
                    "$set": {
                        "name": name,
                        "email": email,
                        "phone": phone,
                        "department": department,
                        "year": year,
                        "roomNumber": room_number
                    }
                }
            )

            st.success(
                "Student updated successfully! ✅"
            )

            del st.session_state["student_to_update"]

            st.rerun()
# --------------------------------------------------
# ROOMS
# --------------------------------------------------
# --------------------------------------------------
# ROOMS
# --------------------------------------------------

elif page == "🛏️ Rooms":

    st.title("🛏️ Room Management")
    st.write("View hostel rooms, occupancy and availability.")

    # Get all rooms
    room_data = list(
        rooms.find(
            {},
            {"_id": 0}
        )
    )

    # ------------------------------------------
    # CALCULATE ROOM STATISTICS
    # ------------------------------------------

    total_rooms = len(room_data)

    total_capacity = sum(
        room.get("capacity", 0)
        for room in room_data
    )

    total_occupied = sum(
        room.get("occupied", 0)
        for room in room_data
    )

    available_beds = total_capacity - total_occupied

    # ------------------------------------------
    # DISPLAY STATISTICS
    # ------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🛏️ Total Rooms",
            total_rooms
        )

    with col2:
        st.metric(
            "👥 Capacity",
            total_capacity
        )

    with col3:
        st.metric(
            "🔴 Occupied",
            total_occupied
        )

    with col4:
        st.metric(
            "🟢 Available Beds",
            available_beds
        )

    st.divider()

    # ------------------------------------------
    # FILTER
    # ------------------------------------------

    st.subheader("🔍 Filter Rooms")

    col1, col2 = st.columns(2)

    with col1:

        block_filter = st.selectbox(
            "Block",
            ["All", "A", "B", "C"]
        )

    with col2:

        room_type_filter = st.selectbox(
            "Room Type",
            ["All", "Double", "Triple"]
        )

    query = {}

    if block_filter != "All":
        query["block"] = block_filter

    if room_type_filter != "All":
        query["roomType"] = room_type_filter

    filtered_rooms = list(
        rooms.find(
            query,
            {"_id": 0}
        )
    )

    # ------------------------------------------
    # ROOM TABLE
    # ------------------------------------------

    st.subheader("🏠 Room Details")

    st.dataframe(
        filtered_rooms,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ------------------------------------------
    # AVAILABLE ROOMS
    # ------------------------------------------

    st.subheader("🟢 Available Rooms")

    available_rooms = list(
        rooms.find(
            {
                "$expr": {
                    "$lt": [
                        "$occupied",
                        "$capacity"
                    ]
                }
            },
            {"_id": 0}
        )
    )

    if available_rooms:

        st.dataframe(
            available_rooms,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.warning(
            "No rooms currently have available beds."
        )

# --------------------------------------------------
# STAFF
# --------------------------------------------------

elif page == "🛠️ Maintenance Staff":

    st.title("🛠️ Maintenance Staff")
    st.write("Manage hostel maintenance staff and their assignments.")

    # =========================
    # GET STAFF DATA
    # =========================

    staff_list = list(
        maintenance_staff.find({}, {"_id": 0})
    )

    total_staff = len(staff_list)
    available_staff = maintenance_staff.count_documents(
        {"available": True}
    )
    unavailable_staff = maintenance_staff.count_documents(
        {"available": False}
    )

    # =========================
    # METRICS
    # =========================

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Staff", total_staff)
    col2.metric("Available", available_staff)
    col3.metric("Unavailable", unavailable_staff)

    st.divider()

    # =========================
    # ADD STAFF
    # =========================

    st.subheader("➕ Add Maintenance Staff")

    with st.form("add_staff_form"):

        col1, col2 = st.columns(2)

        with col1:
            staff_id = st.text_input("Staff ID")
            staff_name = st.text_input("Name")
            specialization = st.selectbox(
                "Specialization",
                [
                    "Electrical",
                    "Plumbing",
                    "Cleaning",
                    "Furniture",
                    "Internet"
                ]
            )

        with col2:
            phone = st.text_input("Phone")
            available = st.selectbox(
                "Availability",
                ["Available", "Unavailable"]
            )

        add_staff = st.form_submit_button("Add Staff")

        if add_staff:

            if not staff_id or not staff_name or not phone:
                st.warning("Please fill all required fields.")

            elif maintenance_staff.find_one(
                {"staffId": staff_id}
            ):
                st.error("Staff ID already exists.")

            else:

                new_staff = {
                    "staffId": staff_id,
                    "name": staff_name,
                    "specialization": specialization,
                    "phone": phone,
                    "available": available == "Available"
                }

                maintenance_staff.insert_one(new_staff)

                st.success(
                    f"Staff {staff_id} added successfully!"
                )

                st.rerun()

    st.divider()

    # =========================
    # STAFF LIST
    # =========================

    st.subheader("👥 Staff List")

    staff_display = list(
        maintenance_staff.find(
            {},
            {"_id": 0}
        )
    )

    if staff_display:
        st.dataframe(
            staff_display,
            use_container_width=True
        )
    else:
        st.info("No maintenance staff found.")

    st.divider()

    # =========================
    # UPDATE AVAILABILITY
    # =========================

    st.subheader("✏️ Update Staff Availability")

    staff_ids = [
        staff["staffId"]
        for staff in staff_display
    ]

    if staff_ids:

        selected_staff = st.selectbox(
            "Select Staff",
            staff_ids
        )

        new_availability = st.selectbox(
            "New Availability",
            ["Available", "Unavailable"]
        )

        if st.button("Update Availability"):

            maintenance_staff.update_one(
                {"staffId": selected_staff},
                {
                    "$set": {
                        "available":
                            new_availability == "Available"
                    }
                }
            )

            st.success("Staff availability updated!")

            st.rerun()

    st.divider()

    # =========================
    # DELETE STAFF
    # =========================

    st.subheader("🗑️ Delete Staff")

    delete_staff_id = st.selectbox(
        "Select Staff to Delete",
        staff_ids,
        key="delete_staff"
    )

    if st.button("Delete Staff"):

        maintenance_staff.delete_one(
            {"staffId": delete_staff_id}
        )

        st.success(
            f"Staff {delete_staff_id} deleted successfully!"
        )

        st.rerun()

    st.divider()

    # =========================
    # STAFF WORKLOAD
    # =========================

    st.subheader("📊 Staff Workload")

    workload_pipeline = [
        {
            "$group": {
                "_id": "$assignedTo",
                "complaintCount": {
                    "$sum": 1
                }
            }
        },
        {
            "$sort": {
                "complaintCount": -1
            }
        }
    ]

    workload = list(
        complaints.aggregate(workload_pipeline)
    )

    if workload:

        workload_display = []

        for item in workload:

            staff = maintenance_staff.find_one(
                {"staffId": item["_id"]},
                {"_id": 0, "name": 1}
            )

            staff_name = (
                staff["name"]
                if staff
                else "Unassigned"
            )

            workload_display.append(
                {
                    "Staff ID": item["_id"],
                    "Staff Name": staff_name,
                    "Assigned Complaints":
                        item["complaintCount"]
                }
            )

        st.dataframe(
            workload_display,
            use_container_width=True
        )

        st.bar_chart(
            {
                item["Staff Name"]:
                    item["Assigned Complaints"]
                for item in workload_display
            }
        )

# --------------------------------------------------
# COMPLAINTS
# --------------------------------------------------

# --------------------------------------------------
# COMPLAINTS
# --------------------------------------------------

elif page == "📋 Complaints":

    st.title("📋 Complaint Management")
    st.write("Manage hostel complaints and maintenance requests.")

    # ==========================================
    # FILTERS
    # ==========================================

    st.subheader("🔍 Filter Complaints")

    col1, col2, col3 = st.columns(3)

    with col1:
        status_filter = st.selectbox(
            "Status",
            ["All", "Pending", "In Progress", "Resolved"]
        )

    with col2:
        priority_filter = st.selectbox(
            "Priority",
            ["All", "Low", "Medium", "High"]
        )

    with col3:
        category_filter = st.selectbox(
            "Category",
            [
                "All",
                "Electrical",
                "Plumbing",
                "Cleaning",
                "Furniture",
                "Internet"
            ]
        )

    # ==========================================
    # BUILD FILTER
    # ==========================================

    query = {}

    if status_filter != "All":
        query["status"] = status_filter

    if priority_filter != "All":
        query["priority"] = priority_filter

    if category_filter != "All":
        query["category"] = category_filter

    complaint_data = list(
        complaints.find(
            query,
            {"_id": 0}
        )
    )

    st.metric(
        "Complaints Found",
        len(complaint_data)
    )

    # ==========================================
    # DISPLAY COMPLAINTS
    # ==========================================

    if complaint_data:

        st.dataframe(
            complaint_data,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info("No complaints found for the selected filters.")

    st.divider()

    # ==========================================
    # ADD COMPLAINT
    # ==========================================

    st.subheader("➕ Create New Complaint")

    student_list = list(
        students.find(
            {},
            {
                "_id": 0,
                "studentId": 1,
                "name": 1,
                "roomNumber": 1
            }
        )
    )

    staff_list = list(
        maintenance_staff.find(
            {},
            {
                "_id": 0,
                "staffId": 1,
                "name": 1
            }
        )
    )

    if student_list and staff_list:

        with st.form("complaint_form"):

            col1, col2 = st.columns(2)

            with col1:

                student_options = {
                    f"{s['studentId']} - {s['name']}": s
                    for s in student_list
                }

                selected_student = st.selectbox(
                    "Student",
                    list(student_options.keys())
                )

                category = st.selectbox(
                    "Category",
                    [
                        "Electrical",
                        "Plumbing",
                        "Cleaning",
                        "Furniture",
                        "Internet"
                    ]
                )

                priority = st.selectbox(
                    "Priority",
                    ["Low", "Medium", "High"]
                )

            with col2:

                staff_options = {
                    f"{s['staffId']} - {s['name']}": s
                    for s in staff_list
                }

                selected_staff = st.selectbox(
                    "Assign Staff",
                    list(staff_options.keys())
                )

                description = st.text_area(
                    "Description"
                )

            submit_complaint = st.form_submit_button(
                "Create Complaint"
            )

            if submit_complaint:

                student = student_options[selected_student]
                staff = staff_options[selected_staff]

                last_complaint = complaints.find_one(
                    {},
                    sort=[("complaintId", -1)]
                )

                if last_complaint:
                    last_id = int(last_complaint["complaintId"][1:])
                    complaint_id = f"C{last_id + 1:03d}"
                else:
                    complaint_id = "C001"

                new_complaint = {

                    "complaintId": complaint_id,
                    "studentId": selected_student,
                    "roomNumber": student_room,
                    "category": category,
                    "description": description,
                    "priority": priority,
                    "status": "Pending",
                    "assignedTo": assigned_staff,
                    "createdAt": datetime.now(),
                    "resolvedAt": None
                }
                complaints.insert_one(new_complaint)

                st.success(f"Complaint {complaint_id} created successfully!")
                st.rerun()

            

    st.divider()

    # ==========================================
    # UPDATE COMPLAINT STATUS
    # ==========================================

    st.subheader("✏️ Update Complaint Status")

    complaint_id = st.text_input(
        "Complaint ID",
        placeholder="Example: C001"
    )

    new_status = st.selectbox(
        "New Status",
        ["Pending", "In Progress", "Resolved"]
    )

    if st.button("Update Status"):

        if new_status == "Resolved":

            complaints.update_one(
                {"complaintId": complaint_id},
                {
                    "$set": {
                        "status": new_status,
                        "resolvedAt": datetime.now()
                    }
                }
            )

        else:

            complaints.update_one(
                {"complaintId": complaint_id},
                {
                    "$set": {
                        "status": new_status
                    }
                }
            )

        st.success("Complaint status updated!")
        st.rerun()
    

        result = complaints.update_one(
            {"complaintId": complaint_id},
            {
                "$set": {
                    "status": new_status
                }
            }
        )

        if result.modified_count > 0:

            st.success(
                "Complaint status updated successfully! ✅"
            )

            st.rerun()

        elif result.matched_count > 0:

            st.info(
                "Complaint already has this status."
            )

        else:

            st.error(
                "Complaint not found."
            )

    st.divider()

    # ==========================================
    # DELETE COMPLAINT
    # ==========================================

    st.subheader("🗑️ Delete Complaint")

    delete_complaint_id = st.text_input(
        "Enter Complaint ID to delete",
        placeholder="Example: C001"
    )

    if st.button("Delete Complaint"):

        result = complaints.delete_one(
            {
                "complaintId": delete_complaint_id
            }
        )

        if result.deleted_count > 0:

            st.success(
                "Complaint deleted successfully."
            )

            st.rerun()

        else:

            st.error(
                "Complaint not found."
            )
# --------------------------------------------------
# ANALYTICS
# --------------------------------------------------
elif page == "📈 Analytics":

    st.title("📈 Analytics")
    st.write("Hostel and complaint analytics")

    # =========================
    # COMPLAINT STATISTICS
    # =========================

    total_complaints = complaints.count_documents({})

    pending = complaints.count_documents({"status": "Pending"})
    in_progress = complaints.count_documents({"status": "In Progress"})
    resolved = complaints.count_documents({"status": "Resolved"})

    high_priority = complaints.count_documents({"priority": "High"})
    medium_priority = complaints.count_documents({"priority": "Medium"})
    low_priority = complaints.count_documents({"priority": "Low"})

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Complaints", total_complaints)
    col2.metric("Pending", pending)
    col3.metric("In Progress", in_progress)
    col4.metric("Resolved", resolved)

    st.divider()

    # =========================
    # COMPLAINTS BY STATUS
    # =========================

    st.subheader("📊 Complaints by Status")

    status_pipeline = [
        {
            "$group": {
                "_id": "$status",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {
                "count": -1
            }
        }
    ]

    status_data = list(complaints.aggregate(status_pipeline))

    status_chart = {
        item["_id"]: item["count"]
        for item in status_data
    }

    st.bar_chart(status_chart)

    st.divider()

    # =========================
    # COMPLAINTS BY CATEGORY
    # =========================

    st.subheader("📂 Complaints by Category")

    category_pipeline = [
        {
            "$group": {
                "_id": "$category",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {
                "count": -1
            }
        }
    ]

    category_data = list(complaints.aggregate(category_pipeline))

    category_chart = {
        item["_id"]: item["count"]
        for item in category_data
    }

    st.bar_chart(category_chart)

    st.divider()

    # =========================
    # COMPLAINTS BY PRIORITY
    # =========================

    st.subheader("⚠️ Complaints by Priority")

    priority_pipeline = [
        {
            "$group": {
                "_id": "$priority",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {
                "count": -1
            }
        }
    ]

    priority_data = list(complaints.aggregate(priority_pipeline))

    priority_chart = {
        item["_id"]: item["count"]
        for item in priority_data
    }

    st.bar_chart(priority_chart)

    st.divider()

    # =========================
    # STAFF WORKLOAD
    # =========================

    st.subheader("🛠️ Maintenance Staff Workload")

    staff_pipeline = [
        {
            "$match": {
                "assignedTo": {
                    "$ne": None
                }
            }
        },
        {
            "$group": {
                "_id": "$assignedTo",
                "complaints": {"$sum": 1}
            }
        },
        {
            "$sort": {
                "complaints": -1
            }
        }
    ]

    staff_data = list(complaints.aggregate(staff_pipeline))

    staff_chart = {
        item["_id"]: item["complaints"]
        for item in staff_data
    }

    st.bar_chart(staff_chart)

    st.divider()

    # =========================
    # ROOM OCCUPANCY
    # =========================

    st.subheader("🛏️ Room Occupancy")

    rooms_data = list(
        rooms.find(
            {},
            {
                "_id": 0,
                "roomNumber": 1,
                "capacity": 1,
                "occupied": 1
            }
        )
    )

    occupancy_data = {}

    for room in rooms_data:
        occupancy_data[room["roomNumber"]] = {
            "Occupied": room["occupied"],
            "Available": room["capacity"] - room["occupied"]
        }

    st.dataframe(
        occupancy_data,
        use_container_width=True
    )