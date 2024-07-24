from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="articles-home"),
    path("view/<article_id>", views.view_article, name="view-article")
]