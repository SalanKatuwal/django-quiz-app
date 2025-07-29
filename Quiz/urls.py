from django.urls import path
from . import views
urlpatterns=[
    path('',views.login,name="login"),
    path('register',views.register,name="register"),
    path('home',views.home,name="home"),
    path('logout',views.logout,name="logout"),
    path('checkans/<int:id>/',views.checkans,name="checkans"),
    path('result',views.result,name="result"),
    path('quit',views.quit,name="quit"),
    path('category',views.category,name="category"),
    path('remove_result',views.remove_result,name='remove_result'),
    path('quiz_home',views.quiz_home,name="quiz_home"),
    path('answer',views.answer,name="answer"),
    path('record',views.record,name='record'),
    path('verify_otp', views.verify_otp, name='verify_otp'),
    path('resend',views.resend, name='resend'),
    path('reset', views.reset, name='reset'),
    path('reset_password', views.reset_password, name='reset_password'),
    path('filter', views.filter, name='filter'),
    path('profile', views.profile, name='profile'),
    path('change_password', views.change_password, name='change_password'),
    path('delete_account', views.delete_account, name='delete_account'),
]