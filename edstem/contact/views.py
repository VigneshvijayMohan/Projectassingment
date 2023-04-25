from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContactForm
# Create your views here.
def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "confirmation.html")
        
    form = ContactForm()
    dict_form = {
        "form" : form
    }
    return render(request,"index.html", dict_form)