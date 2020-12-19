from django.urls import path
from . import views

urlpatterns = [
    path('',views.listing, name="index"),
    path("listing", views.listing, name="listing"),
    path("createjob", views.create_job, name="createjob"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("job/<int:job_id>", views.job, name="job"),
    path("application", views.application, name="application"),
    path("user/<int:user_id>", views.user, name="user"),
    path("categories/<str:category_name>", views.category, name="category")
]