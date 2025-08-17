from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length = 100)
    tagline = models.CharField(max_length = 200, blank = True, null = True)
    bio = models.TextField(blank = True, null = True)
    email = models.EmailField()
    phone = models.CharField(max_length = 20, blank = True, null = True)
    location = models.CharField(max_length = 100, blank = True, null = True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank = True, null = True)
    github = models.URLField(blank = True, null = True)
    linkedin = models.URLField(blank = True, null = True)
    twitter = models.URLField(blank = True, null = True)
    website = models.URLField(blank = True, null = True)

    def __str__(self):
        return self.full_name



class Project(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    github_url = models.URLField(blank = True, null = True)
    live_url = models.URLField(blank = True, null = True)
    tech_stack = models.CharField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    name = models.CharField(max_length = 100)
    level = models.CharField(max_length = 50) 

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

class Certification(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200, blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    certificate_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name