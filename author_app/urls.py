from django.urls import path
#from author_app.views import author_view 
# from . import views
from .views import author_view # author_view is the function from the views.py and it is going to register here

#from .views import author_view → author_view කියලා direct use කරන්න.
#from . import views → views.author_view කියලා use කරන්න.

# Registering views
urlpatterns =[
    path("author-display/", author_view) #If the next part of the browse request contains author-display/ run the author_view function in views.py of this app.

]