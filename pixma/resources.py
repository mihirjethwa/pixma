from import_export import resources
from .models import TableContent

class TableContentResource(resources.ModelResource):
    class Meta:
        model = TableContent
