import psycopg2

with open('/home/voyager/Downloads/text.txt', 'r') as file:
    # Read the entire file content
    file_content = file.read()

# Split text into words
words = file_content.split()

# Generate unique integers from 1 to the number of words in the text
unique_integers = list(range(1, len(words) + 1))

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(dbname="indexes", user="admin", password="secret", host="localhost")

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Loop through words and unique integers and insert into the database
#for text, values in zip(words, unique_integers):
for text in words:
    # SQL query to insert data into the table
    #sql = f"INSERT INTO numbers (values, text) VALUES ({values}, '{text}')"
    sql = f"INSERT INTO numbers (text) VALUES ({text})"

    # Execute the SQL query
    cursor.execute(sql)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
