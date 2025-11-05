from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GenreAPIView, ActorGenericAPIView, CinemaHallViewSet, MovieViewSet

router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_hall")
router.register("movies", MovieViewSet)

urlpatterns = [
    path("cinema/genres/", GenreAPIView.as_view()),
    path("cinema/actors/", ActorGenericAPIView.as_view()),
    path("cinema/", include(router.urls)),
]
