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
    return EMPLOYEES

def get_single_employees():

    requested_employee = None

    for employee in EMPLOYEES:

        if employee["id"] == id:
            requested_employee = employee
    
    return requested_employee


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
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Update the value.
            EMPLOYEES[index] = new_employee
            break