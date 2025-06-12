from django.urls import path
from news.views import home_view , article_detail_view

urlpatterns = [
    path("", home_view),
    path("article-detail/<int:pk>/", article_detail_view),
]



