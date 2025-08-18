from django.contrib import admin
from .models import Menu, SubMenu, Section, SectionContent

@admin.register(SectionContent)
class SectionContentAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'project_type', 'section', 'order')
    list_filter = ('section', 'project_type')
    search_fields = ('project_title', 'project_description')
    ordering = ('section', 'order')


class SectionContentInline(admin.StackedInline):  
    model = SectionContent
    extra = 1
    fields = (
        'project_title', 
        'project_type', 
        'project_description', 
        'project_icon', 
        'github_link', 
        'live_demo', 
        'order'
    )
    ordering = ('order',)


class SectionInline(admin.StackedInline):  
    model = Section
    extra = 1
    fields = ('title', 'sub_title', 'description', 'image', 'background_color', 'order')
    ordering = ('order',)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'menu', 'submenu', 'order')
    list_filter = ('menu', 'submenu')
    inlines = [SectionContentInline]  
    ordering = ('order',)


@admin.register(SubMenu)
class SubMenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu', 'order')
    list_filter = ('menu',)
    inlines = [SectionInline]  
    ordering = ('order',)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    inlines = [SectionInline]  
    ordering = ('order',)
