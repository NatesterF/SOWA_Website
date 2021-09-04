from django.urls import path

from . import views

urlpatterns = [
    path('', views.form, name='form'),
#    path('SendForm/', views.handleInput, name='POST Requests'),
    path('leaderboard/',views.getLeaderboard,name="Leaderboard"),
    path('thanks/',views.formSubmitted,name="Thanks")

]
