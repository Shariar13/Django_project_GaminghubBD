from django.contrib import admin
from .models import pubg_registered_id
from .models import pubg_registered_id_10_taka
from import_export.admin import ImportExportModelAdmin
from .models import freefire_registered_id

@admin.register (pubg_registered_id)
class pubg_register_idAdmin(ImportExportModelAdmin):
    list_display = ('username','tournament_name','tournament','pubg_id_1','pubg_id_2','phone',
    'transactionid','phone_4_digit','registration_status','room_id','room_password','slot','time')
    pass


# admin.site.register (pubg_registered_id)
admin.site.register (pubg_registered_id_10_taka)
admin.site.register (freefire_registered_id)

