from django.urls import path
from .  import views

app_name="blog"
urlpatterns = [
    path('',views.archive_list,name="archive"),
    path('<slug>', views.single_detail,name="single"),
]