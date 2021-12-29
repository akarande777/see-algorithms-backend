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

BASE_URL = getenv('BASE_URL')
JWT_SECRET_KEY = getenv('JWT_SECRET_KEY')

MAIL_SERVER = getenv('MAIL_SERVER')
MAIL_PORT = getenv('MAIL_PORT')
MAIL_USERNAME = getenv('MAIL_USERNAME')
MAIL_PASSWORD = getenv('MAIL_PASSWORD')

SERIALIZER_SECRET_KEY = 'E1F53135E559C253'
SERIALIZER_PASSWORD_SALT = '84B03D034B409D4E'
