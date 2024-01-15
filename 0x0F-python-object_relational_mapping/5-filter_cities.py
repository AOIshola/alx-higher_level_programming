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

    match = sys.argv[4]
    query = """SELECT cities.name FROM cities \
                LEFT JOIN states ON cities.state_id = states.id \
                WHERE cities.state_id = (SELECT id FROM states \
                WHERE states.name = %s) ORDER BY cities.id"""
    c.execute(query, (match,))
    results = c.fetchall()
    cities_list = []

    for i, city_tuple in enumerate(results):
        cities_list.append(','.join(city_tuple))
    cities = ', '.join(cities_list)

    print(cities)
