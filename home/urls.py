from django.urls import path
from .import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns=[
    path('home/',views.indexView,name="home"),
    path('dashboard/',views.dashboardViews,name="dashboard"),
    path('',LoginView.as_view(),name="login"),
    path('register/',views.registerViews,name="register"),
    path('logout/',LogoutView.as_view(next_page='login'),name="logout"),
]

