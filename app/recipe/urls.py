from django.urls import path

from recipe import views


app_name = 'recipe'


urlpatterns = [
    path('tags/', views.TagListCreate.as_view(), name='tag')
]
