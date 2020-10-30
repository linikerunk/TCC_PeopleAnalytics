from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import SubCategory, Category, Ticket, TicketHistory


@admin.register(SubCategory)
class SubCategoryAdmin(ImportExportModelAdmin):
    list_display = ['name']
    verbose_name = "SubCategoria"
    verbose_name_plural = "SubCategorias"


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['name']
    verbose_name = "Categoria"
    verbose_name_plural = "Categorias"


@admin.register(Ticket)
class TicketAdmin(ImportExportModelAdmin):
    list_display = ['text', 'awnser', 'date', 'final_date', 'finish',
                    'file_upload', 'employee', 'category', 'subcategory']
    verbose_name = "Chamados"
    verbose_name_plural = "Chamados"


@admin.register(TicketHistory)
class TicketHistoryAdmin(ImportExportModelAdmin):
    list_display = ['date_message', 'message', 'ticket', 'employee']
    verbose_name = "Historico_de_Chamado"
    verbose_name_plural = "Historico_de_Chamados"