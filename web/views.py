from django.shortcuts import get_object_or_404, render
from web.models import Testimonial, Blog, Banner, Product

def index(request):
    testimonials = Testimonial.objects.all()
    blogs = Blog.objects.all()
    banners = Banner.objects.all()
    products = Product.objects.all()
    context = {
        "is_index": True,
        "testimonials":testimonials,
        "blogs":blogs,
        "banners":banners,
        "products" : products
        }
    return render(request, "web/index.html", context)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    other_blogs = Blog.objects.exclude(slug=slug)
    context = {
        "blog":blog,
        "other_blogs":other_blogs
    }
    return render(request, "web/blog-detail.html", context)