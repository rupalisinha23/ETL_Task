# DROP TABLES

shard1_drop = "DROP TABLE IF EXISTS installs_by_country_A;"
shard2_drop = "DROP TABLE IF EXISTS installs_by_country_B;"
shard3_drop = "DROP TABLE IF EXISTS installs_by_country_C;"


# CREATE TABLES

shard1_create = ("""
    CREATE TABLE IF NOT EXISTS installs_by_country_1 (
        country varchar NOT NULL,
        created_at timestamp NOT NULL,
        paid boolean NOT NULL,
        installs int NOT NULL);
""")

shard2_create = ("""
    CREATE TABLE IF NOT EXISTS installs_by_country_2 (
        country varchar NOT NULL,
        created_at timestamp NOT NULL,
        paid boolean NOT NULL,
        installs int NOT NULL);
""")

shard3_create = ("""
    CREATE TABLE IF NOT EXISTS installs_by_country_3 (
        country varchar NOT NULL,
        created_at timestamp NOT NULL,
        paid boolean NOT NULL,
        installs int NOT NULL);
""")

# SELECT QUERY TO RETRIEVE DATA

select_query = ("""
    SELECT country,  SUM(installs) FROM {}
        WHERE EXTRACT(YEAR FROM created_at) = '2019' AND EXTRACT(MONTH FROM created_at) = '5'
        AND paid = TRUE
        GROUP BY country;
""")


create_table_queries = [shard1_create, shard2_create, shard3_create]
drop_table_queries = [shard1_drop, shard2_drop, shard3_drop]
