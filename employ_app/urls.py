from django.urls import path
from . import views 

urlpatterns=[
    path("",views.home, name="home"),
    path("view_employ",views.view_employ, name="view_employ"),
    path("add_employ",views.add_employ, name="add_employ"),
    path("delete_employ",views.delete_employ, name="delete_employ"),
    path("delete_employ/<int:emp_id>",views.delete_employ, name="delete_employ"),
    path("Filter_employ",views.Filter_employ, name="Filter_employ"),
    path("about",views.about, name="about"),
    path("contact",views.contact, name="contact"),
    path("job",views.job, name="job"),
    path("privacy",views.privacy, name="privacy"),
]