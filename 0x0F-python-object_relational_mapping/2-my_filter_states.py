#!/usr/bin/python3
""" 
A script that takes in an argument and displays all values 
in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(user=username, passwd=password, db=database, port=3306)
        cursor = db.cursor()

        query = "SELECT * FROM states WHERE CONVERT(`name` USING Latin1) COLLATE Latin1_General_CS = %s;"
        cursor.execute(query, (state_name,))
        
        states = cursor.fetchall()

        for state in states:
            print(state)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", e)
        sys.exit(1)



