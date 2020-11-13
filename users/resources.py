from import_export import resources
from .models import *

class CostCenterAdminResource(resources.ModelResource):

    class Meta:
        model   =   CostCenter
        exclude = ('id',)