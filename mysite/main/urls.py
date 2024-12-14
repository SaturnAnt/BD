from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),    
    path('contact/', views.contact, name='contact'), 
    path('login/', views.login, name='login'), 

    path('area/', views.area, name='area'), 
    path('well/', views.well, name='well'), 
    path('column/', views.column, name='column'),
    path('cementing/', views.cementing, name='cementing'),
    
    path('mainbar/', views.mainbar, name='mainbar'), 

    path('area/filter', views.area_list, name='area_list'),
    path('area/create', views.Area_typeCreate.as_view(), name='area_create'),
    path('area/<int:pk>/update/', views.Area_typeUpdate.as_view(), name='area_update'),
    path('area/<int:pk>/delete/', views.Area_typeDelete.as_view(), name='area_delete'),

    path('well/filter', views.well_list, name='well_list'),
    path('well/create', views.Well_typeCreate.as_view(), name='well_create'),
    path('well/<int:pk>/update/', views.Well_typeUpdate.as_view(), name='well_update'),
    path('well/<int:pk>/delete/', views.Well_typeDelete.as_view(), name='well_delete'),

    path('column/filter', views.column_list, name='column_list'),
    path('column/create', views.Сolumn_typeCreate.as_view(), name='column_create'),
    path('column/<int:pk>/update/', views.Сolumn_typeUpdate.as_view(), name='column_update'),
    path('column/<int:pk>/delete/', views.Сolumn_typeDelete.as_view(), name='column_delete'),

    path('cementing/filter', views.cementing_list, name='cementing_list'),
    path('cementing/create', views.Cementing_typeCreate.as_view(), name='cementing_create'),
    path('cementing/<int:pk>/update/', views.Cementing_typeUpdate.as_view(), name='cementing_update'),
    path('cementing/<int:pk>/delete/', views.Cementing_typeDelete.as_view(), name='cementing_delete'),
]
