# Portfolio Database

SQLAlchemy models for User and PortfolioItem.

## Setup

pip install -r requirements.txt
python app.py

## Models

- User: id, username, email, password_hash, created_at
- PortfolioItem: id, title, description, image_url, project_url, skills, created_at, updated_at
