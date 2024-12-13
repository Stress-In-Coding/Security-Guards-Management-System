import pytest
from app import create_app, db
from app.models import Employee, EmployeeCategory

class TestEmployeeEndpoints:
    @pytest.fixture
    def client(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        
        with app.test_client() as client:
            with app.app_context():
                db.create_all()
                yield client
                db.session.remove()
                db.drop_all()

    # ... (rest of your employee tests) 