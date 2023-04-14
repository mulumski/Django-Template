from django.shortcuts import render
from .forms import ProductSubmissionForm, MemberRegistrationForm


def index(request):
    return render(request, 'index.html')


def portfolio(request):
    return render(request, 'portfolio-details.html')


def inner(request):
    return render(request, 'inner-page.html')


def product_submission(request):
    submit_button = request.POST.get("btn-reg")
    name = ''
    product_type = ''
    product_make = ''
    form = ProductSubmissionForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        product_type = form.cleaned_data.get('product_type')
        product_make = form.cleaned_data.get('product_make')
    context = {'form': form, 'submit_button': submit_button, 'name': name,
               'product_type': product_type, 'product_make': product_make}

    return render(request, 'product-submission.html', context)


def MemberRegistrationForm(request):
    submit_button = request.POST.get("btn-reg")
    name = ''
    email = ''
    password = ''
    form = MemberRegistrationForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
    context = {'form': form, 'submit_button': submit_button, 'name': name,
               'email': email, 'password': password}
    return render(request, 'register.html', context)
