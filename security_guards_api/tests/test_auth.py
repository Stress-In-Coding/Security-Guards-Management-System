import pytest
from app import create_app

class TestJWTAuthentication:
    @pytest.fixture
    def client(self):
        # Create test client fixture
        app = create_app()
        app.config['TESTING'] = True
        return app.test_client()

    def test_login_success(self, client):
        # Test successful login with valid credentials
        response = client.post('/login',
            json={'username': 'admin', 'password': 'admin123'})
        assert response.status_code == 200
        assert 'token' in response.json

    # ... (rest of your auth tests) 