# %%
import csv
import random

def read_employee_data(file_path):
    """
    Reads employee data from a CSV file and returns a list of dictionaries containing employee names and email IDs.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: A list of dictionaries, where each dictionary contains:
              - 'name' (str): Employee's name.
              - 'email' (str): Employee's email ID.
    """
    employees = []  # Initialize an empty list to store employee data

    # Open the CSV file for reading
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)  # Create a dictionary reader for CSV data

        # Iterate through each row in the CSV file
        for row in reader:
            # Append a dictionary with employee name and email to the list
            employees.append({'name': row['Employee_Name'], 'email': row['Employee_EmailID']})

    return employees  # Return the list of employee data


def read_previous_assignments(file_path):
    """
    Reads previous secret child assignments from a CSV file and returns a dictionary mapping employee emails to their assigned secret child emails.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        dict: A dictionary where:
              - Keys (str): Employee email IDs.
              - Values (str): Assigned secret child email IDs.
    """
    previous_assignments = {}  # Initialize an empty dictionary to store assignments

    try:
        # Open the CSV file for reading
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)  # Create a dictionary reader for CSV data

            # Iterate through each row in the CSV file
            for row in reader:
                # Store the secret child email assignment for each employee email
                previous_assignments[row['Employee_EmailID']] = row['Secret_Child_EmailID']

    except FileNotFoundError:
        pass  # If the file is not found, return an empty dictionary without error

    return previous_assignments  # Return the dictionary of previous assignments


import csv

def write_assignments(file_path, assignments):
    """
    Writes employee-secret child assignments to a CSV file.

    Args:
        file_path (str): The path to the CSV file where assignments will be saved.
        assignments (list of dict): A list of dictionaries where each dictionary contains:
            - 'Employee_Name' (str): Name of the employee.
            - 'Employee_EmailID' (str): Email ID of the employee.
            - 'Secret_Child_Name' (str): Name of the assigned secret child.
            - 'Secret_Child_EmailID' (str): Email ID of the assigned secret child.

    Returns:
        None
    """
    # Open the CSV file for writing
    with open(file_path, mode='w', newline='') as file:
        # Define the field names for the CSV file
        fieldnames = ['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID']
        
        # Create a CSV writer object with the specified field names
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write the header row to the CSV file
        writer.writeheader()
        
        # Write each assignment record to the file
        for assignment in assignments:
            writer.writerow(assignment)

    # Printing the writer object (not necessary for functionality, can be removed)
    print(writer)


def generate_assignments(employees, previous_assignments):
    """
    Generates secret child assignments for employees while ensuring:
    - An employee is not assigned to themselves.
    - Employees do not receive the same secret child as in the previous assignments.

    Args:
        employees (list of dict): A list of dictionaries where each dictionary contains:
            - 'name' (str): Name of the employee.
            - 'email' (str): Email ID of the employee.
        previous_assignments (dict): A dictionary where keys are employee emails and values 
                                     are the secret child email IDs from previous assignments.

    Returns:
        list of dict: A list of assignment dictionaries with:
            - 'Employee_Name' (str): Name of the employee.
            - 'Employee_EmailID' (str): Email ID of the employee.
            - 'Secret_Child_Name' (str): Name of the assigned secret child.
            - 'Secret_Child_EmailID' (str): Email ID of the assigned secret child.

    Raises:
        Exception: If no valid assignment is found for an employee.
    """
    assignments = []
    
    # Create a copy of employees list to use as potential secret children
    available_children = employees[:]
    
    # Randomly shuffle the list of available children
    random.shuffle(available_children)

    for employee in employees:
        # Try to find a valid secret child for the current employee
        for i, child in enumerate(available_children):
            if (employee['email'] != child['email'] and  # Ensure they are not assigned to themselves
                previous_assignments.get(employee['email']) != child['email']):  # Ensure no repetition from previous assignments
                
                # Create the assignment entry
                assignments.append({
                    'Employee_Name': employee['name'],
                    'Employee_EmailID': employee['email'],
                    'Secret_Child_Name': child['name'],
                    'Secret_Child_EmailID': child['email']
                })
                
                # Remove the assigned child from the available list
                del available_children[i]
                break
        else:
            # Raise an error if no valid assignment is found
            raise Exception(f"No valid assignment found for employee: {employee['name']}")

    return assignments


def main():
    """
    Main function to generate secret child assignments for employees.

    Steps:
    1. Reads the current year's employee data from a CSV file.
    2. Reads the previous year's assignments to avoid duplicate pairings.
    3. Generates new assignments ensuring no employee gets themselves or their previous secret child.
    4. Writes the new assignments to an output CSV file.

    File Paths:
    - 'current_employee.csv': Contains the current year's employees.
    - 'previous_employee.csv': Stores last year's assignments to prevent repetition.
    - 'employee.csv': The output file with the new secret child assignments.

    Returns:
        None
    """
    current_year_file = 'current_employee.csv'  # Input file with current employee data
    previous_year_file = 'previous_employee.csv'  # Input file with previous year's assignments
    output_file = 'employee.csv'  # Output file for new assignments

    # Read employee data from the current year's file
    employees = read_employee_data(current_year_file)

    # Read previous assignments to prevent duplicate pairings
    previous_assignments = read_previous_assignments(previous_year_file)

    # Generate new secret child assignments
    assignments = generate_assignments(employees, previous_assignments)

    # Print assignments for verification
    print(assignments)

    # Write new assignments to the output CSV file
    write_assignments(output_file, assignments)


if __name__ == '__main__':
    main()


# %%



