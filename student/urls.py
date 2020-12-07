from django.urls import path
from student.views import StudentLV, StudentDV,SearchFormView
from student import views

app_name = 'student'
urlpatterns = [
    path('', StudentLV.as_view(), name='index'),
    path('<int:pk>/', StudentDV.as_view(), name='detail'),
    path('search/', SearchFormView.as_view(), name='search'),
    path('add/', views.StudentCreateView.as_view(), name="add"),
    path('change/', views.StudentChangeLV.as_view(), name="change"),
    path('<int:pk>/update/', views.StudentUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', views.StudentDeleteView.as_view(), name="delete"),
]