"""Inspect MySQL tables for the Grocery Tracker app (uses same env as app.py)."""
import pymysql
from sqlalchemy.engine.url import make_url
from tabulate import tabulate

from app import get_database_uri

url = make_url(get_database_uri())
conn = pymysql.connect(
    host=url.host or '127.0.0.1',
    user=url.username or 'root',
    password=url.password or '',
    database=url.database,
    port=url.port or 3306,
    charset='utf8mb4',
)
cursor = conn.cursor()

cursor.execute(
    'SELECT TABLE_NAME FROM information_schema.tables '
    'WHERE table_schema = %s ORDER BY TABLE_NAME',
    (url.database,),
)
tables = cursor.fetchall()

print('\nTables in the database:')
for (table_name,) in tables:
    print(f'\nTable: {table_name}')
    print('-' * 50)
    cursor.execute(f'DESCRIBE `{table_name}`')
    columns = cursor.fetchall()
    print('\nColumns:')
    for col in columns:
        print(f'{col[0]} ({col[1]})')
    cursor.execute(f'SELECT * FROM `{table_name}`')
    rows = cursor.fetchall()
    if rows:
        col_names = [d[0] for d in cursor.description] if cursor.description else []
        print('\nData:')
        print(tabulate(rows, headers=col_names, tablefmt='grid'))
    else:
        print('\nNo data in this table')

conn.close()
