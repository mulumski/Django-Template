from django import forms

class ProductSubmissionForm(forms.Form):
    name = forms.CharField(max_length=100)
    product_type=forms.CharField()
    product_make = forms.CharField()

class MemberRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField()
    password = forms.CharField()