from flask import Flask, request, jsonify, make_response
import psycopg2
from os import environ

# Creating a Flask application object.
app = Flask(__name__)

# Getting the environment variables.
db_host = environ.get('DB_HOST')
db_username = environ.get('DB_USER')
db_password = environ.get('DB_PASS')
db_name = environ.get('DB_NAME')
db_port = environ.get('DB_PORT')

# A SQL query that is selecting the average price of a trip between two ports on a given day.
SELECT_RATES = '''SELECT TO_CHAR(day::date, 'YYYY-MM-DD'),
CASE WHEN COUNT(price) < 3 THEN NULL ELSE AVG(price) END AS average_price
FROM prices WHERE orig_code = (%s) AND dest_code = (%s) GROUP BY day HAVING day BETWEEN (%s) AND (%s);'''

# Connect to the database
conn = psycopg2.connect(database=db_name, user=db_username,
                        password=db_password, host=db_host, port=db_port)


# A function to execute SQL query, an alternative
# def execute_query(query, *args):
#     conn = psycopg2.connect(database=db_host, user=db_username,
#                             password=db_password, host=db_host, port=db_port)
#     cur = conn.cursor()
#     cur.execute(query, args)
#     result = cur.fetchall()
#     cur.close()
#     conn.close()
#     return result

@app.route('/test', methods=['GET'])
def test():
    return make_response(jsonify({'message': 'test route'}), 200)


#  It takes in a date range, origin, and destination, and returns the rates for that origin/destination
#  pair for that date range
#  :return: json data
@app.route('/rates', methods=['GET'])
def get_rates():
    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(
                SELECT_RATES, (origin, destination, date_from, date_to))
            result = cursor.fetchall()
    return jsonify(result)
