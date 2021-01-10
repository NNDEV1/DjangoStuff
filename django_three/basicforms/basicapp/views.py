from django.shortcuts import render, redirect
from .forms import UserForm

# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')

def hi(request):
    return render(request, 'basicapp/thank_you.html')

def thank_you_page(request):
    return render(request, 'basicapp/thank_you_page.html')

def forms_page(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return thank_you_page(request)
        else:
            print('FORM INVALID')

    return render(request, 'basicapp/forms_page.html', {'form':form})
