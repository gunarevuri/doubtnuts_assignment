# doubtnuts_assignment
#### To run this project
1.Clone the project

2.Enter your aws iam user credentials key_id and secret_key_id

3.Enter your bucket name and region where you bucket present in the settings.py file.

5.Enter your Postgres database credentials.

6.Then Run

```
python3 manage.py makemigrations
```

It will create migrations folder and contain all required maigrations over db, then run 

```
python3 manage.py migrate
```

Then it will automatically create all tables with required columns.I think 17 relations will be created.Then create superuser for django admin 

```
python3 manage.py createsuperuser
```

Make sure to collect your admin required static files put into aws S3 bucket for that run following command

```
python3 manage.py collectstatic
```

If you run your ```python3 manage.py runserver``` command it will automatically fetch data required for admin page from AWS S3 bucket.

#### For this project Frontend is not developed only REST API
