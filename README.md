# Database - Lab #5
Python script to deploy a database for parking management

# Getting started / Prerequisites
Clone the repository to your machine. 

Create a virtual environment and activate it:
```shell
python3 -m venv venv
source venv/bin/activate
```

Install project dependencies (run in project root):
`python pip install -r requirements`

Deploy MySQL database and phpMyAdmin (phpMyAdmin optional, as interface for the database).

Create a database and user for the database
  - **Required**: The user must have ALL PRIVILEGES or at least permission level to create and manage a database

Create an `.env` file at the root of the project and fill it with appropriate accesses
- In the MySQL part, the user must have access to the specified database, the database must already exist


## Env/secrets
Env (.env) file:
```
# Database Credentials
DB_HOST=db_ip
DB_NAME=db_name
DB_USER=db_user
DB_PASSWORD=user_password
```