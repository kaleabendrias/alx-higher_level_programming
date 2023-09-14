#!/usr/bin/python3
'''script that lists all cities from the database hbtn_0e_4_usa'''
import MySQLdb
import sys


def main():
    # makes conn and executes query
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    username, password, database = sys.argv[1],\
        sys.argv[2], sys.argv[3]
    # Connect to the MySQL server
    db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )
    # Create a cursor object
    cursor = db.cursor()
    # Execute the SQL query to select states with a matching name
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """
    cursor.execute(query)
    # Fetch all the results
    results = cursor.fetchall()
    # Print the results
    for row in results:
        print(row)
    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    from sys import argv
    main()
