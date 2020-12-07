from django.urls import path
from namecard.views import NamecardLV, NamecardDV, SearchFormView
from namecard import views

app_name = 'namecard'
urlpatterns = [
    path('', NamecardLV.as_view(), name='index'),
    path('<int:pk>/', NamecardDV.as_view(), name='detail'),
    path('search/', SearchFormView.as_view(), name='search'),
    path('add/', views.NamecardCreateView.as_view(), name="add"),
    path('change/', views.NamecardChangeLV.as_view(), name="change"),
    path('<int:pk>/update/', views.NamecardUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', views.NamecardDeleteView.as_view(), name="delete"),
]