from django.urls import path,include
from . import views
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'apiapp'

urlpatterns = [
    
    #path('get_Flores', views.FloresList.as_view() , name='get_Flores'),
    #path('get_Coronas', views.CoronasList.as_view() , name='get_Coronas'),
    #path('get_Construccion', views.ConstruccionList.as_view() , name='get_Construccion'),
    #path('get_Transporte', views.TransporteList.as_view() , name='get_Transporte'),
    #path('get_Agricultura', views.AgriculturaList.as_view() , name='get_Agricultura'),
    #path('get_Cerdo', views.CerdoList.as_view() , name='get_Cerdo'),
    #path('get_Flores/<str:topado_por>', views.Flores1List.as_view() , name='get_Flores-'),
    #path('get_Coronas/<str:topado_por>', views.Coronas1List.as_view() , name='get_Coronas-'),
    #path('get_Construccion/<str:topado_por>', views.Construccion1List.as_view() , name='get_Construccion-'),
    #path('get_Transporte/<str:topado_por>', views.Transporte1List.as_view() , name='get_Transporte-'),
    #path('get_Agricultura/<str:topado_por>', views.Agricultura1List.as_view() , name='get_Agricultura-'),
    #path('get_Cerdo/<str:topado_por>', views.Cerdo1List.as_view() , name='get_Cerdo-'),
    path('get/<str:municipio>', views.GetMunicipio.as_view() , name='get'),
    path('last_update', views.GetLastUpdate.as_view(), name='last_update')
  

]

if settings.DEBUG:
    urlpatterns = format_suffix_patterns(urlpatterns)



