from django.urls import path
from basicapp import views

app_name = "basicapp"

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('user_login/', views.user_login, name = 'user_login'),
    path('user_post/', views.user_post, name = 'user_post')
]
