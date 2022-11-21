import psycopg2
import logging

connection = psycopg2.connect(
    host='localhost',
    database='boondocks',
    user='dsuser',
    password='admin',
    port=''
)
table_sql_query = '''
      CREATE TABLE Customer(
      ID INT PRIMARY KEY NOT NULL,
      NAME TEXT NOT NULL,
      AGE INT NOT NULL,
      ADDRESS CHAR(100),
      LOAN_AMOUNT REAL
   )   
'''
pointer = connection.cursor()
pointer.execute(table_sql_query)
connection.commit()
print("table is created ")

