from web.forms import ContactForm


def pop_contact(request):
    form = ContactForm()
    return {"form": form}
