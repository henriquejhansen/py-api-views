from django.urls import path
from .views import GenreList, GenreDetail, ActorList, ActorDetail

urlpatterns = [
    path("cinema/genres/", GenreList.as_view()),
    path("cinema/genres/<int:pk>/", GenreDetail.as_view()),
    path("cinema/actors/", ActorList.as_view()),
    path("cinema/actors/<int:pk>/", ActorDetail.as_view()),
]
