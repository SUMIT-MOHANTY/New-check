from database import init_db, Session
from models import User, PortfolioItem


def create_tables():
    print('Creating database tables...')
    init_db()
    print('Tables created successfully!')


def add_sample_data():
    session = Session()
    try:
        # Check if data exists
        if session.query(User).count() == 0:
            sample_user = User(
                username='admin',
                email='admin@example.com',
                password_hash='hashed_password_here'
            )
            session.add(sample_user)

        if session.query(PortfolioItem).count() == 0:
            sample_item = PortfolioItem(
                title='Sample Portfolio Project',
                description='This is a sample portfolio project.',
                image_url='https://example.com/image.jpg',
                project_url='https://example.com/project',
                skills='Python, SQLAlchemy, Flask'
            )
            session.add(sample_item)

        session.commit()
        print('Sample data added successfully!')
    except Exception as e:
        session.rollback()
        print(f'Error adding sample data: {e}')
    finally:
        session.close()


if __name__ == '__main__':
    create_tables()
    add_sample_data()
