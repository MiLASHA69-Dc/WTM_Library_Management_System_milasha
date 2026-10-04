from django.urls import path
from genre_app.views import view_genre,update_genre,delete_genere


urlpatterns = [
    path("display_genre/",view_genre,name="all_genres"),
    path("delete_genre/<str:delete_id>/",delete_genere,name="delete_genre"),
    path("update_genre/<str:update_id>/",update_genre,name="update_genre")
]