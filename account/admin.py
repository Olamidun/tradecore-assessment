from .models import UserAccount
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Register your models here.

class UserAccountAdmin(UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ['email', 'date_joined', 'is_admin', 'is_staff', 'is_active', 'country', 'city', 'country_code', 'continent', 'timezone', 'region', 'name_of_holiday', 'holiday_type', 'holiday_date', 'weekday']
    search_fields = ['email',]
    readonly_fields = ['date_joined',]

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'country', 'city', 'country_code', 'continent', 'timezone', 'region', 'name_of_holiday', 'holiday_type', 'holiday_date', 'weekday', 'password',)}),
        ('Personal info', {'fields': ('date_joined',)}),
        ('Permissions', {'fields': ('is_admin', 'is_verified', 'is_active', 'is_staff',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',),
        }),
        ('Permissions', {'fields': ('is_admin', 'is_verified', 'is_active', 'is_staff', )}),
    )
    ordering = ('email', )

admin.site.register(UserAccount, UserAccountAdmin)
