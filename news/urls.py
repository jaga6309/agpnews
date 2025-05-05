from django.urls import path
from news.views import home_view
urlpatterns = [
    path("", home_view),

]



