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
