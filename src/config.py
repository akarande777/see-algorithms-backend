from os import getenv
from dotenv import load_dotenv

load_dotenv()

DATABASE_URI = 'postgresql://{username}:{password}@{hostname}:{db_port}/{db_name}'.format(
    username=getenv('DB_USER'),
    password=getenv('DB_PASS'),
    hostname=getenv('DB_HOST'),
    db_port=getenv('DB_PORT'),
    db_name=getenv('DB_NAME')
)

JWT_SECRET_KEY = getenv('JWT_SECRET_KEY')
