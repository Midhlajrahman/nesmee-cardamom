from django.contrib import admin
from web.models import *

# Register your models here.


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "message")
    
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question",)


@admin.register(Meta)
class MetaAdmin(admin.ModelAdmin):
    list_display = ("meta_title", "page")
    

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title",)