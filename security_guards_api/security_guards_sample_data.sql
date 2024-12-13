from faker import Faker
import random
from datetime import datetime, timedelta
import json
import mysql.connector
from typing import List, Dict

fake = Faker()

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'security_guards'
}

def connect_to_db():
    """Establish database connection"""
    return mysql.connector.connect(**db_config)

def generate_clients(num_records: int = 25) -> List[Dict]:
    """Generate sample client data"""
    clients = []
    for i in range(1, num_records + 1):
        client_details = {
            'company_name': fake.company(),
            'address': fake.address(),
            'contact_person': fake.name(),
            'phone': fake.phone_number(),
            'email': fake.company_email()
        }
        clients.append({
            'client_id': i,
            'client_details': json.dumps(client_details)
        })
    return clients

def generate_employee_categories() -> List[Dict]:
    """Generate employee categories"""
    categories = [
        {'category_code': 'SEC', 'category_description': 'Security Guard'},
        {'category_code': 'SUP', 'category_description': 'Supervisor'},
        {'category_code': 'MGR', 'category_description': 'Manager'},
        {'category_code': 'TRN', 'category_description': 'Trainee'},
        {'category_code': 'SPL', 'category_description': 'Specialist'}
    ]
    return categories

def generate_employees(num_records: int = 30) -> List[Dict]:
    """Generate sample employee data"""
    categories = ['SEC', 'SUP', 'MGR', 'TRN', 'SPL']
    employees = []
    for i in range(1, num_records + 1):
        employee_details = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'dob': fake.date_of_birth(minimum_age=21, maximum_age=65).strftime('%Y-%m-%d'),
            'address': fake.address(),
            'phone': fake.phone_number(),
            'email': fake.email(),
            'hire_date': fake.date_between(start_date='-5y').strftime('%Y-%m-%d')
        }
        employees.append({
            'employee_id': i,
            'category_code': random.choice(categories),
            'employee_details': json.dumps(employee_details)
        })
    return employees

def generate_training_courses(num_records: int = 10) -> List[Dict]:
    """Generate training courses data"""
    courses = []
    course_types = ['First Aid', 'Self Defense', 'Surveillance', 'Emergency Response', 
                   'Conflict Resolution', 'Weapons Training', 'Crisis Management',
                   'Communication Skills', 'Legal Requirements', 'Safety Procedures']
    
    for i in range(1, num_records + 1):
        course_details = {
            'course_name': course_types[i-1],
            'duration': f"{random.randint(1, 5)} days",
            'instructor': fake.name(),
            'certification': bool(random.getrandbits(1))
        }
        courses.append({
            'course_id': i,
            'course_details': json.dumps(course_details)
        })
    return courses

def generate_qualifications(num_records: int = 8) -> List[Dict]:
    """Generate qualifications data"""
    qualification_types = [
        'Security License', 'First Aid Certificate', 'Weapons Permit',
        'Crisis Management Certification', 'Surveillance Certification',
        'Emergency Response Certificate', 'Safety Officer Certificate',
        'Leadership Certification'
    ]
    
    qualifications = []
    for i in range(1, num_records + 1):
        qualification_details = {
            'qualification_name': qualification_types[i-1],
            'issuing_authority': fake.company(),
            'validity_period': f"{random.randint(1, 5)} years"
        }
        qualifications.append({
            'qualification_id': i,
            'qualification_details': json.dumps(qualification_details)
        })
    return qualifications

def generate_assignments(employees: List[Dict], clients: List[Dict]) -> List[Dict]:
    """Generate employee assignments"""
    assignments = []
    for employee in employees:
        num_assignments = random.randint(1, 3)
        for _ in range(num_assignments):
            start_date = fake.date_between(start_date='-2y')
            assignments.append({
                'employee_id': employee['employee_id'],
                'client_id': random.choice(clients)['client_id'],
                'start_date': start_date.strftime('%Y-%m-%d'),
                'end_date': (start_date + timedelta(days=random.randint(30, 365))).strftime('%Y-%m-%d')
            })
    return assignments

def insert_sample_data():
    """Insert all sample data into the database"""
    conn = connect_to_db()
    cursor = conn.cursor()
    
    try:
        # Generate and insert clients
        clients = generate_clients()
        cursor.executemany(
            "INSERT INTO clients (client_id, client_details) VALUES (%(client_id)s, %(client_details)s)",
            clients
        )

        # Generate and insert employee categories
        categories = generate_employee_categories()
        cursor.executemany(
            "INSERT INTO employee_category (category_code, category_description) VALUES (%(category_code)s, %(category_description)s)",
            categories
        )

        # Generate and insert employees
        employees = generate_employees()
        cursor.executemany(
            "INSERT INTO employees (employee_id, category_code, employee_details) VALUES (%(employee_id)s, %(category_code)s, %(employee_details)s)",
            employees
        )

        # Generate and insert training courses
        courses = generate_training_courses()
        cursor.executemany(
            "INSERT INTO training_courses (course_id, course_details) VALUES (%(course_id)s, %(course_details)s)",
            courses
        )

        # Generate and insert qualifications
        qualifications = generate_qualifications()
        cursor.executemany(
            "INSERT INTO qualifications (qualification_id, qualification_details) VALUES (%(qualification_id)s, %(qualification_details)s)",
            qualifications
        )

        # Generate and insert assignments
        assignments = generate_assignments(employees, clients)
        cursor.executemany(
            "INSERT INTO employee_assignments (employee_id, client_id, start_date, end_date) VALUES (%(employee_id)s, %(client_id)s, %(start_date)s, %(end_date)s)",
            assignments
        )

        conn.commit()
        print("Sample data inserted successfully!")

    except Exception as e:
        conn.rollback()
        print(f"Error inserting sample data: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    insert_sample_data()
