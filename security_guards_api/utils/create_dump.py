import subprocess
import os
from dotenv import load_dotenv
from app import ma
from marshmallow import fields, validate
from app.models import Client, Employee

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def create_database_dump():
    """Create a SQL dump of the database"""
    command = [
        'mysqldump',
        '-u', 'your_username',
        '-p', 'your_password',
        'security_guards',
        '>', 'security_guards_dump.sql'
    ]
    subprocess.run(' '.join(command), shell=True)

class ClientSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Client

    client_id = ma.auto_field()
    client_details = fields.Dict(required=True)
    created_at = ma.auto_field()

class EmployeeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Employee

    employee_id = ma.auto_field()
    category_code = fields.Str(required=True, validate=validate.Length(min=2, max=10))
    employee_details = fields.Dict(required=True)
    created_at = ma.auto_field()

if __name__ == '__main__':
    create_database_dump() 