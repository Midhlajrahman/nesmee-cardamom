from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse_lazy



class Banner(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=180)
    image = models.ImageField(upload_to="banner/")
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts' 
        
        
class Testimonial(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name} - {self.position}"
    
    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        
    

class FAQ(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
    
    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
    
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    category = models.CharField(max_length=100)
    date = models.DateField()
    description = HTMLField()
    image = models.ImageField(upload_to='blog/')
    
    def get_absolute_url(self):
        return reverse_lazy('web:blog_detail', kwargs={'slug': self.slug})

    
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
        verbose_name = 'Meta'
        verbose_name_plural = 'Metas'



class Product(models.Model):
    title = models.CharField(max_length=100)
    