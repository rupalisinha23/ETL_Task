import time
time.sleep(10)
import psycopg2
from psycopg2 import sql
import pandas as pd
import io
from collections import Counter
from sql_queries import *


def query_table(cur, table_name):
    """
    i/p: cursor
    returns: queried results in dictionary format
    This function takes the cursor as input and queries the data to
    get the installs amount of all the paid countries of May2019
    time span
    """
    cur.execute(
        sql.SQL(select_query)
            .format(sql.Identifier(table_name)))
    records = cur.fetchall()
    return dict(records)


def process_data(cur, conn, i, func, filepath):
    """
    i/p: cursor, connection, index value, ETL function and filepath
    returns: queried records
    This is a helper function for extracting, transforming and loading
    data onto the relational database
    """

    df = pd.read_csv(filepath)
    df = df.drop(df.columns[0], axis=1).set_index('index')
    buf = io.StringIO()
    df.to_csv(buf, header=False, index=False)

    buf.seek(0)
    table_name = 'installs_by_country_'+str(i)
    cur.copy_from(buf, table_name, sep=',')
    conn.commit()
    records = func(cur, table_name)
    return records


def main():
    conn = psycopg2.connect("host=db dbname=installs user=postgres password=postgres")
    cur = conn.cursor()
    temp = {}
    for i in range(1,4):
        records = process_data(cur, conn, i, query_table, filepath='data/shard'+str(i)+'.csv')
        temp = Counter(temp) + Counter(records)
    print('The paid install amount of the countries are:')
    result = pd.DataFrame({'Country': list(temp.keys()),
                 'Installs': list(temp.values())}).set_index('Country')
    print(result)

    conn.close()


if __name__ == "__main__":
    main()
