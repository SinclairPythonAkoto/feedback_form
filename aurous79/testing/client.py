import os
import pytest
from aurous79 import app
from aurous79.extension import init_db
from dotenv import load_dotenv
load_dotenv()


@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["MEMORY"]
    app.config['TESTING'] = True
    client = app.test_client()

    # create db models
    with app.app_context():
        init_db()
    
    yield client