from urllib.parse import quote

from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from web.forms import ContactForm
from web.models import Banner, Blog, Product, Testimonial, FAQ, Logo


def index(request):
    testimonials = Testimonial.objects.all()
    blogs = Blog.objects.all()
    banners = Banner.objects.all()
    products = Product.objects.all()
    faqs = FAQ.objects.all()
    logos = Logo.objects.all()
    context = {
        "is_index": True,
        "testimonials": testimonials,
        "blogs": blogs,
        "banners": banners,
        "products": products,
        "faqs":faqs,
        "logos":logos,
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
        print("POST Data:", request.POST)  # Log POST data for debugging
        if contact_form.is_valid():
            data = contact_form.save(commit=False)
            print("Valid Form Data:", data)  # Log valid form data
            data.save()

            # Send Email
            subject = "Enquiry Form Submission"
            message = (
                f"Name: {data.name}\n"
                f"Email: {data.email}\n"
                f"Phone: {data.number}\n"
                f"Subject: {data.subject}\n"
                f"Message: {data.message}\n"
            )
            from_email = "mdlajrahman016@gmail.in"
            recipient_list = ["mdlajrahman016@gmail.in"]

            try:
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                print("Email sent successfully!")  # Log email success
            except Exception as e:
                print(f"Email sending failed: {e}")  # Print error to terminal
                return JsonResponse({"status": "error", "message": f"Email sending failed: {str(e)}"})

            # Generate WhatsApp URL
            whatsapp_message = (
                f"Name: {data.name}\n"
                f"Email: {data.email}\n"
                f"Phone: {data.number}\n"
                f"Subject: {data.subject}\n"
                f"Message: {data.message}\n"
            )
            whatsapp_api_url = "https://api.whatsapp.com/send"
            phone_number = "+917902855554"
            encoded_message = quote(whatsapp_message)
            whatsapp_url = f"{whatsapp_api_url}?phone={phone_number}&text={encoded_message}"
            print("Generated WhatsApp URL:", whatsapp_url)  # Log WhatsApp URL
            return JsonResponse({"status": "success", "whatsapp_url": whatsapp_url})

        else:
            # Log form errors to the terminal
            print("Form Validation Errors:", contact_form.errors)
            # Form validation error response
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

    print("Invalid request method.")
    return JsonResponse({"status": "error", "message": "Invalid request method."})