"""Create a MySQL SQL dump backup (same logic as app exit backup)."""
from app import app, create_backup

if __name__ == '__main__':
    with app.app_context():
        create_backup()
