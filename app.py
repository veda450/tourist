python-m venv env
 cd env
 CAScripts
 Activate
 TD install Django
 PIP install Django
 cd..
 cd..
 (a) Project creation
 To Create a project:
 django-admin start project projectname.
 django-admin Start project project.
 This will create a directory named project.
 manage.py
 myproject/--init--.py
 settings.py
 urls.py
 wsgi.py
 asgi.py
  apps.py
 models.py
 tests.py
 views.py
 Set App1 in project/Settings.py
 INSTALLED APPS=[----,----,
 'APP1',
 ]
 To create Admin
 python manage.py make migrations
 python manage py migrate
 python manager.py crecite supeuser
 username:----
 email:----
 password:---- (not visible)
 confirm password:---- (Not visible)
 Yes/No->Y
 To run the development server:
 Python manage.py run server
 Then Access the admin interface with the following link
 gives in the terminal
