#!/usr/bin/python3
"""
    A script that lists all cities for a
    specific state in a database
"""


import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    param = "SELECT * FROM states WHERE name = %s"
    cur.execute(param, (sys.argv[4],))
    state = cur.fetchone()
    val = state[0]
    param2 = "SELECT * FROM cities WHERE
    cities.state_id = %s ORDER BY cities.id ASC"
    cur.execute(param2, (val,))
    cities = cur.fetchall()
    length = len(cities)
    for row in cities:
        if length > 1:
            print("{}".format(row[2]), end=", ")
        else:
            print("{}".format(row[2]))
        length = length - 1
    cur.close()
    db.close()
