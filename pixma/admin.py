
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Course,Department,TableContent

admin.site.register(Course)
admin.site.register(Department)
#admin.site.register(TableContent)
@admin.register(TableContent)
class TableContentAdmin(ImportExportModelAdmin):
    pass
