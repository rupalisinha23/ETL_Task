import psycopg2
import time
time.sleep(10)
from sql_queries import drop_table_queries, create_table_queries


def create_database():
    """
    This fucntion connects to the database, defines a cursor, drops the database if they exist
    already and create the database
    returns:
    conn: connection to the database
    cur: cursor
    """
    # connect to default database
    conn = psycopg2.connect("host=db dbname=postgres user=postgres password=postgres")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create installs database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS installs")
    cur.execute("CREATE DATABASE installs WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()

    # connect to installs database
    conn = psycopg2.connect("host=db dbname=installs user=postgres password=postgres")
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    """
    This function drops the tables if they already exist
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    This function creates the tables
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    print('creating postgres connection')
    cur, conn = create_database()
    print('dropping existing tables')
    drop_tables(cur, conn)
    print('creating tables')
    create_tables(cur, conn)

    # close the connection
    conn.close()


if __name__ == "__main__":
    main()