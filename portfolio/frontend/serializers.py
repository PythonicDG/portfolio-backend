from rest_framework import serializers
from .models import Menu, SubMenu, Section, SectionContent

class SectionContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionContent
        fields = ['id', 'content_title', 'content_description', 'content_icon', 'order']

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
        fields = ['id', 'title', 'order', 'submenus', 'sections']

    def get_sections(self, obj):
        sections = Section.objects.filter(menu=obj, submenu__isnull=True).order_by('order')
        return SectionSerializer(sections, many=True).data
