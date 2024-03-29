#!/usr/bin/python3
"""A script that lists all states from the database"""


import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * from states")
    table = cur.fetchall()
    for row in table:
        print("{}".format(row))
    cur.close()
    db.close()
