database_file = 'SalesTracking.db'
# Connect to the database
conn = sqlite3.connect(database_file)
# Get a cursor pointing to the database
cursor = conn.cursor()
# Create the tables
cursor.executescript(sql)
# Commit to save everything
conn.commit()
# Close the connection to the database
#
cur = conn.cursor()
#