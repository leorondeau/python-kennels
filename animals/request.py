import sqlite3
import json
from models import Animal
from models import Location
from models import Customer

# ANIMALS = [
#     {
#         "id": 1,
#         "name": "Snickers",
#         "species": "Dog",
#         "locationId": 1,
#         "customerId": 4,
#         "status": "Admitted"
#     },
#     {
#         "id": 2,
#         "name": "Gypsy",
#         "species": "Dog",
#         "locationId": 1,
#         "customerId": 2,
#         "status": "Admitted"
#     },
#     {
#         "id": 3,
#         "name": "Blue",
#         "species": "Cat",
#         "locationId": 2,
#         "customerId": 1,
#         "status": "Admitted"
#     }
# ]


def get_all_animals():
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
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.id loc_id,
            l.name location_name ,
            l.address location_address,
            c.id cus_id,
            c.name customer_name,
            c.address customer_address,
            c.email customer_email

        FROM animal a
        JOIN location l
            ON l.id = a.location_id
        JOIN customer c
            ON c.id = a.customer_id
        """)

        # Initialize an empty list to hold all animal representations
        animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row
            animal = Animal(row['id'], row['name'], row['breed'], row['status'],
                            row['location_id'], row['customer_id'])

            # Create a Location instance from the current row
            location = Location(row['loc_id'], row['location_name'], row['location_address'])

            animal.location = location.__dict__

            customer = Customer(row['cus_id'], row['customer_name'], row['customer_address'], 
                        row['customer_email'])

            animal.customer = customer.__dict__
            # Add the dictionary representation of the location to the animal

            # Add the dictionary representation of the animal to the list
            animals.append(animal.__dict__)

    # Use `json` package to properly serialize list as JSON
        return json.dumps(animals)


def get_single_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the "SQL statement" or "query".
        db_cursor.execute("""
        SELECT
            a.id,
            a.name animal_name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.id loc_id,
            l.name location_name,
            c.id cus_id,
            c.name customer_name,
            c.address
            
        FROM animal a
        JOIN location l
            ON l.id = a.location_id
        JOIN customer c
            ON c.id = a.customer_id
        WHERE a.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        
        animal = Animal(data['id'], data['animal_name'], data['breed'],
                            data['status'], data['location_id'],
                            data['customer_id'])

        location = Location(data['loc_id'], data['location_name'])
        animal.location= location.__dict__


        customer = Customer(data['cus_id'], data['customer_name'], data['address'])
        animal.customer = customer.__dict__



        return json.dumps(animal.__dict__)


def get_animals_by_location_id(location_id):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM Animal a
        WHERE a.location_id = ?
        """, (location_id, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])
            animals.append(animal.__dict__)

        return json.dumps(animals)


def get_animals_by_status(status):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM Animal a
        WHERE a.status = ?
        """, (status, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'], row['status'], row['location_id'], row['customer_id'])

            animals.append(animal.__dict__)

        return json.dumps(animals)


def create_animal(new_animal):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Animal
            ( name, breed, status, location_id, customer_id )
        VALUES
            ( ?, ?, ?, ?, ?);   
        """, (new_animal['name'], 
            new_animal['breed'], 
            new_animal['status'],
            new_animal['locationId'],
            new_animal['customerId'], ))

        id = db_cursor.lastrowid

        new_animal['id'] = id
    
    return json.dumps(new_animal)


def delete_animal(id):

    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM animal
        WHERE id = ?
        """, (id, ))


def update_animal(id, new_animal):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Animal
            SET
                name = ?, 
                breed = ?,
                status = ?,
                location_id = ?,
                customer_id =?
        WHERE id = ?
        """, (new_animal['name'], new_animal['breed'],
            new_animal['status'], new_animal['locationId'],
            new_animal['customerId'], id,))

        rows_affected = db_cursor.rowcount

        if rows_affected == 0:
            return False
        else:
            return True
