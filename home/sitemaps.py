from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import blog_content_dynamic


class blog_sitemap(Sitemap):

    priority = 0.8
    changefreq = "daily"

    def items(self):
        return blog_content_dynamic.objects.all()

class staticviewssitemap(Sitemap):
    priority = 0.9
    changefreq = "daily"

    def items(self):
        return [
            'homepage',
            'aboutpage',
            'productspage',
            'servicespage',
            'contactpage',
            'careerspage',
            'whypage',
            'blogpage'
        ]
    
    def location(self, item):
        return reverse(item)