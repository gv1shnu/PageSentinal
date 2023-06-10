import sqlite3


# Connect to the SQLite database
with sqlite3.connect('db/website_states.db') as conn:

    # Create a cursor object
    cursor = conn.cursor()

    # Execute SQL command to get table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()

    # Fetch and print the contents of each table
    for table in tables:
        table_name = table[0]
        print(f"Table: {table_name}")

        # Execute SQL command to fetch all rows from the table
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        # Print the rows
        for row in rows:
            print(row)

        print()

    # Close the cursor and the database connection
    cursor.close()
