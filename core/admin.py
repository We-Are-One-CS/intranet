from django.contrib import admin

from .models import User, Category, Structure, CotisationType, Event

admin.site.site_header = 'WAO Dashboard'
admin.site.site_title = 'WAO Admin'
admin.site.index_title = ''


class MyUserAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'last_name', 'first_name', 'telephone', 'is_enterprise', 'is_superuser', 'is_active', 'photo')
    list_filter = ('is_enterprise', 'is_superuser')
    list_editable = ('is_superuser', 'is_enterprise', 'is_active')
    search_fields = ('last_name', 'first_name', 'email')


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'description', 'price', 'capacity', 'type', 'photo')


admin.site.register(User, MyUserAdmin)
admin.site.register(Category)
admin.site.register(Structure)
admin.site.register(CotisationType)
admin.site.register(Event, EventAdmin)
