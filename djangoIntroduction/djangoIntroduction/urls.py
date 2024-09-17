"""
STEP 1: Create a project
STEP 2: Create an app
STEP 3: Add the app to MY_APPS

# If Postgres is needed

STEP 4: Replace DB settings with Postgres DB settings
STEP 5: Enter credentials
STEP 6: Install psycopg2
STEP 7: Create the database
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('djangoIntroduction.todo_app.urls'))
]
