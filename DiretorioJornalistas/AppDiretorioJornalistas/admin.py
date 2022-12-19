from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from AppDiretorioJornalistas.models.usuarios import Jornalista, User
# Register your models here.
admin.site.register(Jornalista)
# admin.site.register(User, UserAdmin)

# @admin.register(User)
# class UserAdmin(DjangoUserAdmin):
#     """Define admin model for custom User model with no email field."""

#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name')}),
#         (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
#                                        'groups', 'user_permissions')}),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2'),
#         }),
#     )
#     list_display = ('email', 'first_name', 'last_name', 'is_staff')
#     search_fields = ('email', 'first_name', 'last_name')
#     ordering = ('email',)
