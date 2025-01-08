from django.contrib import admin

from web.models import FAQ, Banner, Blog, Contact, Product, Testimonial

# Register your models here.


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "content")


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question",)


# @admin.register(Meta)
# class MetaAdmin(admin.ModelAdmin):
#     list_display = ("meta_title", "page")


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title",)
