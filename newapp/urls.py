from django.urls import path
from .import views 

urlpatterns = [
    path('signup/',views.Signup.as_view(), name='signup'),
    path('login/',views.Login.as_view(), name='login'),
    path('test/view/', views.TestView.as_view(), name='test_view'),
    path('logout/', views.Logout.as_view(), name='logout')
]