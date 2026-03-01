import os

DATABASE_URL = os.environ.get(
    'DATABASE_URL',
    'sqlite:///portfolio.db'
)
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
