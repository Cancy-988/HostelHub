# HostelHub

HostelHub is a Python and MongoDB hostel-management data project. It
demonstrates how to store, query, update, aggregate, and index hostel data
with PyMongo.

The project models four related areas:

- **Students** and their room assignments
- **Rooms** and current occupancy
- **Maintenance staff** and their specializations
- **Complaints** raised by students and assigned to maintenance staff

The repository contains focused Python scripts rather than a web interface or
command-line menu. Each script imports the collections defined in
`database.py` and performs one part of the database workflow.

## Features

- Connects to a local MongoDB server using PyMongo
- Creates sample records for students, rooms, maintenance staff, and
  complaints
- Demonstrates CRUD operations for student and complaint records
- Filters complaints by status, priority, category, and description
- Finds students by department and academic year
- Identifies rooms with available capacity
- Produces complaint and maintenance workload reports with aggregation
  pipelines
- Creates unique, single-field, and compound indexes for common lookups

## Technology stack

- **Python:** 3.9 or newer
- **Database:** MongoDB
- **Driver:** PyMongo
- **Data format:** MongoDB documents

No `requirements.txt` is currently included; install the single runtime
dependency directly with `pip`.

## Prerequisites

Install the following before running the scripts:

1. Python 3.9 or newer
2. MongoDB Community Server, running locally
3. `pip`

The default connection string is:

```text
mongodb://localhost:27017/
```

If MongoDB is running on another host or port, update the connection string in
`database.py` before running the scripts.

## Installation

Clone the repository and enter the project directory:

```bash
git clone <repository-url>
cd HostelHub
```

Create and activate a virtual environment:

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```bat
python -m venv .venv
.venv\Scripts\activate
```

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install PyMongo:

```bash
python -m pip install pymongo
```

## Database configuration

`database.py` creates a `MongoClient` and exposes the `HostelHub` database and
four collections:

```python
client = MongoClient("mongodb://localhost:27017/")
db = client["HostelHub"]
```

The collections are:

| Collection | Purpose |
| --- | --- |
| `students` | Student identity, academic details, and room assignment |
| `rooms` | Room block, floor, capacity, occupancy, and room type |
| `maintenance_staff` | Staff contact details, specialization, and availability |
| `complaints` | Student issues, priority, status, assignment, and timestamps |

The MongoDB database and collections are created by MongoDB when data is first
written. Importing `database.py` also prints a connection message. A MongoDB
server must be available before running scripts that read or write data.

## Recommended first run

Run the scripts in this order from the repository root:

```bash
python database.py
python seed_data.py
python indexing.py
python queries.py
python aggregation.py
python crud.py
```

### What each command does

#### 1. Check the database module

```bash
python database.py
```

Loads the MongoDB client and collection handles and prints a connection
message. This script does not insert sample records.

#### 2. Insert sample data

```bash
python seed_data.py
```

Inserts:

- 20 students
- 13 rooms
- 5 maintenance staff members
- 30 randomly generated complaints

Complaint categories, priorities, statuses, assigned staff, and dates are
generated with Python's `random` module. Re-running this script inserts the
same student, room, staff, and complaint identifiers again. Because the
unique indexes are not created until `indexing.py` is run, repeated seeding
can create duplicate records. For a clean demo database, clear the
`HostelHub` database in MongoDB before seeding again.

#### 3. Create indexes

```bash
python indexing.py
```

Creates and displays these indexes:

- Unique index on `students.studentId`
- Unique index on `complaints.complaintId`
- Index on `complaints.status`
- Index on `complaints.category`
- Compound index on `complaints.status` and `complaints.createdAt`

Run this after the first seed. If duplicate identifiers already exist, MongoDB
will reject creation of the unique indexes; remove duplicates or reset the
database first.

#### 4. Run query examples

```bash
python queries.py
```

Displays:

- Pending complaints
- High-priority complaints
- Students in the CSE department
- Third- and fourth-year students
- High-priority pending complaints
- Complaints that are not resolved
- Complaints whose description contains `issue`
- Rooms where `occupied` is less than `capacity`

#### 5. Run aggregation reports

```bash
python aggregation.py
```

Reports complaint totals grouped by:

- Category
- Status
- Assigned maintenance staff
- Category for high-priority complaints

#### 6. Run CRUD demonstrations

```bash
python crud.py
```

The script:

1. Prints all students
2. Inserts a temporary student, `ST021`
3. Changes complaint `C001` to `Resolved`
4. Deletes `ST021`

Because the operations are executed when the module runs, this file is a
demonstration script, not a reusable interactive API. Its final delete removes
the student inserted during the same run.

## Data model

### Student document

```json
{
  "studentId": "ST001",
  "name": "Aarav Sharma",
  "email": "aarav@gmail.com",
  "phone": "9876500001",
  "department": "CSE",
  "year": 3,
  "roomNumber": "A101"
}
```

### Room document

```json
{
  "roomNumber": "A101",
  "block": "A",
  "floor": 1,
  "capacity": 2,
  "occupied": 2,
  "roomType": "Double"
}
```

Rooms are considered available when `occupied < capacity`. The project uses
room numbers as references from student documents and complaint documents.

### Maintenance staff document

```json
{
  "staffId": "M001",
  "name": "Amit Kumar",
  "specialization": "Electrical",
  "phone": "9811100001",
  "available": true
}
```

### Complaint document

```json
{
  "complaintId": "C001",
  "studentId": "ST001",
  "roomNumber": "A101",
  "category": "Electrical",
  "description": "Electrical issue reported in room A101",
  "priority": "High",
  "status": "Pending",
  "assignedTo": "M001",
  "createdAt": "2024-01-01T00:00:00Z",
  "resolvedAt": null
}
```

The seed script uses Python `datetime` values for `createdAt` and
`resolvedAt`; MongoDB stores them as BSON dates. Resolved complaints receive a
calculated `resolvedAt` value, while unresolved complaints receive `None`.

## Project structure

| File | Description |
| --- | --- |
| `database.py` | Creates the MongoDB client, selects the `HostelHub` database, and exposes collection handles |
| `seed_data.py` | Inserts sample students, rooms, staff, and randomly generated complaints |
| `crud.py` | Demonstrates create, read, update, and delete operations |
| `queries.py` | Demonstrates filtering and expression-based MongoDB queries |
| `aggregation.py` | Runs grouping and sorting pipelines for reports |
| `indexing.py` | Creates and prints collection indexes |
| `.gitignore` | Defines files excluded from version control |

## Useful MongoDB commands

Open the MongoDB shell with `mongosh` and inspect the generated data:

```javascript
use HostelHub
show collections

db.students.countDocuments()
db.rooms.countDocuments()
db.maintenance_staff.countDocuments()
db.complaints.countDocuments()
```

To reset the local demo database before seeding:

```javascript
use HostelHub
db.dropDatabase()
```

After resetting, run `seed_data.py` and then `indexing.py` again.

## Troubleshooting

### `ServerSelectionTimeoutError`

MongoDB is not running, or the configured URI is incorrect. Start the MongoDB
service and confirm that `database.py` uses the correct host and port.

### `ModuleNotFoundError: No module named 'pymongo'`

Activate the virtual environment and install the dependency:

```bash
python -m pip install pymongo
```

### Duplicate key errors

The seed and CRUD scripts use fixed identifiers. Re-running them can create
duplicates, especially after unique indexes have been created. Reset the
local demo database with `db.dropDatabase()` and seed it again.

### No query or report output

The query and aggregation scripts read existing collections. Run
`seed_data.py` first, then rerun the query or report script.

## Limitations and next steps

This project is intended as a PyMongo and MongoDB practice application. It
does not currently include authentication, input validation, a web UI,
transaction handling, environment-based configuration, automated tests, or a
packaged dependency manifest.

Possible extensions include:

- Moving the MongoDB URI to an environment variable
- Adding validation for student, room, and complaint fields
- Preventing duplicate room assignments and over-capacity rooms
- Building an interactive CLI or web API
- Adding tests with a dedicated test database
- Adding update and delete operations for rooms, staff, and complaints
- Adding a reproducible seed option instead of non-deterministic complaint data

## License

No license file is currently included in this repository. Add a license before
distributing the project or accepting external contributions.
