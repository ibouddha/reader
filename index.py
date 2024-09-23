import psycopg2

def getfromPostgres():
    conn = psycopg2.connect(
        dbname="etldb",
        user="bouddha",
        password="logyouin",
        host="localhost",
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM your_table")
    rows = cur.fetchall()
    
    # print them on a csv file
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([desc[0] for desc in cur.description])
        writer.writerows(rows)
    
    cur.close()
    conn.close()
    print("Data exported to 'your_output_file.csv'")
    return 0

getfromPostgres()