from django.urls import path
from . import views

app_name = 'danhmucsanpham'
urlpatterns = [
    path('', views.ClassSaveNews.as_view(), name = 'list'),

]
