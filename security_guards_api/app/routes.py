from flask import Blueprint, jsonify, request
from app.models import Client, Employee
from app import db
from app.schemas import ClientSchema, EmployeeSchema
from flask_jwt_extended import jwt_required

bp = Blueprint('api', __name__)

@bp.route('/clients', methods=['GET'])
@jwt_required()
def get_clients():
    clients = Client.query.all()
    return jsonify([{'client_id': c.client_id, 'client_details': c.client_details} for c in clients])

# ... (rest of your route handlers) 