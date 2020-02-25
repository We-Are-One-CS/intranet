from django.contrib import admin

from .models import User, UserCategory, UserStructure, UserCotisationType

admin.site.site_header = 'WAO Dashboard'
admin.site.site_title = 'WAO Admin'
admin.site.index_title = ''


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'last_name', 'first_name', 'telephone', 'is_enterprise', 'is_superuser', 'is_active')
    list_filter = ('is_enterprise', 'is_superuser')
    list_editable = ('is_superuser', 'is_enterprise')
    search_fields = ('last_name', 'first_name', 'email')


admin.site.register(User, MyUserAdmin)
admin.site.register(UserCategory)
admin.site.register(UserStructure)
admin.site.register(UserCotisationType)
