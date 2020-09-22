import psycopg2
conn=psycopg2.connect(user="postgres",password="Superuser",host="127.0.0.1",port="5432",database="postgres")
cursor=conn.cursor()
create_table_query='''Create TABLE tourneys 
                       (NAME TEXT PRIMARY KEY NOT NULL,
                        MOBILE_NO INT NOT NULL,
                        TOURNAMENT_WINS INT NOT NULL,
                        SHOE_SIZE INT NOT NULL);'''
cursor.execute(create_table_query)
#PQL DB not updated without using commit()
conn.commit()
print("Table created")
cursor.close()
conn.close()