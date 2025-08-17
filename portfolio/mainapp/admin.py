from django.contrib import admin
from .models import Project, Skill, Blog, ContactMessage, Profile

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Blog)
admin.site.register(ContactMessage)
