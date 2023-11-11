from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from purchase_request.models import *
from import_export import resources

# Register your models here.

class RequestOrderResource(resources.ModelResource):
    class Meta:
        model = RequestOrder


class RequestOrderAdmin(ImportExportModelAdmin):
    resource_class = RequestOrderResource
admin.site.register(RequestOrder, RequestOrderAdmin)





class ItemRequestResource(resources.ModelResource):
    class Meta:
        model = ItemRequest

class ItemRequestAdmin(ImportExportModelAdmin):
    resource_class = ItemRequestResource
admin.site.register(ItemRequest, ItemRequestAdmin)

class RequestOrderAproveResource(resources.ModelResource):
    class Meta:
        model = RequestOrderAprove
class RequestOrderAproveAdmin(ImportExportModelAdmin):
    resource_class = RequestOrderAproveResource
admin.site.register(RequestOrderAprove, RequestOrderAproveAdmin)