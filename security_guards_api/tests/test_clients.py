import pytest
from app import create_app, db
from app.models import Client

class TestClientEndpoints:
    @pytest.fixture
    def client(self):
        # Create test client with in-memory SQLite database
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        
        with app.test_client() as client:
            with app.app_context():
                # Set up fresh database for each test
                db.create_all()
                yield client
                # Clean up after test
                db.session.remove()
                db.drop_all()

    def test_get_clients_empty(self, client):
        # Test GET /clients with empty database
        response = client.get('/clients')
        assert response.status_code == 200
        assert response.json == []

    # ... (rest of your client tests) 