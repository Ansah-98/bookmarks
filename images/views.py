from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Image
from django.forms import ModelForm
from .forms import ImageCreation
from django.contrib import messages


@login_required
def image_creation(request):
    if request.method == 'POST':
        image_form =    ImageCreation(data = request.POST)
        if image_form.is_valid():
            cd = image_form.cleaned_data
            new_item = image_form.save(commit=False)
            new_item.user = request.user    
            new_item.save()
            messages.success('image added successfully')
            return redirect(new_item.get_absolute_url())
    

    else :
        image_form = ImageCreation()
    return render(request, 'images/create.html',{'form':image_form})

def image_detail(request,id,slug):
    image = Image.objects.get(pk =id)    
    true = False
    if image is not None:
        true  = True
        
    return render(request,'images/detail.html', {'image': image,'true':true,'section':'images'})







