from django.urls import path
from . import views

urlpatterns = [
    # genres
    path('', views.index.as_view(), name='index'),
    
    # genres/1
    path('<int:pk>/', views.details.as_view(), name='details'),
    
    # Register new user
    path('register/', views.UserFormView.as_view(), name='userform'),
]
