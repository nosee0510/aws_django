from django.urls import path
from sugang import views


app_name = 'sugang'
urlpatterns = [

    # Example: /sugang
    path('', views.SubjectLV.as_view(), name='index'),

    # Example: /sugang/subject/, same as /apply/
    path('subject', views.SubjectLV.as_view(), name='subject_list'),

    # Example:/sugang/subject/99/
    path('subject/<int:pk>/', views.SubjectDV.as_view(), name='subject_detail'),

    # Example: /sugang/apply/99/
    path('apply/<int:pk>/', views.ApplyDV.as_view(), name='apply_detail'),

    # Example: /photo/album/add/
    path('subject/add/', views.SubjectApplyCV.as_view(), name='subject_add'),

    # Example: /photo/album/change/
    path('subject/change/', views.SubjectChangeLV.as_view(), name='subject_change'),

    # Example: /photo/album/99/update/
    path('subject/<int:pk>/update/', views.SubjectApplyUV.as_view(), name='subject_update'),

    # Example: /photo/album/99/delete/
    path('subject/<int:pk>/delete/', views.SubjectDelV.as_view(), name='subject_delete'),

    # Example: /photo/photo/add/
    path('apply/add/', views.ApplyCV.as_view(), name='apply_add'),

    # Example: /photo/photo/change/
    path('apply/change/', views.ApplyChangeLV.as_view(), name='apply_change'),

    # Example: /photo/photo/99/update/
    path('apply/<int:pk>/update/', views.ApplyUV.as_view(), name='apply_update'),

    # Example: /photo/photo/99/delete/
    path('apply/<int:pk>/delete/', views.ApplyDelV.as_view(), name='apply_delete'),

]