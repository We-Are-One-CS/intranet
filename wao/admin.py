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
    # TODO: Create readonly fields


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'description', 'price', 'capacity', 'photo')


class CategoryAdmin(admin.ModelAdmin):
    pass


class StructureAdmin(admin.ModelAdmin):
    pass


class MembershipTypeAdmin(admin.ModelAdmin):
    pass


class SubjectImpactAdmin(admin.ModelAdmin):
    pass


class CompanyAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, MyUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Structure, StructureAdmin)
admin.site.register(MembershipType, MembershipTypeAdmin)
admin.site.register(SubjectImpact, StructureAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Company, CompanyAdmin)
# admin.site.register(Yearbook) # Uncomment when Yearbook model is ready
# admin.site.register(SelfDevelopmentProgram) # Uncomment when SelfDevelopmentProgram model is ready
