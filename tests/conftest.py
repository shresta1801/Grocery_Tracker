import os

import pytest
from sqlalchemy import delete
from urllib.parse import quote_plus

from app import GroceryItem, User, app, db


def _test_database_uri():
    if os.environ.get('TEST_DATABASE_URL'):
        return os.environ['TEST_DATABASE_URL']
    user = os.environ.get('MYSQL_USER', 'root')
    password = os.environ.get('MYSQL_PASSWORD', '')
    host = os.environ.get('MYSQL_HOST', '127.0.0.1')
    port = os.environ.get('MYSQL_PORT', '3306')
    database = os.environ.get('MYSQL_TEST_DATABASE', 'grocery_tracker_test')
    return (
        f'mysql+pymysql://{quote_plus(user)}:{quote_plus(password)}'
        f'@{host}:{port}/{database}?charset=utf8mb4'
    )


def _purge_test_rows():
    """Clear app tables without dropping schema (avoids db.drop_all())."""
    with app.app_context():
        db.session.execute(delete(GroceryItem))
        db.session.execute(delete(User))
        db.session.commit()


@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = _test_database_uri()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False

    with app.app_context():
        db.get_engine(app).dispose()
        db.create_all()
        _purge_test_rows()

    with app.test_client() as test_client:
        yield test_client

    _purge_test_rows()


@pytest.fixture
def auth_client(client):
    """Authenticated client fixture"""
    client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpass123'
    })
    client.post('/login', data={
        'username': 'testuser',
        'password': 'testpass123'
    })
    return client


@pytest.fixture
def sample_item():
    """Sample grocery item data"""
    return {
        'name': 'Test Item',
        'category': 'Dairy',
        'quantity': '1 gallon',
        'expiry_date': '2024-12-31'
    }
