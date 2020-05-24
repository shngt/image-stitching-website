from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageForm
from django.views.generic.edit import FormView
from .imagestitching import fetch_images, stitch_images
from django.core.files.storage import FileSystemStorage
import shutil
import cv2 as cv

# Create your views here

def SuccessView(request):
    return render(request, 'success.html')

class InputView(FormView):
    form_class = ImageForm
    template_name = 'index.html' 
    success_url = 'success'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('image_field')
        if form.is_valid():
            shutil.rmtree("media")
            fs = FileSystemStorage()
            for f in files:
                fs.save(f.name, f)
            images = fetch_images("media")
            stitched = stitch_images(images)
            cv.imwrite("stitch/static/stitched.jpg", stitched)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
