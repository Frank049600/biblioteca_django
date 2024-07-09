from django.contrib import admin
from .models import acervo_model
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# class acervo_admin(admin.ModelAdmin):
#     list_display = ('titulo','autor','editorial','colocacion','adqui','estado','formato')
#     search_fields = ('titulo','colocacion','message')
#     list_filter = ('titulo','colocacion','estado','formato')

admin.site.register(acervo_model, ImportExportModelAdmin)