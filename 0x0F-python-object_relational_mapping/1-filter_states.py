#!/usr/bin/python3
""" a script that lists all states with a name starting
 with N (upper N) from the database hbtn_0e_0_usa """
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    mycur = db.cursor()
    mycur.execute("SELECT * FROM states WHERE CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS \
    LIKE 'N%';")
    states = mycur.fetchall()

    for state in states:
        print(state)
