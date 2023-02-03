from django.shortcuts import redirect, render
from django.contrib.auth.models  import User
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm,UserRegistrationForm,ProfileEditForms,UserEditForm
from .models import Profile
from django.contrib import messages



@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', 
    {'section': 'dashboard'}) 
    
def userlogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'],
             password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated Successfully')
                else:
                    return HttpResponse('Disabled account')
                
            else:
                return HttpResponse("Invalid account")
    else:
        form = LoginForm()
    return render(request,'account/login.html', {'form':form} )

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/registration_done.html', {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/registration.html',{'form':user_form})
        
@login_required
def edit(request):
    print(type(request.user))
    profile = Profile.objects.get(user = request.user)
    if profile == None:
        profile_edit = ProfileEditForms()
        user_edit = UserEditForm(instance=request.user)
    elif request.method == 'POST':   
        user_edit = UserEditForm(instance = request.user , data =request.POST)
        profile_edit = ProfileEditForms(instance = profile,
                                    data = request.POST,
                                    files = request.FILES )
        
        if user_edit.is_valid() and profile_edit.is_valid():
            user_edit.save()
            profile_edit.save()
            messages.success(request,"your profile has been updated")
        else:
            messages.error(request , "error updating your profile")
    else:
        user_edit = UserEditForm(instance = request.user)
        profile_edit = ProfileEditForms(instance = profile)
    return render(request, 'account/edit_html',
                {'user_edit': user_edit,
                'profile_edit':profile_edit})