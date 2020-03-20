from django.contrib import admin

from .models import User, Category, Structure, CotisationType, Event, SubjectImpact

admin.site.site_header = 'WAO Dashboard'
admin.site.site_title = 'WAO Admin'
admin.site.index_title = ''


class MyUserAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'first_name', 'last_name', 'telephone', 'cotisation_paid', 'is_enterprise', 'is_superuser',
        'is_active')
    list_filter = ('is_enterprise', 'is_superuser', 'cotisation_paid')
    list_editable = ('is_superuser', 'is_enterprise', 'is_active', 'cotisation_paid')
    search_fields = ('last_name', 'first_name', 'email')


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'description', 'price', 'capacity', 'type', 'photo')


admin.site.register(User, MyUserAdmin)
admin.site.register(Category)
admin.site.register(Structure)
admin.site.register(CotisationType)
admin.site.register(SubjectImpact)
admin.site.register(Event, EventAdmin)
# admin.site.register(Yearbook) # Uncomment when Yearbook model is ready
# admin.site.register(SelfDevelopmentProgram) # Uncomment when SelfDevelopmentProgram model is ready
