from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
<<<<<<< HEAD
from .models import User, Event, Registration, Certificate

# ---------------- Admin do usuário ----------------
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('role', 'phone')}),
    )
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')

# ---------------- Admin do evento ----------------
=======
from .models import User, Event, Registration

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('role','institution','phone')}),
    )
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')

>>>>>>> d777e06a7afec3224da65659784b0ef318e76793
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'start_date', 'end_date', 'location', 'max_participants')
    list_filter = ('event_type', 'start_date')
    search_fields = ('title', 'location')

<<<<<<< HEAD
# ---------------- Admin da inscrição ----------------
=======
>>>>>>> d777e06a7afec3224da65659784b0ef318e76793
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'registered_at')
    list_filter = ('event',)
<<<<<<< HEAD

# ---------------- Admin do certificado ----------------
@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'date_issued')
    list_filter = ('event',)
=======
>>>>>>> d777e06a7afec3224da65659784b0ef318e76793
