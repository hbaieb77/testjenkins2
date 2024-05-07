import csv
import oracledb

pw = 'hr'

connection = oracledb.connect(
    user="hr",
    password=pw,
    dsn="localhost/xepdb1")

print("Successfully connected to Oracle Database")

cursor = connection.cursor()

def extract_and_save_as_csv(cursor, table_name):
    # Execute SQL query to fetch data from table
    cursor.execute(f"SELECT * FROM {table_name}")

    # Get column names
    column_names = [desc[0] for desc in cursor.description]

    # Fetch all rows
    rows = cursor.fetchall()

    # Prepare CSV file name
    csv_filename = f"{table_name}.csv"

    # Write data to CSV file
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(column_names)  # Write column headers
        csv_writer.writerows(rows)         # Write rows of data

    print(f"Data extracted from table '{table_name}' and saved as '{csv_filename}'")


extract_and_save_as_csv(cursor, 'INCIDENTS')





















