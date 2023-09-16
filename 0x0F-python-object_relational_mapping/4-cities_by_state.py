#!/usr/bin/python3
"""
    A script that lists all states with a given
    name argument from a database
"""


import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    param = "SELECT * FROM cities ORDER BY cities.id ASC"
    cur.execute(param)
    table = cur.fetchall()
    for row in table:
        print("{}".format(row))
    cur.close()
    db.close()
