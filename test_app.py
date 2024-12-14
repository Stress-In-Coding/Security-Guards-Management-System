import pytest
from app import app, db, User
from flask_jwt_extended import create_access_token
import json

@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

@pytest.fixture
def auth_headers():
    user = User(
        user_id='test-uuid',
        username='test_admin',
        password_hash='hashed_password',
        role='admin'
    )
    db.session.add(user)
    db.session.commit()
    
    access_token = create_access_token(identity='test_admin')
    return {'Authorization': f'Bearer {access_token}'}

def test_register(client):
    response = client.post('/auth/register', 
        json={
            'username': 'testuser',
            'password': 'testpass',
            'role': 'user'
        }
    )
    assert response.status_code == 201
    assert b'User created successfully' in response.data

def test_login(client):
    # First register a user
    client.post('/auth/register', 
        json={
            'username': 'testuser',
            'password': 'testpass',
            'role': 'user'
        }
    )
    
    # Then try to login
    response = client.post('/auth/login',
        json={
            'username': 'testuser',
            'password': 'testpass'
        }
    )
    assert response.status_code == 200
    assert 'access_token' in json.loads(response.data)

def test_get_employees_unauthorized(client):
    response = client.get('/api/employees')
    assert response.status_code == 401

def test_get_employees_authorized(client, auth_headers):
    response = client.get('/api/employees', headers=auth_headers)
    assert response.status_code == 200

# Add more test cases...

if __name__ == '__main__':
    pytest.main(['-v'])
