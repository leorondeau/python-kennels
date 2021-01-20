import sqlite3
import json
from models import Employee


EMPLOYEES = [
    {
        "name": "Hector",
        "locationId": 2,
        "animalId": 3,
        "id": 6
    },
    {
        "name": "Jeff",
        "locationId": 1,
        "animalId": 5,
        "id": 7
    },
    {
        "name": "Rick Eddy",
        "locationId": 1,
        "animalId": 2,
        "id": 8
    }
]

def get_all_employees():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,                        
            a.location_id
            
        FROM employee a
        """)

        
        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            employee = Employee(row['id'], row['name'],
                            row['address'], row['location_id']
                            )

            employees.append(employee.__dict__)

        return json.dumps(employees)

def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
            a.location_id

        FROM employee a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an employee instance from the current row
        employee = Employee(data['id'], data['name'], data['address'],
                            data['location_id'])

        return json.dumps(employee.__dict__)


def create_employee(employee):

    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1

    employee["id"] = new_id
    
    EMPLOYEES.append(employee)

    return employee

def delete_employee(id):
    
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            
            employee_index = index

    
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    # Iterate the EMPLOYEES list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Update the value.
            EMPLOYEES[index] = new_employee
            break