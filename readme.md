# HostelHub

HostelHub is a MongoDB-based hostel management system built with Python and
PyMongo. It is designed to organize student records, hostel rooms, maintenance
staff, and complaints in one database.

## Main objectives

- Store and manage student and hostel records.
- Allocate rooms and track occupancy.
- Register and track maintenance complaints.
- Search and filter records efficiently.
- Generate reports with MongoDB aggregation pipelines.
- Improve query performance with indexes.

## Requirements

- Python 3.9+
- MongoDB running locally on `mongodb://localhost:27017/`
- PyMongo

Install the Python dependency:

```bash
pip install pymongo
```

## Run

Start MongoDB, then run the connection check:

```bash
python database.py
```

The application uses the `HostelHub` database. Update the MongoDB URI in
`database.py` if MongoDB is hosted elsewhere.

## Project files

- `database.py` - Connects to MongoDB and checks the database connection.
- `crud.py` - CRUD operations for hostel records.
- `queries.py` - Search and filtering queries.
- `aggregation.py` - Reporting and aggregation pipelines.
- `indexing.py` - Database index definitions.
- `main.py` - Application entry point.