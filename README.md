# Django-Querysets-and-Managers
Author: Olubayode Ebenezer
Created 15-07-2022 08:43:55

I builts more features for URL shortener service.

I Created a new GitHub repository with a README.md, and Python .gitignore file.

Cloned it to my machine/computer, which will create a new folder on my computer with my repository’s content. Copied my Django project files from the previous task “Working with APIs”, to the newly created folder.

I Created a new virtual environment in that folder named venv.  Activated it and installed the Django python package (Hint: `pip install Django).

Also, installed the Django rest framework (pip install djangorestframework)

I want users of the API to view all active links. I also want to provide users with an endpoint to view Links created during the week.

I Created a new file, managers.py in my links app folder. 
You can see sample of starter files to be added to the managers.py here 👇
https://github.com/TobeTek/Zuri/blob/main/starter-files/Querysets-and-Managers/managers.py

I Added the following attributes to my Link model in links/models.py

objects = models.Manager()

public = ActiveLinkManager()

# On to the views. 
I  added ActiveLinkView and RecentLinkView u can see samples here 👇
https://github.com/TobeTek/Zuri/blob/main/starter-files/Querysets-and-Managers/views.py to links/views.py.

I Added the following new URL paths in links/urls.py.

path("active/", ActiveLinkView.as_view(), name=’active_link’)

path("recent/", RecentLinkView.as_view(), name=’recent_link’)

I Staged and Commit my Django project and push my changes to my GitHub repository. 


Resources:


Django - Project Setup (https://www.youtube.com/watch?v=c8wy96eAHOs&pp=wgIGCgQQAhgB)

DJANGO - DRF API Views and Permissions ( https://www.youtube.com/watch?v=dt42L4N_DdY&pp=wgIGCgQQAhgB)

Django ORM (Querysets) · HonKit (https://tutorial.djangogirls.org/en/django_orm/)

Django Tutorial | Django Queryset, Filter & ORM (https://www.programink.com/django-tutorial/django-queryset.html)
