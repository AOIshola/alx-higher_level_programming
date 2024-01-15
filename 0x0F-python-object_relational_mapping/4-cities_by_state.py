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

    query = """SELECT cities.id, cities.name, states.name FROM cities \
                LEFT JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id"""
    c.execute(query)
    results = c.fetchall()
    for row in results:
        print(row)
