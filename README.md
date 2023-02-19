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

#### In pycharm terminal
```
- pip install --upgrade pip --user 
- pip install -r requirements.txt --user 
- python -m pip install --upgrade pillow 
- python.exe -m pip install --upgrade pip
- python -m pip install psycopg2 

- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver
- python manage.py collectstatic
```
##### Django generation of secret key
```
python manage.py shell
```

##### In shell
```
>>from django.core.management.utils import get_random_secret_key                       
>>print(get_random_secret_key()) 
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

### Installation of Heroku
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


### To deploy the project to the heroku websites via different branches

```
git push heroku master
```
```
git push heroku branch-name:master    
```
### To integration the project to the heroku 
```
heroku run python manage.py migrate
```
```
heroku run python manage.py collectstatic
```