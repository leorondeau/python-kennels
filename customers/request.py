import sqlite3
import json
from models import Customer



CUSTOMERS = [
    {
        "email": "leon@kennels.com",
        "password": "goodboys",
        "name": "leon Dean",
        "id": 1
    },
    {
        "email": "jon@kennels.com",
        "password": "goodboys",
        "name": "jon johns",
        "id": 2
    },
    {
        "email": "jim@kennels.com",
        "password": "goodboys",
        "name": "james howell",
        "id": 3
    }
]

def get_all_customers():
    
    with sqlite3.connect("./kennel.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id, 
            a.name,
            a.email,
            a.password
        FROM customer a
        """)

        customers = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            customer = Customer(row['id'], row['name'], row['email'],
                                row['password'])

            customers.append(customer.__dict__)

        return json.dumps(customers)

def get_single_customer():
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.email,
            a.password
        FROM customer a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        customer = Customer(data['id'], data['name'], data['email'],
                            data['password'])
        return json.dumps(customer.__dict__)

        
def create_customer(customer):

    max_id = CUSTOMERS[-1]["id"]

    new_id = max_id + 1

    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer


def delete_customer(id):
    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the customerS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)


def update_customer(id, new_customer):
   
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            
            CUSTOMERS[index] = new_customer
            break