from django.db import models
from ckeditor.fields import RichTextField

# About Page #
class team_dynamic(models.Model):

    image = models.ImageField(upload_to='team-pics', null=True, blank=True)
    name = models.CharField(max_length=100,null=False)
    designation = models.CharField(max_length=100, null=False)
    linkedin_url = models.CharField(max_length=500, null=False)

# Carrer Page #
class career_content_dynamic(models.Model):

    job_post = models.CharField(max_length=100,null=False)
    slug = models.SlugField(null=True, blank=True)
    job_department = models.CharField(max_length=500,null=True, blank=True)
    job_requirements = RichTextField(null=True, blank=True)
    job_years_exp = models.CharField(max_length=100,null=False)
    job_location = models.CharField(max_length=100,null=False)
    job_responsibilities = RichTextField(null=True, blank=True)
    job_description = RichTextField(null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-date_time']

# Blog Page #
class blog_content_dynamic(models.Model):

    image = models.ImageField(upload_to='blog-pics', null=True, blank=True)
    topic_name = models.CharField(max_length=100,null=False)
    slug = models.SlugField(null=True, blank=True)
    topic_abstract = models.CharField(max_length=500,null=True, blank=True)
    topic_description = RichTextField(blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-date_time']
