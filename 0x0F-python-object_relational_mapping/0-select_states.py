#!/usr/bin/python3
import sys
import MySQLdb as _mysql


if __name__ == "__main__":
    db = _mysql.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]