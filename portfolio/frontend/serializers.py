from rest_framework import serializers
from .models import Menu, SubMenu, Section, SectionContent
from .models import ContactMessage

class SectionContentSerializer(serializers.ModelSerializer):
    project_type_display = serializers.CharField(source='get_project_type_display', read_only=True)

    class Meta:
        model = SectionContent
        fields = [
            'id',
            'project_title',
            'project_type',
            'project_type_display',
            'project_description',
            'project_icon',
            'order',
            'github_link',
            'live_demo',
        ]


class SectionSerializer(serializers.ModelSerializer):
    contents = SectionContentSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = [
            'id',
            'title',
            'sub_title',
            'description',
            'image',
            'background_color',
            'menu',
            'submenu',
            'order',
            'contents'
        ]


class SubMenuSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()

    class Meta:
        model = SubMenu
        fields = ['id', 'title', 'order', 'sections']

    def get_sections(self, obj):
        sections = Section.objects.filter(submenu=obj).order_by('order')
        return SectionSerializer(sections, many=True).data


class MenuSerializer(serializers.ModelSerializer):
    submenus = SubMenuSerializer(many=True, read_only=True)
    sections = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ['id', 'title', 'order', 'submenus', 'sections', 'is_button']

    def get_sections(self, obj):
        sections = Section.objects.filter(menu=obj, submenu__isnull=True).order_by('order')
        return SectionSerializer(sections, many=True).data



class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'location', 'budget', 'subject', 'message', 'created_at']