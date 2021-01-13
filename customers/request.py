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
    return CUSTOMERS

def get_single_customer():
    
    requested_customer = None

    for customer in CUSTOMERS:

        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):

    max_id = CUSTOMERS[-1]["id"]

    new_id = max_id + 1

    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer
    