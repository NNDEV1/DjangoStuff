from django.urls import path
from basicapp import views

app_name = 'basicapp'

urlpatterns = [
    path('formpage/', views.forms_page, name = 'forms_page'),
    path('thank_you/', views.thank_you_page, name='thank_you_page'),
    path('thank/', views.hi, name='hi')
]
