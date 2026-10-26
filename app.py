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
:root {
    --bg: #f4f7f6;
    --bg-glow: rgba(20, 184, 166, 0.10);
    --surface: #ffffff;
    --border: #e2e8e6;
    --text: #12302d;
    --muted: #5b706d;
    --primary: #0d9488;
    --primary-strong: #0f766e;
    --accent: #f59e0b;
    --pill-bg: #ccfbf1;
    --pill-text: #115e59;
    --input-bg: #ffffff;
    --shadow: 0 8px 24px rgba(18, 48, 45, 0.06);
    --hero: linear-gradient(115deg, #134e4a 0%, #0f766e 55%, #0d9488 100%);
}

.stApp {
    background: var(--bg);
    color: var(--text);
}

[data-testid="stAppViewContainer"] > .main {
    background:
        radial-gradient(circle at 88% 0%, var(--bg-glow), transparent 28rem),
        var(--bg);
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1500px;
    padding: 2.5rem 3rem 4rem;
}

/* ---------- Sidebar ---------- */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b1f1e 0%, #134e4a 100%);
    border-right: 1px solid rgba(255, 255, 255, 0.08);
}

section[data-testid="stSidebar"] * {
    color: #e6f4f1;
}

section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1 {
    color: #ffffff !important;
    letter-spacing: -0.04em;
}

section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #99f6e4;
}

section[data-testid="stSidebar"] .stRadio > label {
    color: #99f6e4;
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 0.12em;
    text-transform: uppercase;
}

section[data-testid="stSidebar"] .stRadio > div {
    gap: 0.35rem;
}

section[data-testid="stSidebar"] .stRadio label[data-baseweb="radio"] {
    background: rgba(255, 255, 255, 0.04);
    border-radius: 10px;
    padding: 0.45rem 0.7rem;
    transition: background 0.2s ease;
}

section[data-testid="stSidebar"] .stRadio label[data-baseweb="radio"]:hover {
    background: rgba(255, 255, 255, 0.12);
}

section[data-testid="stSidebar"] [data-testid="stWidgetLabel"] {
    color: #99f6e4;
}

section[data-testid="stSidebar"] [data-testid="stToggle"] {
    padding: 0.7rem 0.8rem;
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 12px;
    background: rgba(255, 255, 255, 0.05);
}

/* ---------- Typography ---------- */
h1, h2, h3,
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3,
[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3 {
    color: var(--text) !important;
    letter-spacing: -0.035em;
}

h1 {
    font-size: 2.35rem !important;
    font-weight: 800 !important;
}

h2, h3 {
    font-weight: 750 !important;
}

/* ---------- Hero / headers ---------- */
.hero {
    background: var(--hero);
    border-radius: 24px;
    padding: 2rem 2.25rem;
    margin: 0.2rem 0 1.8rem;
    color: #ffffff;
    box-shadow: 0 20px 45px rgba(15, 118, 110, 0.25);
    position: relative;
    overflow: hidden;
}

.hero:after {
    content: "";
    width: 260px;
    height: 260px;
    border: 1px solid rgba(255, 255, 255, 0.16);
    border-radius: 50%;
    position: absolute;
    right: -70px;
    top: -100px;
    pointer-events: none;
}

.hero h1 {
    color: #ffffff !important;
    font-size: 2.4rem !important;
    margin: 0 0 0.35rem;
}

.hero p {
    color: rgba(255, 255, 255, 0.85);
    margin: 0;
    font-size: 1.02rem;
}

.eyebrow {
    color: #fde68a;
    font-size: 0.75rem;
    font-weight: 800;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 0.55rem;
}

.page-header {
    background: var(--hero);
    border-radius: 20px;
    padding: 1.45rem 1.7rem;
    margin: 0.1rem 0 1.6rem;
    color: #ffffff;
    box-shadow: 0 14px 34px rgba(15, 118, 110, 0.2);
}

.page-header .eyebrow {
    margin-bottom: 0.35rem;
}

.page-header h1 {
    color: #ffffff !important;
    font-size: 1.85rem !important;
    margin: 0 0 0.25rem;
}

.page-header p {
    color: rgba(255, 255, 255, 0.85);
    margin: 0;
}

/* ---------- Cards ---------- */
div[data-testid="metric-container"],
div[data-testid="stMetric"] {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.1rem 1.2rem;
    min-height: 112px;
    box-shadow: var(--shadow);
}

div[data-testid="stMetricLabel"], div[data-testid="stMetricLabel"] * {
    color: var(--muted) !important;
    font-size: 0.82rem;
    font-weight: 700;
}

div[data-testid="stMetricValue"], div[data-testid="stMetricValue"] * {
    color: var(--text) !important;
    font-size: 1.85rem;
    font-weight: 800;
}

div[data-testid="stMetricDelta"] {
    font-size: 0.78rem;
}

.section-label {
    color: var(--muted);
    font-size: 0.75rem;
    font-weight: 800;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin: 1.8rem 0 0.75rem;
}

.panel {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 1.35rem 1.45rem;
    box-shadow: var(--shadow);
}

.panel-title {
    color: var(--text);
    font-size: 1.05rem;
    font-weight: 750;
    margin-bottom: 0.85rem;
}

.panel-muted { color: var(--muted); font-size: 0.88rem; }
.panel-strong { color: var(--text); font-size: 1.7rem; }

.page-section {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 1.25rem 1.4rem;
    margin: 1.1rem 0;
    box-shadow: var(--shadow);
}

.status-pill {
    display: inline-block;
    border-radius: 999px;
    padding: 0.28rem 0.65rem;
    font-size: 0.75rem;
    font-weight: 750;
    background: var(--pill-bg);
    color: var(--pill-text);
}

/* ---------- Widgets ---------- */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, var(--primary), var(--accent));
}

.stButton > button,
.stFormSubmitButton > button {
    border-radius: 10px;
    border: 1px solid var(--border);
    background: var(--surface);
    color: var(--text);
    font-weight: 700;
    min-height: 2.6rem;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    border-color: var(--primary);
    color: var(--primary-strong);
}

.stButton > button[kind="primary"],
.stFormSubmitButton > button[kind="primary"] {
    background: var(--primary);
    border-color: var(--primary);
    color: #ffffff;
}

.stButton > button[kind="primary"]:hover,
.stFormSubmitButton > button[kind="primary"]:hover {
    background: var(--primary-strong);
    color: #ffffff;
}

input, textarea, [data-baseweb="select"] > div {
    background-color: var(--input-bg) !important;
    color: var(--text) !important;
    border-color: var(--border) !important;
}

input:focus, textarea:focus {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 1px var(--primary) !important;
}

div[data-testid="stDataFrame"] {
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
}

hr {
    border-color: var(--border);
    margin: 1.8rem 0;
}

/* ---------- Responsive ---------- */
@media (max-width: 1100px) {
    .block-container { padding: 2rem 1.5rem 3rem; }
    h1 { font-size: 2rem !important; }
    .hero h1 { font-size: 2rem !important; }
}

@media (max-width: 768px) {
    .block-container { padding: 1.25rem 1rem 2.5rem; }
    h1 { font-size: 1.6rem !important; }

    /* stack Streamlit columns */
    div[data-testid="stHorizontalBlock"] {
        flex-wrap: wrap !important;
        gap: 0.75rem !important;
    }
    div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"],
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {
        flex: 1 1 100% !important;
        min-width: 100% !important;
        width: 100% !important;
    }

    .hero, .page-header {
        padding: 1.1rem 1.2rem;
        border-radius: 16px;
        margin-bottom: 1.1rem;
    }
    .hero h1 { font-size: 1.6rem !important; }
    .page-header h1 { font-size: 1.35rem !important; }
    .hero:after { display: none; }

    .panel, .page-section { padding: 1rem; border-radius: 14px; }
    .panel-strong { font-size: 1.35rem; }
    div[data-testid="metric-container"],
    div[data-testid="stMetric"] { min-height: 0; padding: 0.85rem 1rem; }
    div[data-testid="stMetricValue"], div[data-testid="stMetricValue"] * { font-size: 1.5rem; }

    .stButton > button, .stFormSubmitButton > button { width: 100%; }
}

@media (max-width: 480px) {
    .block-container { padding: 1rem 0.75rem 2rem; }
    .hero p, .page-header p { font-size: 0.9rem; }
}
</style>
""", unsafe_allow_html=True)


def render_page_header(eyebrow, title, subtitle):
    st.markdown(
        f"""
        <div class="page-header">
            <div class="eyebrow">{eyebrow}</div>
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


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

    dark_mode = st.toggle(
        "🌙 Dark mode",
        value=st.session_state.get("dark_mode", False),
        key="dark_mode"
    )

    st.markdown(
        """
        <div style="margin-top:1.4rem;padding:0.9rem 1rem;border:1px solid rgba(255,255,255,.12);
        border-radius:14px;background:rgba(255,255,255,.06);">
            <div style="font-weight:750;color:#fff;">HostelHub Admin</div>
            <div style="font-size:.76rem;color:#99f6e4;margin-top:.25rem;">
                MongoDB · PyMongo · Streamlit
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


if dark_mode:
    st.markdown(
        """
        <style>
        :root {
            --bg: #0b1514;
            --bg-glow: rgba(20, 184, 166, 0.14);
            --surface: #12201f;
            --border: #24403d;
            --text: #e6f4f1;
            --muted: #9db8b4;
            --primary: #2dd4bf;
            --primary-strong: #5eead4;
            --pill-bg: #134e4a;
            --pill-text: #99f6e4;
            --input-bg: #0f1b1a;
            --shadow: 0 10px 28px rgba(0, 0, 0, 0.3);
        }
        .stApp p, .stApp label, .stApp span, [data-testid="stText"] {
            color: var(--text);
        }
        section[data-testid="stSidebar"] * { color: #e6f4f1; }
        [data-testid="stDataFrame"] * { color: var(--text) !important; }
        .stButton > button[kind="primary"],
        .stFormSubmitButton > button[kind="primary"] {
            color: #04201d;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

if page == "📊 Dashboard":
    # =========================
    # DASHBOARD DATA
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

    st.markdown(
        f"""
        <div class="hero">
            <div class="eyebrow">HostelHub / Operations overview</div>
            <h1>Good evening, Admin 👋</h1>
            <p>Here is what is happening across your hostel today.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="section-label">At a glance</div>', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("👨‍🎓 Students", f"{total_students:,}", "Active residents")
    col2.metric("🛏️ Rooms", f"{total_rooms:,}", f"{available_beds} beds available")
    col3.metric("🛠️ Staff", f"{total_staff:,}", "Maintenance team")
    col4.metric("📋 Complaints", f"{total_complaints:,}", f"{pending_complaints} need attention")

    st.markdown('<div class="section-label">Operations pulse</div>', unsafe_allow_html=True)
    status_col, occupancy_col = st.columns([1, 1], gap="large")

    with status_col:
        st.markdown(
            f"""
            <div class="panel">
                <div class="panel-title">Complaint status</div>
                <span class="status-pill">Live queue</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        status_a, status_b, status_c = st.columns(3)
        status_a.metric("Pending", pending_complaints)
        status_b.metric("In progress", in_progress)
        status_c.metric("Resolved", resolved_complaints)

    with occupancy_col:
        st.markdown(
            f"""
            <div class="panel">
                <div class="panel-title">Room occupancy</div>
                <div style="display:flex;justify-content:space-between;align-items:end;margin-bottom:0.6rem;">
                    <span class="panel-muted">Current utilization</span>
                    <strong class="panel-strong">{occupancy_percentage:.1f}%</strong>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.progress(min(occupancy_percentage / 100, 1.0))
        occupancy_a, occupancy_b, occupancy_c = st.columns(3)
        occupancy_a.metric("Capacity", total_capacity)
        occupancy_b.metric("Occupied", total_occupied)
        occupancy_c.metric("Available", available_beds)

    st.markdown('<div class="section-label">Latest activity</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="panel"><div class="panel-title">🕒 Recent complaints</div>',
        unsafe_allow_html=True
    )

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
            use_container_width=True,
            hide_index=True,
            column_config={
                "complaintId": "ID",
                "studentId": "Student",
                "category": "Category",
                "priority": "Priority",
                "status": "Status",
                "createdAt": st.column_config.DatetimeColumn(
                    "Created",
                    format="MMM D, YYYY"
                )
            }
        )
    else:
        st.info("No complaints found.")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="section-label">Quick insights</div>', unsafe_allow_html=True)
    insight_col1, insight_col2 = st.columns(2, gap="large")
    with insight_col1:
        st.markdown('<div class="panel"><div class="panel-title">📋 Complaint mix</div>', unsafe_allow_html=True)
        st.bar_chart(
            {
                "Pending": pending_complaints,
                "In Progress": in_progress,
                "Resolved": resolved_complaints
            },
            color="#0d9488"
        )
        st.markdown("</div>", unsafe_allow_html=True)
    with insight_col2:
        st.markdown('<div class="panel"><div class="panel-title">🛏️ Bed utilization</div>', unsafe_allow_html=True)
        st.bar_chart(
            {
                "Occupied": total_occupied,
                "Available": available_beds
            },
            color="#f59e0b"
        )
        st.markdown("</div>", unsafe_allow_html=True)


# --------------------------------------------------
# STUDENTS
# --------------------------------------------------

# --------------------------------------------------
# STUDENTS
# --------------------------------------------------

elif page == "👨‍🎓 Students":

    render_page_header(
        "HostelHub / Residents",
        "👨‍🎓 Student Management",
        "Search residents, review room assignments, and keep student records up to date."
    )

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

    st.markdown('<div class="page-section">', unsafe_allow_html=True)
    st.metric(
        "Total Students",
        students.count_documents({})
    )

    st.dataframe(
        student_data,
        use_container_width=True,
        hide_index=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

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

    render_page_header(
        "HostelHub / Accommodation",
        "🛏️ Room Management",
        "Monitor capacity, occupancy, and available beds across every hostel block."
    )

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

    render_page_header(
        "HostelHub / Operations team",
        "🛠️ Maintenance Staff",
        "Manage staff availability, assignments, and workload at a glance."
    )

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

    render_page_header(
        "HostelHub / Service desk",
        "📋 Complaint Management",
        "Track maintenance requests from first report through resolution."
    )

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

    render_page_header(
        "HostelHub / Insights",
        "📈 Analytics",
        "Understand complaint trends, staff workload, and room utilization."
    )

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