from django.conf.urls import url
from .views import blog, details, create

urlpatterns = [
    url("create/", create),
    url("details/(?P<pk>\d+)/", details, name="article_details"),
    url("", blog)
]
