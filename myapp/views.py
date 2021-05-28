from django.shortcuts import render
from django.urls import reverse_lazy
from django.conf import settings
from .models import *
from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def base(request):
    return render(request, 'myapp/base.html')

def api_urls(request):
    return render(request,'myapp/api_urls.html')

def error_404(request):
    return render(request, "myapp/404.html", {})



#Flores Views
class FloresCreateView(LoginRequiredMixin,CreateView):
    model = Flores
    template_name = 'myapp/Flores/Flores_create.html'  # <appname>/<modelname_list>
    fields = '__all__'
    success_url = reverse_lazy('myapp:Flores_list') 


class FloresListView(LoginRequiredMixin,ListView):
    model = Flores
    template_name = 'myapp/Flores/Flores_list.html'  # <appname>/<modelname_list>
    queryset = Flores.objects.all()

class FloresUpdateView(LoginRequiredMixin,UpdateView):
    model = Flores
    template_name = 'myapp/Flores/Flores_update.html'  # <appname>/<modelname_list>
    fields = '__all__'
    success_url = reverse_lazy('myapp:Flores_list') 


class FloresDetailView(LoginRequiredMixin,DetailView):
    model = Flores
    template_name = 'myapp/Flores/Flores_details.html'  # <appname>/<modelname_list>
    queryset = Flores.objects.all()

class FloresDeleteView(LoginRequiredMixin,DeleteView):
    model = Flores
    template_name = 'myapp/Flores/Flores_delete.html'  # <appname>/<modelname_list>
    success_url = reverse_lazy('myapp:Flores_list') 
    




#Coronas Views
class CoronasCreateView(LoginRequiredMixin,CreateView):
    model = Coronas
    template_name = 'myapp/Coronas/Coronas_create.html'  # <appname>/<modelname_list>
    fields = '__all__'
    success_url = reverse_lazy('myapp:Coronas_list') 


class CoronasListView(LoginRequiredMixin,ListView):
    model = Coronas
    template_name = 'myapp/Coronas/Coronas_list.html'  # <appname>/<modelname_list>
    queryset = Coronas.objects.all()

class CoronasUpdateView(LoginRequiredMixin,UpdateView):
    model = Coronas
    template_name = 'myapp/Coronas/Coronas_update.html'  # <appname>/<modelname_list>
    fields = '__all__'
    success_url = reverse_lazy('myapp:Coronas_list') 


class CoronasDetailView(LoginRequiredMixin,DetailView):
    model = Coronas
    template_name = 'myapp/Coronas/Coronas_details.html'  # <appname>/<modelname_list>
    queryset = Coronas.objects.all()

class CoronasDeleteView(LoginRequiredMixin,DeleteView):
    model = Coronas
    template_name = 'myapp/Coronas/Coronas_delete.html'  # <appname>/<modelname_list>
    success_url = reverse_lazy('myapp:Coronas_list') 
    




#Transporte Views
class TransporteCreateView(LoginRequiredMixin,CreateView):
    model = Transporte
    template_name = 'myapp/Transporte/Transporte_create.html'  # <appname>/<modelname_list>
    fields = '__all__'
    success_url = reverse_lazy('myapp:Transporte_list') 


class TransporteListView(LoginRequiredMixin,ListView):
    model = Transporte
    template_name = 'myapp/Transporte/Transporte_list.html'  # <appname>/<modelname_list>
    queryset = Transporte.objects.all()

class TransporteUpdateView(LoginRequiredMixin,UpdateView):
    model = Transporte
    template_name = 'myapp/Transporte/Transporte_update.html'  # <appname>/<modelname_list>
    fields = '__all__'
    success_url = reverse_lazy('myapp:Transporte_list') 


class TransporteDetailView(LoginRequiredMixin,DetailView):
    model = Transporte
    template_name = 'myapp/Transporte/Transporte_details.html'  # <appname>/<modelname_list>
    queryset = Transporte.objects.all()

class TransporteDeleteView(LoginRequiredMixin,DeleteView):
    model = Transporte
    template_name = 'myapp/Transporte/Transporte_delete.html'  # <appname>/<modelname_list>
    success_url = reverse_lazy('myapp:Transporte_list') 
    


#Construccion Views
class ConstruccionCreateView(LoginRequiredMixin,CreateView):
    model = Construccion
    template_name = 'myapp/Construccion/Construccion_create.html'  # <appname>/<modelname_list>
    fields = '__all__'
    success_url = reverse_lazy('myapp:Construccion_list') 


class ConstruccionListView(LoginRequiredMixin,ListView):
    model = Construccion
    template_name = 'myapp/Construccion/Construccion_list.html'  # <appname>/<modelname_list>
    queryset = Construccion.objects.all()

class ConstruccionUpdateView(LoginRequiredMixin,UpdateView):
    model = Construccion
    template_name = 'myapp/Construccion/Construccion_update.html'  # <appname>/<modelname_list>
    fields = '__all__'
    success_url = reverse_lazy('myapp:Construccion_list') 


class ConstruccionDetailView(LoginRequiredMixin,DetailView):
    model = Construccion
    template_name = 'myapp/Construccion/Construccion_details.html'  # <appname>/<modelname_list>
    queryset = Construccion.objects.all()

class ConstruccionDeleteView(LoginRequiredMixin,DeleteView):
    model = Construccion
    template_name = 'myapp/Construccion/Construccion_delete.html'  # <appname>/<modelname_list>
    success_url = reverse_lazy('myapp:Construccion_list') 




#Hotalizas Views
class AgriculturaCreateView(LoginRequiredMixin,CreateView):
    model = Agricultura
    template_name = 'myapp/Agricultura/Agricultura_create.html'  # <appname>/<modelname_list>
    fields = '__all__'
    success_url = reverse_lazy('myapp:Agricultura_list') 


class AgriculturaListView(LoginRequiredMixin,ListView):
    model = Agricultura
    template_name = 'myapp/Agricultura/Agricultura_list.html'  # <appname>/<modelname_list>
    queryset = Agricultura.objects.all()

class AgriculturaUpdateView(LoginRequiredMixin,UpdateView):
    model = Agricultura
    template_name = 'myapp/Agricultura/Agricultura_update.html'  # <appname>/<modelname_list>
    fields = '__all__'
    success_url = reverse_lazy('myapp:Agricultura_list') 


class AgriculturaDetailView(LoginRequiredMixin,DetailView):
    model = Agricultura
    template_name = 'myapp/Agricultura/Agricultura_details.html'  # <appname>/<modelname_list>
    queryset = Agricultura.objects.all()

class AgriculturaDeleteView(LoginRequiredMixin,DeleteView):
    model = Agricultura
    template_name = 'myapp/Agricultura/Agricultura_delete.html'  # <appname>/<modelname_list>
    success_url = reverse_lazy('myapp:Agricultura_list') 
    




#Cerdo Views
class CerdoCreateView(LoginRequiredMixin,CreateView):
    model = Cerdo
    template_name = 'myapp/Cerdo/Cerdo_create.html'  # <appname>/<modelname_list>
    fields = '__all__'
    success_url = reverse_lazy('myapp:Cerdo_list') 



class CerdoListView(LoginRequiredMixin,ListView):
    model = Cerdo
    template_name = 'myapp/Cerdo/Cerdo_list.html'  # <appname>/<modelname_list>
    queryset = Cerdo.objects.all()

class CerdoUpdateView(LoginRequiredMixin,UpdateView):
    model = Cerdo
    template_name = 'myapp/Cerdo/Cerdo_update.html'  # <appname>/<modelname_list>
    fields ='__all__'
    success_url = reverse_lazy('myapp:Cerdo_list') 


class CerdoDetailView(LoginRequiredMixin,DetailView):
    model = Cerdo
    template_name = 'myapp/Cerdo/Cerdo_details.html'  # <appname>/<modelname_list>
    queryset = Cerdo.objects.all()

class CerdoDeleteView(LoginRequiredMixin,DeleteView):
    model = Cerdo
    template_name = 'myapp/Cerdo/Cerdo_delete.html'  # <appname>/<modelname_list>
    success_url = reverse_lazy('myapp:Cerdo_list') 
    


#Topado Views
class TopadoCreateView(LoginRequiredMixin,CreateView):
    model = Topado
    template_name = 'myapp/Topado/Topado_create.html'  # <appname>/<modelname_list>
    fields = '__all__'
    success_url = reverse_lazy('myapp:Topado_list') 



class TopadoListView(LoginRequiredMixin,ListView):
    model = Topado
    template_name = 'myapp/Topado/Topado_list.html'  # <appname>/<modelname_list>
    queryset = Topado.objects.all()

class TopadoUpdateView(LoginRequiredMixin,UpdateView):
    model = Topado
    template_name = 'myapp/Topado/Topado_update.html'  # <appname>/<modelname_list>
    fields ='__all__'
    success_url = reverse_lazy('myapp:Topado_list') 


class TopadoDetailView(LoginRequiredMixin,DetailView):
    model = Topado
    template_name = 'myapp/Topado/Topado_details.html'  # <appname>/<modelname_list>
    queryset = Topado.objects.all()

class TopadoDeleteView(LoginRequiredMixin,DeleteView):
    model = Topado
    template_name = 'myapp/Topado/Topado_delete.html'  # <appname>/<modelname_list>
    success_url = reverse_lazy('myapp:Topado_list') 
    



