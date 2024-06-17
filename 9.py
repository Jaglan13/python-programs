import mysql.connector

# Function to create a connection to the MySQL database
def create_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="employee_database"
    )
    return conn

# Function to create the employee table
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            designation VARCHAR(255),
            salary FLOAT
        )
    """)
    print("Table 'employees' created successfully!")

# Function to add details of an employee
def add_employee(conn, emp_id, emp_name, designation, salary):
    cursor = conn.cursor()
    sql = "INSERT INTO employees (id, name, designation, salary) VALUES (%s, %s, %s, %s)"
    values = (emp_id, emp_name, designation, salary)
    cursor.execute(sql, values)
    conn.commit()
    print("Employee added successfully!")

# Function to search for an employee by ID
def search_employee(conn, emp_id):
    cursor = conn.cursor()
    sql = "SELECT * FROM employees WHERE id = %s"
    cursor.execute(sql, (emp_id,))
    employee = cursor.fetchone()
    if employee:
        print("Employee found:")
        print("ID:", employee[0])
        print("Name:", employee[1])
        print("Designation:", employee[2])
        print("Salary:", employee[3])
    else:
        print("Employee not found!")

# Function to delete an employee by ID
def delete_employee(conn, emp_id):
    cursor = conn.cursor()
    sql_select = "SELECT * FROM employees WHERE id = %s"
    cursor.execute(sql_select, (emp_id,))
    employee = cursor.fetchone()

    if employee:
        sql_delete = "DELETE FROM employees WHERE id = %s"
        cursor.execute(sql_delete, (emp_id,))
        conn.commit()
        print("Employee with ID", emp_id, "deleted successfully.")
    else:
        print("Employee with ID", emp_id, "not found.")

# Function to update employee details by ID
def update_employee(conn, emp_id, designation, salary):
    cursor = conn.cursor()
    sql = "UPDATE employees SET designation = %s, salary = %s WHERE id = %s"
    values = (designation, salary, emp_id)
    cursor.execute(sql, values)
    conn.commit()
    print("Employee details updated successfully!")

# Function to print all employees
def print_all_employees(conn):
    cursor = conn.cursor()
    sql = "SELECT * FROM employees"
    cursor.execute(sql)
    employees = cursor.fetchall()
    if employees:
        print("All Employees:")
        for employee in employees:
            print("ID:", employee[0])
            print("Name:", employee[1])
            print("Designation:", employee[2])
            print("Salary:", employee[3])
            print("-----------------------")
    else:
        print("No employees found!")

# Main function
def main():
    # Create a connection to the MySQL database
    conn = create_connection()

    # Create the employee table if it doesn't exist
    create_table(conn)

    # Menu-driven interface
    while True:
        print("\nMENU:")
        print("1. Add Employee")
        print("2. Search Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Print All Employees")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            n=int(input("enter number of employees:"))
            for i in range(n):
                emp_id = input("Enter employee ID: ")
                emp_name = input("Enter employee name: ")
                designation = input("Enter employee designation: ")
                salary = float(input("Enter employee salary: "))
                add_employee(conn, emp_id, emp_name, designation, salary)
        elif choice == "2":
            emp_id = input("Enter employee ID to search: ")
            search_employee(conn, emp_id)
        elif choice == "3":
            emp_id = input("Enter employee ID to update: ")
            designation = input("Enter new designation: ")
            salary = float(input("Enter new salary: "))
            update_employee(conn, emp_id, designation, salary)
        elif choice == "4":
            emp_id = input("Enter employee ID to delete: ")
            delete_employee(conn, emp_id)
        elif choice == "5":
            print_all_employees(conn)
        elif choice == "6":
            break
        else:
            print("Invalid choice! Please enter a valid option.")

    # Close the database connection
    conn.close()
    print("Connection closed.")

main()