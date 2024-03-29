import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="tope",
                                  password="pingu",
                                  host="localhost",
                                  port="5432",
                                  database="todo")
    cursor = connection.cursor()
    # Print PostgreSQL details
    #print("PostgreSQL server information")
    #print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT * FROM entry;")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

