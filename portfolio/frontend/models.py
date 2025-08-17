from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class SubMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='submenus')
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.menu.title} -> {self.title}"

class Section(models.Model):
    title = models.CharField(max_length=200, null = True, blank = True)
    sub_title = models.CharField(max_length = 200, null = True, blank = True)
    description = models.CharField(max_length = 200, null = True, blank = True)
    image = models.ImageField(upload_to = "images/", null = True, blank = True)
    background_color = models.CharField(max_length = 20, null = True, blank = True)
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True, blank=True)
    submenu = models.ForeignKey(SubMenu, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class SectionContent(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='contents')
    content_title = models.TextField(blank=True, null=True)
    content_description = models.TextField(blank = True, null = True)
    content_icon = models.ImageField(upload_to='section_icons/', blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.section.title}"
