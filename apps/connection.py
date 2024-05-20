import psycopg2
from config import (host,
                     user,
                     port,
                     password,
                     db_name,
                     )

try:
    connection = psycopg2.connect(host=host,
                                  user=user,
                                  port=port,
                                  database=db_name,
                                  )
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")

    print("Server version", cursor.fetchone())

except Exception as _ex:
    print(('[INFO] PostgreSQL connection closed'), _ex)
  
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection was closed")