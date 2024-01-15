#!/usr/bin/python3
"""List States module"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    """Import the MySQLdb module"""

    db = MySQLdb.connect(
            host="localhost",
            password=sys.argv[1],
            user=sys.argv[2],
            database=sys.argv[3]
        )
    c = db.cursor()

    c.execute("""SELECT * FROM states ORDER BY id""")
    results = c.fetchall()

    for row in results:
        print(row)
