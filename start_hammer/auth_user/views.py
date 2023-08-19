from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserCodeForm, UserProfileForm
from .models import Enter
import random
def register(request):
    if request.method == 'POST':
        person=Enter()
        form=UserRegisterForm(request.POST)
        person.inv_code=gener_inv_code()
        person.phone_number=request.POST.get("phone_number")
        if form.is_valid():
            person.save()
        return redirect('code-enter')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def code(request):
    if request.method == 'POST':
        
        form = UserCodeForm(request.POST)
        
        return redirect('profile')
    else:
        print(request.GET)
        form = UserCodeForm()
    return render(request, 'code.html', {'form': form})

def gener_inv_code():
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password =''
    for i in range(6):
        password += random.choice(chars)
    return password

def profile(request):
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Перенаправьте на страницу просмотра профиля
    else:
        form = UserProfileForm()
    
    context = {'form': form}
    return render(request, 'profile.html', context)