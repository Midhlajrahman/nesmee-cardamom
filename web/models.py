from django.db import models
from django.urls import reverse_lazy
from tinymce.models import HTMLField


class Banner(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=180)
    image = models.ImageField(upload_to="banner/")
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "Banner"
        verbose_name_plural = "Banners"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class Testimonial(models.Model):
    content = models.TextField()
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to="testimonial/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.position}"

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"


class FAQ(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    category = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to="blog/")
    description = HTMLField()

    def get_absolute_url(self):
        return reverse_lazy("web:blog_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Meta(models.Model):
    PAGES = [
        ("home", "Home"),
        ("about", "About"),
        ("products", "Products"),
        ("blog", "Blog"),
        ("contact", "Contact"),
    ]
    page = models.CharField(max_length=100, choices=PAGES)
    meta_title = models.CharField(max_length=100)
    meta_description = models.TextField()
    meta_keywords = models.TextField()

    def __str__(self):
        return f"{self.get_page_display()} - {self.meta_title}"

    class Meta:
        verbose_name = "Meta"
        verbose_name_plural = "Metas"


class Product(models.Model):
    image = models.ImageField(upload_to="product/")
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Logo(models.Model):
    name = models.CharField(max_length=180)
    image = models.ImageField(upload_to="logs/")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logos'
    