#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    curs = db.cursor()
    curs.execute("SELECT cities.name FROM \
      cities LEFT JOIN states ON states.id = cities.state_id \
      states.name LIKE BINARY %s ORDER BY cities.id ASC", (sys.argv[4],))
    r = curs.fetchall()
    t = list(row[0] for row in r)
    print(*t, sep=", ")
    cur.close()
    db.close()
