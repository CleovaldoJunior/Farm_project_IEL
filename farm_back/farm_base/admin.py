from django.contrib import admin
from django.utils.translation import gettext as _

from farm_base.models import Owner, Farm

admin.site.site_header = _("Farm Project - Administration")
admin.site.site_title = _("Farm Project - Site Administration")
admin.site.index_title = _("Applications")


class OwnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'document', 'document_type', 'is_active']
    list_filter = ['document_type', 'creation_date',
                   'last_modification_date', 'is_active']
    search_fields = ['name', 'document', '=id']


class FarmAdmin(admin.ModelAdmin):
    #Included the display of municipality, owner and State on the Admin's Page.
    list_display = ['id', 'name', 'municipality', 'owner', 'state',
                    'creation_date', 'last_modification_date',
                    'is_active']
    list_filter = ['creation_date', 'last_modification_date', 'is_active']
    #Included the municipality, state and owner in the Admin's filters.
    search_fields = ['name', '=id', 'municipality', 'state', 'owner']

    readonly_fields = ["centroid", "area"]


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Farm, FarmAdmin)
