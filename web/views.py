from urllib.parse import quote

from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from web.forms import ContactForm
from web.models import Banefit, Banner, Blog, Product, Testimonial, FAQ


def index(request):
    testimonials = Testimonial.objects.all()
    blogs = Blog.objects.all()
    banners = Banner.objects.all()
    products = Product.objects.all()
    benefits = Banefit.objects.all()
    faqs = FAQ.objects.all()
    context = {
        "is_index": True,
        "testimonials": testimonials,
        "blogs": blogs,
        "banners": banners,
        "products": products,
        "benefits": benefits,
        "faqs":faqs,
    }
    return render(request, "web/index.html", context)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    other_blogs = Blog.objects.exclude(slug=slug)
    context = {"blog": blog, "other_blogs": other_blogs}
    return render(request, "web/blog-details.html", context)


def pop_contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            data = contact_form.save(commit=False)
            data.save()

            subject = "Enquiry Form Submission"
            message = (
                f"Name: {data.name}\n"
                f"Email: {data.email}\n"
                f"Phone: {data.number}\n"
                f"Subject: {data.subject}\n"
                f"Message: {data.message}\n"
            )
            from_email = "midhlajrahman26@gmail.com"
            recipient_list = ["midlajrahman016@gmail.com"]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            whatsapp_message = (
                f"Name: {data.name}\n"
                f"Email: {data.email}\n"
                f"Phone: {data.number}\n"
                f"Subject: {data.subject}\n"
                f"Message: {data.message}\n"
            )
            whatsapp_api_url = "https://api.whatsapp.com/send"
            phone_number = "+919037126305"
            encoded_message = quote(whatsapp_message)
            whatsapp_url = (
                f"{whatsapp_api_url}?phone={phone_number}&text={encoded_message}"
            )

            return JsonResponse({"status": "success", "whatsapp_url": whatsapp_url})

        else:
            error_messages = {
                field: contact_form.errors[field][0] for field in contact_form.errors
            }
            return JsonResponse(
                {
                    "status": "error",
                    "title": "Form Validation Error",
                    "message": error_messages,
                }
            )

    return JsonResponse({"status": "error", "message": "Invalid request method."})
