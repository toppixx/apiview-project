from django.contrib import admin
from . import models

admin.site.register(models.NfcListOfUsers)
admin.site.register(models.NfcDoorGroup)
admin.site.register(models.NfcDoor)
admin.site.register(models.NfcKey)



#class FlatPageAdmin(admin.ModelAdmin):#
#    fieldsets=(#
#    (None,{
#    'fields' : ('url', 'titel', 'content', 'sites')}),
#    ('Advanced options' ,{'classes' : ('collapse',),
#    'fields' : ('registration_required', 'template_name'),
#    }),
#    )


#from django.contrib import admin
#from django.utils.translation import ugettext_lazy as _


#class FlatPageAdmin(admin.ModelAdmin):
#    fieldsets = (
#        (None, {'fields': ('door_name', 'door_nfc_tag_list')}),
#        (('Advanced options'), {
#            'classes': ('collapse', ),
#            'fields': ('door_name',
#                'door_:nfc_tag_list',
#            ),
#        }),
#    )
#    list_display = ['door_name', 'door_nfc_tag_list']
#    list_filter = ['door_name', 'door_nfc_tag_list']
#
#admin.site.register(DoorNfcTagModel, FlatPageAdmin)
