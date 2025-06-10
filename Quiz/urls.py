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
    path('record',views.record,name='record')
]