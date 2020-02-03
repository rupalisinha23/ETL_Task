# ETL Pipeline with PostgreSQL

This project creates ETL pipeline to create tables via horizontal partitioning, reads csv fines, populate the tables and then queries the tables.

## Getting Started

Download the project: You can download it as zip and unpack the files or you can clone this repository
### Pre-requisites
One should have docker already installed in the machine. For more information please refer https://docs.docker.com/install/

## Executing and Setting Up
After the pre-requisites are satisfied:
In Terminal/CommandPromt run:

```
cd ~/ETL_Task
docker-compose up --build
```

## File structure
./data: contains data
create_tables.py: establishes the connection with the postgres server and creates database
etl.py: loads the data and queries to get the results

## Author
* **Rupali Sinha** - *Initial work*
