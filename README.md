
xetracker gathers information from foreign currency exchange traders and stores it in the database.

# Installation

## via pip

`pip install xetracker`

xetracker depends on `lxml` and `psycopg2`. In case of problems installing these dependencies try

`sudo apt-get install python-dev libxml2-dev libxslt-dev` to fix `lxml` installation issues

## via setup.py

`sudo python setup.py install`

# Configure postgresql

Install postgresql on your OS. On Debian Linux the steps for installing postgresql 9.4 are found [here](http://goo.gl/4jtlsZ).

[Optional step] Create a data cluster. This step is optional since the installation of the server creates a cluster.

`sudo pg_createcluster -d /var/lib/postgresql/9.4 -l /var/log/postgresql/postgresql-9.4-main.log --start-conf=auto 9.4 main`

[Unnecessary step] Drop a data cluster. Sometimes it is helpful if the installation was messed up.

`sudo pg_dropcluster 9.4 main`

[Unnecessary step] List existing clusters.

`pg_lsclusters`

[Unnecessary step] Disable cluster from startup. Replace value in `start.conf` with `manual`

`sudo vim /etc/postgresql/9.4/main/start.conf`

[Unnecessary step] Start cluster with `pg_ctlcluster`

`sudo pg_ctlcluster 9.4 main start`

# Run tests

From the project root run

`nosetests`

# Access database

```su timofeya
psql -p 5434  -d xe
```
