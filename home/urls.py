from django.urls import path
from . import views

urlpatterns =[path('home', views.homepage, name='homepage'),
              path('About_Us', views.aboutpage, name='aboutpage'),
              path('Services', views.servicespage, name='servicespage'),
              path('Products', views.productspage, name='productspage'),
              path('Contact', views.contactpage, name='contactpage'),
              path('Why_Us', views.whypage, name='whypage'),
              path('Careers', views.careerpage, name='careerpage'),
              path('thanks', views.careerpage, name='careerpage'),
              path('Careers/<slug:slug>', views.career_detail, name='career_detail'),
              path('Blog', views.blogpage, name='blogpage'),
              path('Blog/<slug:slug>', views.blog_detail, name='blog_detail'),
              path('Pilot_Training', views.pilotproductpage, name='pilotproductpage'),
              path('Cabin_Crew_Training', views.cabincrewproductpage, name='cabincrewproductpage'),
              path('Engine_Inspection_Training', views.engineinspectionproductpage, name='engineinspectionproductpage'),
              path('Catalogue_Download', views.cataloguepage, name='cataloguepage'),]