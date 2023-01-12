from flask import request, Blueprint
import json
import bcrypt
import mysql.connector

def hash_password(text_password):
    hashed_password = bcrypt.hashpw(text_password, bcrypt.gensalt())
    return hashed_password

def check_password(text_password, hashed_value):
    is_right_password = bcrypt.checkpw(text_password, hashed_value)
    return is_right_password

auth = Blueprint('auth', __name__)

# API Endpoint to authenticate user
@auth.get('/authenticate/<user>/<password>')
def authenticate(user,password):
    try:
        SQL_conn = mysql.connector.connect(user='sal', password='sal123', host='localhost', database='StockOptions')
        SQL_cursor = SQL_conn.cursor(dictionary=True)
    except Exception as e:
        return f"{e}"
    # Get hashed password from database for the provided username
    SQL_cursor.execute(f"SELECT password FROM User WHERE username = '{user}' LIMIT 1")
    db_pwd = SQL_cursor.fetchone()['password']
    # Check if the passwords match
    try:
        byte_text_password = bytes(password, 'utf-8')
        byte_db_password = bytes(db_pwd, 'utf-8')
        authenticate = check_password(text_password=byte_text_password, hashed_value=byte_db_password)
    except TypeError:
        SQL_conn.close()
        return f'PWD NOT UNICODE. Given: {byte_text_password}-{byte_db_password}'
    # If they do, return True, else return False
    SQL_conn.close()
    return 'PASS' if authenticate else 'FAIL'

# API Endpoint to create user
@auth.post('/add/<user>/<password>')
def register(user,password):
    byte_password = bytes(password, 'utf-8')
    hashed_pass = str(hash_password(byte_password), 'utf-8')
    # Generate SQL connection
    try:
        SQL_conn = mysql.connector.connect(user='sal', password='sal123', host='localhost', database='StockOptions')
        SQL_cursor = SQL_conn.cursor(dictionary=True)
    except Exception as e:
        return f"{e}"
    # Get hashed password from database for the provided username
    SQL_cursor.execute(f"INSERT INTO User(username, password) VALUES ('{user}','{hashed_pass}')")
    SQL_conn.commit()
    SQL_conn.close()
    return 'PASS'