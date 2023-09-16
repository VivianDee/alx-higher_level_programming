#!/usr/bin/python3

import MySQLdb
import sys


"""
    A script that lists all states with a given
    name argument from a database
"""
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    param = "SELECT * FROM states WHERE name = %s"
    cur.execute(param, (sys.argv[4],))
    table = cur.fetchall()
    for row in table:
        print("{}".format(row))
    cur.close()
    db.close()
