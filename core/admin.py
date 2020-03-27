from django.contrib import admin

from .models import User, Category, Structure, MembershipType, Event, SubjectImpact, Company

admin.site.site_header = 'WAO Dashboard'
admin.site.site_title = 'WAO Admin'
admin.site.index_title = ''


class MyUserAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'first_name', 'last_name', 'telephone', 'membership_paid', 'company', 'is_superuser',
        'is_active')
    list_filter = ('company', 'is_superuser', 'membership_paid')
    list_editable = ('is_superuser', 'company', 'is_active', 'membership_paid')
    search_fields = ('last_name', 'first_name', 'email')


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'description', 'price', 'capacity', 'type', 'photo')


admin.site.register(User, MyUserAdmin)
admin.site.register(Category)
admin.site.register(Structure)
admin.site.register(MembershipType)
admin.site.register(SubjectImpact)
admin.site.register(Event, EventAdmin)
admin.site.register(Company)
# admin.site.register(Yearbook) # Uncomment when Yearbook model is ready
# admin.site.register(SelfDevelopmentProgram) # Uncomment when SelfDevelopmentProgram model is ready
