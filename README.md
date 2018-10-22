# app-mpl-purchase-orders

1. Create GCP project
2. Download sources
```
git@github.com:brmespiritu/apps-mpl-purchase-orders.git
```
3. Go to source folder
```
cd apps-mpl-purchase-orders
```
4. Create virtualenv and install dependencies
```
virtualenv env
source env/bin/activate
pip install -r requirements-vendor.txt -t lib/
pip install -r requirements.txt
```
5. Create an app.yaml file from the sample [app.yaml.sample](./app.yaml.sample) and set the environment variables
6. When connecting to Cloud SQL from local machine, install the Cloud SQL Proxy and connect by following the steps from this documentation: https://cloud.google.com/sql/docs/mysql/sql-proxy
Authenticated properly for connecting to Cloud SQL
```
gcloud auth application-default login
```
Then, run Cloud SQL Proxy
```
./cloud_sql_proxy -instances=mpl-po:us-central1:mpl=tcp:3309
```

7. Open another tab and set environment variables using the following commands
```
export CLOUD_SQL_CONNECTION_STRING=<CLOUD_SQL_CONNECTION_STRING>
export DB_USER=<DB username>
export DB_PASSWORD=<DB password>
export DJANGO_ENV=<dev or cloud_sql_proxy or local>
export DJANGO_SECRET_KEY=<any text>
export DEBUG:=<True or False>
```
8. Initialize the database and generate static files
```
python manage.py migrate
python manage.py collectstatic
```
9. Create a superuser
https://docs.djangoproject.com/en/2.1/intro/tutorial02/#creating-an-admin-user
10. To run locally
```
dev_appserver.py .
```
11. To deploy to app engine, make sure gcloud configuration is set correctly
```
gcloud app deploy app.yaml --version v1
```
12. Access app using the URL https://<GCP_PROJECT_ID>.appspot.com/
