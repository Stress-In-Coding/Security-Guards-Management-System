from app import db

# Client model represents organizations that hire security guards
class Client(db.Model):
    __tablename__ = 'clients'
    # Unique identifier for each client
    client_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # JSON string containing client details (name, address, contact info)
    client_details = db.Column(db.String(255), nullable=False)
    # One-to-many relationship with employee assignments
    assignments = db.relationship('EmployeeAssignment', backref='client', lazy=True)

class Employee(db.Model):
    __tablename__ = 'employees'
    # Unique identifier for each employee
    employee_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Reference to employee category (SEC, SUP, MGR, etc.)
    category_code = db.Column(db.String(10), db.ForeignKey('employee_category.category_code'))
    # JSON string containing employee details (name, contact, etc.)
    employee_details = db.Column(db.String(255), nullable=False)
    # Relationships
    assignments = db.relationship('EmployeeAssignment', backref='employee', lazy=True)
    trainings = db.relationship('EmployeeTraining', backref='employee', lazy=True)
    qualifications = db.relationship('EmployeeQualification', backref='employee', lazy=True)

# ... (rest of your model classes) 