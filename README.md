**Install required packages**

    '''pip install -r requirements.txt'''


**How To start project**

    To Run the Django Development Server :

    '''python manage.py runserver'''

    Start the Celery Worker :
    '''celery -A app.celery worker --pool=solo -l info'''

    Start the Celery Beat Scheduler :
    '''celery -A app beat -l INFO'''

**Django Admin Credentials**
    username: root
    password: root123 


