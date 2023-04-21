import psycopg2
import json

conn = psycopg2.connect(database="database",
                        host="localhost",
                        user="postgres",
                        password="123456789",
                        port="5432")

cursor = conn.cursor()

cursor.execute(""" create table if not exists orders3 (
 id serial NOT NULL PRIMARY KEY,
 info json NOT NULL
); """)
               
conn.commit()

d = { "customer": "John Doe", "items": {"product": "Beer","qty": 6}}
d_json =json.dumps(d)

query_sql = f"insert into orders3 (info) values ('{d_json}')"
cursor.execute(query_sql)
conn.commit()
conn.close()