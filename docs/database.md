# Database Setups

This guide will help you set up your databases for fixtureless.

## Linux Installation (Ubuntu/Debian)

By following these steps, you can easily have working databases to help fixtureless development and testing.

**Note:** A dollar sign ($) indicates a terminal prompt, as your user, not root.

### SQLite


No setup is necessary.  Django's test suite automatically handles
the creation and tear down of SQLite databases.


### Postgres


1.  Use your package manager to install the postgres server::

        $ sudo apt-get install postgresql postgresql-contrib libpq-dev

1.  Become the postgresql user, and create a user and database.::

        $ sudo su - postgres
        $ createuser test_user
        $ createdb -O test_user test_django_project_db
        $ psql test_django_project_db
        test_django_project_db=# ALTER USER test_user WITH SUPERUSER;
        test_django_project_db=# ALTER USER test_user WITH PASSWORD 'test_user';
        test_django_project_db=# CREATE EXTENSION hstore;
        test_django_project_db=# \q

1.  Edit the file **/etc/postgresql/<version>/main/pg_hba.conf** and add the
    following to the bottom of the file::

        # TYPE  DATABASE                    USER            ADDRESS       METHOD
        local   test_django_project_db      test_user                     trust

4.  Reload postgres::

        sudo service postgresql reload

MySQL
-----

1.  Use your package manager to install the mysql server::

        $ sudo apt-get install mysql-server python-mysqldb libmysqlclient-dev

1.  Log on to the mysql server and configure the new database.::

        $ sudo mysql -u root
        mysql> CREATE DATABASE test_django_project_db;
        mysql> CREATE USER test_user@localhost;
        mysql> GRANT ALL ON *.* TO test_user@localhost;

1.  Reload the MySQL service::

        sudo service mysql restart

