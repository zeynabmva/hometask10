from django.urls import path
from . import views
urlpatterns = [
    path("list/" , views.blog_list_view, name="list"),
    path("create/" , views.blog_create_view),
    path("detail/<id>/" , views.blog_detail_view),
    path("update/<id>/" , views.blog_update_view , name="update"),
]