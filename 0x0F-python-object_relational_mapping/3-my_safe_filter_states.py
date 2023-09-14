#!/usr/bin/python3
'''write a script that takes in arguments and displays all values in the states'''
import MySQLdb
import sys


def main():
    # makes conn and executes query
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <tobesearched>".format(sys.argv[0]))
        sys.exit(1)
        
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    
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
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))

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