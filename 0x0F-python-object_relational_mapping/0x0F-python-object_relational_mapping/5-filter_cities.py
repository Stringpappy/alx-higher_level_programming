#!/usr/bin/python3
""" the script that List all cities of a state """
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    mycur = db.cursor()
    mycur.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    WHERE states.name = '{}';".format(sys.argv[4]))
    states = mycur.fetchall()

    print(", ".join([state[1] for state in states]))