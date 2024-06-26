#!/usr/bin/python3
""" a script that takes in an argument and displays all
 values in the states table
of hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    mycur = db.cursor()
    mycur.execute("SELECT * \
    FROM states \
    WHERE CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS = '{}';".format(sys.argv[4]))
    states = mycur.fetchall()

    for state in states:
        print(state)
