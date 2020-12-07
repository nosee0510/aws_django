from django.urls import path
from photo1 import views


app_name = 'photo1'
urlpatterns = [

    # Example: /photo/
    path('', views.AlbumLV.as_view(), name='index'),

    # Example: /photo/album/, same as /photo/
    path('album1', views.AlbumLV.as_view(), name='album1_list'),

    # Example: /photo/album/99/
    path('album1/<int:pk>/', views.AlbumDV.as_view(), name='album1_detail'),

    # Example: /photo/photo/99/
    path('photo1/<int:pk>/', views.PhotoDV.as_view(), name='photo1_detail'),

    # Example: /photo/album/add/
    path('album1/add/', views.AlbumPhotoCV.as_view(), name='album1_add'),

    # Example: /photo/album/change/
    path('album1/change/', views.AlbumChangeLV.as_view(), name='album1_change'),

    # Example: /photo/album/99/update/
    path('album1/<int:pk>/update/', views.AlbumPhotoUV.as_view(), name='album1_update'),

    # Example: /photo/album/99/delete/
    path('album1/<int:pk>/delete/', views.AlbumDelV.as_view(), name='album1_delete'),

    # Example: /photo/photo/add/
    path('photo1/add/', views.PhotoCV.as_view(), name='photo1_add'),

    # Example: /photo/photo/change/
    path('photo1/change/', views.PhotoChangeLV.as_view(), name='photo1_change'),

    # Example: /photo/photo/99/update/
    path('photo1/<int:pk>/update/', views.PhotoUV.as_view(), name='photo1_update'),

    # Example: /photo/photo/99/delete/
    path('photo1/<int:pk>/delete/', views.PhotoDelV.as_view(), name='photo1_delete'),

]