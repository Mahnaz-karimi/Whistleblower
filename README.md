# Whistle_blower

### First you need to install python 3 and pip 

For windows https://www.geeksforgeeks.org/how-to-install-pip-on-windows/

### Django virtual machine activation

``` 
source ./venv/Scripts/activate 
```
#### or 
``` 
.\venv\Scripts\activate.bat 
```

##### for deactivate venv
```
 deactivate
 ```

#### For install requirements 
```
 pip install -r requirements.txt 
 ```
```
 pip freeze
```
```
pip freeze > requirements.txt
```
#### In pycharm terminal
```
pip install --upgrade pip --user 
pip install -r requirements.txt --user 
python -m pip install --upgrade pillow 
python.exe -m pip install --upgrade pip
python -m pip install psycopg2 

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py collectstatic
```
### Django generation of secret key

```
python manage.py shell
```

##### In shell
```
>>> from django.core.management.utils import get_random_secret_key                       
>>> print(get_random_secret_key()) 
```
##### for generation of secret key by Token_hex(24)
```
python
>>> import secrets
>>> secrets.token_hex(24)
```
### Git commands 

##### For push changing on other branch
``` 
git pull origin master 
```

``` 
git push --set-upstream origin integration
```

```
git remote -v
```
## Heroku 

#### Installation of Heroku
```
Heroku website install heroku 
https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli  
the path should be in environment variable.
```

#### To change or access to the heroku app

```
heroku login
```

```
heroku info <app-name>
```

```
heroku git:remote -a app-name
```


#### To deploy the project to the heroku websites via different branches

```
git push heroku master
```
```
git push heroku branch-name:master    
```
#### To integrate the project to database on heroku
```
heroku run python manage.py migrate
```
```
heroku run python manage.py collectstatic
```
#### To see database name on Heroku
```
heroku addons 
```
```
heroku open
```
```
heroku config:set AWS_STORAGE_BUCKET_NAME="AWS_STORAGE_BUCKET_NAME" 
```
```
heroku config:set EMAIL_USER="email@emai.com"
```
```
heroku config:set EMAIL_PASSWORD="email@emai.com"
```
#### To create superuser on postgres database on Heroku
```
heroku run bash
~ $ python manage.py createsuperuser
```
#### To generate SSH keys
```
heroku keys:add
For more information -> https://devcenter.heroku.com/articles/keys#add-keys-to-a-heroku-account
```
#### To display the token via the CLI
```
heroku auth:token
heroku config:set HEROKU_API_TOKEN ="xxxxx-xxxx-xxx-xxxxxx-xxxxx"
```


#### Redis 

Redis is an open-source, in-memory data structure store that serves as a versatile solution 
for various purposes. It can be used as a cache to store frequently accessed data, improving 
application performance. Redis also functions as a session storage, enabling easy scalability 
for web applications across multiple servers. It supports publish/subscribe messaging, making
it useful for real-time applications and event-driven architectures. Redis provides task queue 
capabilities for background job processing and managing asynchronous workloads. Additionally, 
it offers various data structures like lists, sets, sorted sets, and hashes, which can be 
utilized to efficiently solve specific problems. With its high performance, scalability, 
and flexibility, Redis is widely adopted for a broad range of applications and use cases.






