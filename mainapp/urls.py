from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    
    path('', views.index, name='index'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('tnc/', views.tnc, name='tnc'),
    path('download/', views.download, name='download'),
    path('comming-soon/', views.comming, name='comming'),
    path('contact/', views.index, name='indexc'), 
    path('merchantcontact/', views.index, name='indexmc'),
    path('merchants-list/', views.merchant, name='merchant'),
    path('music/', views.music, name='music'),
    path('quiz/', views.quizcat, name='quizcat'),
    path('quiz/<str:category_name>/', views.sets, name='sets'),
    path('quiz/set/<int:set_id>/', views.quiz, name='quiz'),
]
