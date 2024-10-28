from django.urls import path
from .views import index, get_category, test

urlpatterns = [
    path("", index, name='home'),
    path("category/<int:category_id>/", get_category, name='category'),
    path("test/", test),
]