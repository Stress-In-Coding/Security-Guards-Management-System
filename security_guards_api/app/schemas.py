from marshmallow import Schema, fields, validate

# Schema for validating and serializing client data
class ClientSchema(Schema):
    # Read-only field for client ID
    client_id = fields.Int(dump_only=True)
    # Required field for client details with minimum length validation
    client_details = fields.Str(required=True, validate=validate.Length(min=1))

# Schema for validating and serializing employee data
class EmployeeSchema(Schema):
    # Read-only field for employee ID
    employee_id = fields.Int(dump_only=True)
    # Required field for category code with length validation
    category_code = fields.Str(required=True, validate=validate.Length(min=2, max=10))
    # Required field for employee details
    employee_details = fields.Str(required=True) 