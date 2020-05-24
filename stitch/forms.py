from django import forms

class ImageForm(forms.Form):
    image_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label="Images from left to right")
