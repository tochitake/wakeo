from django.contrib import admin
from cms.models import Member, attribute


# admin.site.register(Member)
# admin.site.register(attribute)


class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'div', 'sex', 'team' ,'serialcd')
    list_display_links = ('id', 'name',)


admin.site.register(Member, MemberAdmin)


#class attributeAdmin(admin.ModelAdmin):
#    list_display = ('id', 'comment',)
#    list_display_links = ('id', 'comment',)
#    raw_id_fields = ('rel',)


#admin.site.register(attribute, attributeAdmin)

