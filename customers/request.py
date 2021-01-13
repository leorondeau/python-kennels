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
    