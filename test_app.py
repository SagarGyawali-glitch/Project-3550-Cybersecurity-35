import pytest
from flask_testing import TestCase
from Project3A import app, db, User, AuthLog
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class BaseTestCase(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        return app

    def setUp(self):
        db.create_all()
        # Seed the database if necessary

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestUserManagement(BaseTestCase):
    def test_user_registration(self):
        """Test the user registration process."""
        response = self.client.post('/register', json={
            'username': 'newuser',
            'email': 'newuser@example.com'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('password', response.json)

    def test_user_authentication(self):
        """Test the user authentication process."""
        # Register a user first
        self.client.post('/register', json={
            'username': 'testuser',
            'email': 'testuser@example.com'
        })
        user = User.query.filter_by(username='testuser').first()
        response = self.client.post('/auth', json={
            'user_id': user.id
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'success')

    def test_authentication_failure(self):
        """Test authentication failure when user_id is missing."""
        response = self.client.post('/auth', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

# Run the tests
if __name__ == '__main__':
    pytest.main()
