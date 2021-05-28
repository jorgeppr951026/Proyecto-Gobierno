from django.urls import path,include
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views


app_name = 'myapp'

urlpatterns = [

    path('',FloresListView.as_view() , name='Flores_list'),
    #path('api_urls',api_urls , name='api_urls'),

    path('404/', error_404, name='error_404'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
    path('accounts/password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
   
    
    #Flores URLS
    path('Flores_list',FloresListView.as_view() , name='Flores_list'),
    path('Flores_create', FloresCreateView.as_view(), name='Flores_create'),
    path('Flores_update/<int:pk>', FloresUpdateView.as_view(), name='Flores_update'),
    path('Flores_delete/<int:pk>', FloresDeleteView.as_view(), name='Flores_delete'),
    path('Flores_details/<int:pk>', FloresDetailView.as_view(), name='Flores_details'),

    #Coronas URLS
    path('Coronas_list',CoronasListView.as_view() , name='Coronas_list'),
    path('Coronas_create', CoronasCreateView.as_view(), name='Coronas_create'),
    path('Coronas_update/<int:pk>', CoronasUpdateView.as_view(), name='Coronas_update'),
    path('Coronas_delete/<int:pk>', CoronasDeleteView.as_view(), name='Coronas_delete'),
    path('Coronas_details/<int:pk>', CoronasDetailView.as_view(), name='Coronas_details'),

    #Transporte URLS
    path('Transporte_list',TransporteListView.as_view() , name='Transporte_list'),
    path('Transporte_create', TransporteCreateView.as_view(), name='Transporte_create'),
    path('Transporte_update/<int:pk>', TransporteUpdateView.as_view(), name='Transporte_update'),
    path('Transporte_delete/<int:pk>', TransporteDeleteView.as_view(), name='Transporte_delete'),
    path('Transporte_details/<int:pk>',TransporteDetailView.as_view(), name='Transporte_details'),

    #Construccion URLS
    path('Construccion_list',ConstruccionListView.as_view() , name='Construccion_list'),
    path('Construccion_create',ConstruccionCreateView.as_view(), name='Construccion_create'),
    path('Construccion_update/<int:pk>', ConstruccionUpdateView.as_view(), name='Construccion_update'),
    path('Construccion_delete/<int:pk>', ConstruccionDeleteView.as_view(), name='Construccion_delete'),
    path('Construccion_details/<int:pk>', ConstruccionDetailView.as_view(), name='Construccion_details'),


    #Agricultura URLS
    path('Agricultura_list',AgriculturaListView.as_view() , name='Agricultura_list'),
    path('Agricultura_create', AgriculturaCreateView.as_view(), name='Agricultura_create'),
    path('Agricultura_update/<int:pk>', AgriculturaUpdateView.as_view(), name='Agricultura_update'),
    path('Agricultura_delete/<int:pk>', AgriculturaDeleteView.as_view(), name='Agricultura_delete'),
    path('Agricultura_details/<int:pk>', AgriculturaDetailView.as_view(), name='Agricultura_details'),
     #Topado URLS
    path('Topado_list',TopadoListView.as_view() , name='Topado_list'),
    path('Topado_create', TopadoCreateView.as_view(), name='Topado_create'),
    path('Topado_update/<int:pk>', TopadoUpdateView.as_view(), name='Topado_update'),
    path('Topado_delete/<int:pk>', TopadoDeleteView.as_view(), name='Topado_delete'),
    path('Topado_details/<int:pk>', TopadoDetailView.as_view(), name='Topado_details'),

   
    #Cerdo URLS
    path('Cerdo_list',CerdoListView.as_view() , name='Cerdo_list'),
    path('Cerdo_create', CerdoCreateView.as_view(), name='Cerdo_create'),
    path('Cerdo_update/<int:pk>', CerdoUpdateView.as_view(), name='Cerdo_update'),
    path('Cerdo_delete/<int:pk>', CerdoDeleteView.as_view(), name='Cerdo_delete'),
    path('Cerdo_details/<int:pk>', CerdoDetailView.as_view(), name='Cerdo_details'),
    

 
   

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



