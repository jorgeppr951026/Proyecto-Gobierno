from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class FloresResource(resources.ModelResource):
    class Meta:
        model = Flores


class FloresAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = FloresResource


class CoronasResource(resources.ModelResource):
    class Meta:
        model = Coronas


class CoronasAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = CoronasResource


class ConstruccionResource(resources.ModelResource):
    class Meta:
        model = Construccion
class ConstruccionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = ConstruccionResource


class TransporteResource(resources.ModelResource):
    class Meta:
        model = Transporte
class TransporteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = TransporteResource


class AgriculturaResource(resources.ModelResource):
    class Meta:
        model = Agricultura
class AgriculturaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = AgriculturaResource


class CerdoResource(resources.ModelResource):
    class Meta:
        model = Cerdo
class CerdoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = CerdoResource


class TopadoResource(resources.ModelResource):
    class Meta:
        model = Topado
class TopadoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = TopadoResource

###########################
admin.site.register(Flores, FloresAdmin)
admin.site.register(Coronas, CoronasAdmin)
admin.site.register(Construccion, ConstruccionAdmin)
admin.site.register(Transporte, TransporteAdmin)
admin.site.register(Agricultura, AgriculturaAdmin)
admin.site.register(Cerdo, CerdoAdmin)
admin.site.register(Topado, TopadoAdmin)






