from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from myapp.models import *
from .serializers import *
from django.db.models import Count

class GetLastUpdate(APIView):
    def get(self, request):
        updates = []

        if Flores.history.first():
            flores_update = Flores.history.first().history_date
            updates.append(flores_update)

        if Coronas.history.first():
            corona_update = Coronas.history.first().history_date
            updates.append(corona_update)

        if Construccion.history.first():
            construccion_update = Construccion.history.first().history_date
            updates.append(construccion_update)
        if Agricultura.history.first():
            agricultura_update = Agricultura.history.first().history_date
            updates.append(agricultura_update)
        if Cerdo.history.first():
            cerdo_update = Cerdo.history.first().history_date
            updates.append(cerdo_update)
        if Transporte.history.first():
            trasporte_update = Transporte.history.first().history_date
            updates.append(trasporte_update)

        updates.sort(reverse=True)  
        if updates[0]:
            last_update = updates[0]
            return Response({'last_update': last_update})
        
        return Response({'menssage': "No hay datos en la base de datos"})



class GetMunicipio(APIView):
    def get(self, request, **kwargs):
        municipio = kwargs['municipio']

        flores = Flores.objects.all()
        coronas = Coronas.objects.all()
        construccions = Construccion.objects.all()
        agricultura = Agricultura.objects.all()
        cerdo = Cerdo.objects.all()
        tranporte = Transporte.objects.all()




        dicc = {}
     
        obj_flores = []
        obj_coronas = []
        obj_construccion = []
        obj_agricultura = []
        obj_cerdo = []
        obj_transporte = []
    #Flores
        for flor in flores:
            existe = False
          

            flor_name = flor.descripcion + ' ' + flor.um 
            for element in obj_flores : 
                if flor_name == element['name']:
                    existe =True
                    if element['topado_por'] == 'Nacional':
                        break
                    else:
                        if  element['topado_por']  == 'Provincial':
                            if flor.topado_por.name == 'Nacional':
                                element['topado_por'] = flor.topado_por.name
                                element['primera'] = flor.precio_1 
                                element['segunda'] = flor.precio_2 
                                element['tercera'] = flor.precio_3
                        elif flor.topado_por.name == municipio or flor.topado_por.name == 'Nacional' or flor.topado_por.name == 'Provincial':
                            element['topado_por'] = flor.topado_por.name
                            element['primera'] = flor.precio_1 
                            element['segunda'] = flor.precio_2 
                            element['tercera'] = flor.precio_3

            if existe == False and ( flor.topado_por.name == municipio or flor.topado_por.name == 'Nacional' or flor.topado_por.name == 'Provincial' )  :
                obj_flores.append({
                    'name': flor.descripcion + ' ' + flor.um ,
                    'primera': flor.precio_1 ,
                    'segunda': flor.precio_2 ,
                    'tercera': flor.precio_3 ,
                    'topado_por': flor.topado_por.name
                })
        if obj_flores :
            dicc['Flores'] = obj_flores
          
    #Coronas
        for corona in coronas:
            existe = False
           
            for element in obj_coronas: 
                if corona.variedades_de_flores == element['cant_variedades_flores']:
                    existe =True
                    if element['topado_por'] == 'Nacional':
                        break
                    else:
                        if  element['topado_por']  == 'Provincial':
                            if corona.topado_por.name == 'Nacional':
                                element['topado_por'] = corona.topado_por.name
                                element['cant_variedades_flores'] = corona.variedades_de_flores 
                                element['docenas'] = corona.cant_docenas 
                                element['diametro'] = corona.diametro_aro
                                element['precio'] = corona.precio_minorista
                        
                        elif corona.topado_por.name == municipio or corona.topado_por.name == 'Nacional' or corona.topado_por.name == 'Provincial'  :
                            element['topado_por'] = corona.topado_por.name
                            element['cant_variedades_flores'] = corona.variedades_de_flores 
                            element['docenas'] = corona.cant_docenas 
                            element['diametro'] = corona.diametro_aro
                            element['precio'] = corona.precio_minorista

            if existe == False and ( corona.topado_por.name == municipio or corona.topado_por.name == 'Nacional' or corona.topado_por.name == 'Provincial' )  :
                obj_coronas.append({
                    'cant_variedades_flores': corona.variedades_de_flores ,
                    'docenas': corona.cant_docenas ,
                    'diametro': corona.diametro_aro ,
                    'precio': corona.precio_minorista ,
                    'topado_por': corona.topado_por.name
                })
        if obj_coronas :
            dicc['Coronas'] = obj_coronas
        
    #Contrucciones
        for material in construccions:
            existe = False
            material_name = material.producto + ' ' + material.um 
            for element in obj_construccion : 
                if material_name == element['name']:
                    existe =True
                    if element['topado_por'] == 'Nacional':
                        break
                    else:
                        if  element['topado_por']  == 'Provincial':
                            if material.topado_por.name == 'Nacional':
                                element['topado_por'] = material.topado_por.name
                                element['price'] = material.precio_venta 
                                
                        elif material.topado_por.name == municipio or material.topado_por.name == 'Nacional' or material.topado_por.name == 'Provincial':
                            element['topado_por'] = material.topado_por.name
                            element['price'] = material.precio_venta 

            if existe == False and ( material.topado_por.name == municipio or material.topado_por.name == 'Nacional' or material.topado_por.name == 'Provincial' )  :
                obj_construccion.append({
                    'name': material_name ,
                    'price': material.precio_venta ,
                    'topado_por': material.topado_por.name
                })
        if obj_construccion :
            dicc['Construccion'] = obj_construccion

    #Agricultura
        for producto in agricultura:
            existe = False
           
            for element in obj_agricultura: 
                if producto.producto == element['name']:
                    existe =True
                    if element['topado_por'] == 'Nacional':
                        break
                    else:
                        if  element['topado_por']  == 'Provincial':
                            if producto.topado_por.name == 'Nacional':
                                element['topado_por'] = producto.topado_por.name
                                element['type'] = producto.tipo 
                                element['name'] = producto.producto 
                                element['docenas'] = producto.compra_productor 
                                element['diametro'] = producto.venta_mayorista
                                element['precio'] = producto.venta_minorista
                        
                        elif producto.topado_por.name == municipio or producto.topado_por.name == 'Nacional' or producto.topado_por.name == 'Provincial'  :
                            element['topado_por'] = producto.topado_por.name
                            element['type'] = producto.tipo 
                            element['name'] = producto.producto 
                            element['compra_productor'] = producto.compra_productor 
                            element['venta_mayorista'] = producto.venta_mayorista
                            element['venta_minorista'] = producto.venta_minorista
            
            if existe == False and ( producto.topado_por.name == municipio or producto.topado_por.name == 'Nacional' or producto.topado_por.name == 'Provincial' )  :
                obj_agricultura.append({
                    'type': producto.tipo ,
                    'name':  producto.producto ,
                    'compra_productor': producto.compra_productor ,
                    'venta_mayorista': producto.venta_mayorista ,
                    'venta_minorista': producto.venta_minorista,
                    'topado_por': producto.topado_por.name  ,
                })

            
        if obj_agricultura :
            list_agricultura = []
            viandas = ['Viandas','Hortalizas','Otras Hortalizas','Citricos y Frutas','Granos']
            for item in viandas :
                products = []
                for produc in obj_agricultura :
                    if produc['type'] == item :
                        products.append({
                            'name':  produc['name'] ,
                            'compra_productor': produc['compra_productor'] ,
                            'venta_mayorista': produc['venta_mayorista'] ,
                            'venta_minorista': produc['venta_minorista'],
                            'topado_por': produc['topado_por']  ,
                        })

                if products :
                    list_agricultura.append({
                        'type': item,
                        'products':products
                    })
            if list_agricultura :
                dicc['Agricultura'] = list_agricultura
        
    #Cerdo
        for parte in cerdo:
            existe = False
            
            for element in obj_cerdo : 
                if parte.producto == element['name']:
                    existe =True
                    if element['topado_por'] == 'Nacional':
                        break
                    else:
                        if  element['topado_por']  == 'Provincial':
                            if parte.topado_por.name == 'Nacional':
                                element['topado_por'] = parte.topado_por.name
                                element['price'] = parte.precio 
                                
                        elif parte.topado_por.name == municipio or parte.topado_por.name == 'Nacional' or parte.topado_por.name == 'Provincial':
                            element['topado_por'] = parte.topado_por.name
                            element['price'] = parte.precio 

            if existe == False and ( parte.topado_por.name == municipio or parte.topado_por.name == 'Nacional' or parte.topado_por.name == 'Provincial' )  :
                obj_cerdo.append({
                    'name': parte.producto ,
                    'price': parte.precio ,
                    'topado_por': parte.topado_por.name
                })

        if obj_cerdo :
            dicc['Cerdo'] = obj_cerdo

    #Transporte
        for tramo in tranporte:
            existe = False
            
            for element in obj_transporte : 
                if tramo.tramo == element['name']:
                    existe =True
                    if element['topado_por'] == 'Nacional' and element['Municipio'] == municipio:
                        break
                    else:
                        if  element['topado_por']  == 'Provincial' and element['Municipio'] == municipio:
                            if tramo.topado_por.name == 'Nacional':
                                element['topado_por'] = tramo.topado_por.name
                                element['Municipio'] = tramo.municipio
                                element['name'] = tramo.tramo 
                                element['km'] = tramo.km 
                                element['triciclo'] = tramo.triciclo 
                                element['auto'] = tramo.auto 
                                element['auto_y_jeep'] = tramo.auto_y_jeep 
                                element['panel_y_micro'] = tramo.panel_y_micro 
                                element['camioneta'] = tramo.camioneta 
                                element['camino'] = tramo.camino
                                                                
                        elif tramo.municipio == municipio and (tramo.topado_por.name == municipio or tramo.topado_por.name == 'Nacional' or tramo.topado_por.name == 'Provincial'):
                            element['topado_por'] = tramo.topado_por.name
                            element['Municipio'] = tramo.municipio
                            element['name'] = tramo.tramo 
                            element['km'] = tramo.km 
                            element['triciclo'] = tramo.triciclo 
                            element['auto'] = tramo.auto 
                            element['auto_y_jeep'] = tramo.auto_y_jeep 
                            element['panel_y_micro'] = tramo.panel_y_micro 
                            element['camioneta'] = tramo.camioneta 
                            element['camino'] = tramo.camino 

            if existe == False and tramo.municipio == municipio and ( tramo.topado_por.name == municipio or tramo.topado_por.name == 'Nacional' or tramo.topado_por.name == 'Provincial' )  :
                obj_transporte.append({
                    'Municipio': tramo.municipio,
                    'name': tramo.tramo ,
                    'km': tramo.km ,
                    'triciclo': tramo.triciclo ,
                    'auto': tramo.auto ,
                    'auto_y_jeep': tramo.auto_y_jeep ,
                    'panel_y_micro': tramo.panel_y_micro ,
                    'camioneta': tramo.camioneta ,
                    'camino': tramo.camino ,
                    'topado_por' :tramo.topado_por.name
                })

        if obj_transporte :
            dicc['Transporte'] = obj_transporte
        return  Response(dicc)