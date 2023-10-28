from django.urls import path
from . import views

urlpatterns = [
    path('',views.view_questions, name='view_questions'),
    path('registration',views.register_view, name='registration'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('post_question/', views.post_question, name='post_question'),
    path('post_answer/<int:question_id>/', views.post_answer, name='post_answer'),
    path('like_answer/<int:answer_id>/', views.like_answer, name='like_answer'),
    path('view_questions/', views.view_questions, name='view_questions'),
]
