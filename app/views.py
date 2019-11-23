from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pet

@login_required(login_url='/login/')
def register_pet(request):
    pet_id = request.GET.get('id')
    if pet_id:
        pet = Pet.objects.get(id = pet_id)
        if pet.user == request.user:
            return render(request, 'register-pet.html', {'pet': pet})
    return render(request, 'register-pet.html')

@login_required(login_url='/login/')
def set_pet(request):
    cidade = request.POST.get('cidade')
    email = request.POST.get('email')
    fone = request.POST.get('fone')
    descricao = request.POST.get('descricao')
    imagem = request.FILES.get('file')
    pet_id = request.POST.get('pet-id')
    user = request.user 
    if pet_id:
        pet = Pet.objects.get(id=pet_id)
        if user == pet.user:
            pet.email = email
            pet.fone = fone
            pet.cidade = cidade
            pet.descricao = descricao
            if imagem:
                pet.imagem = imagem
            pet.save()
    else:
        pet = Pet.objects.create(email=email, fone=fone, descricao=descricao, imagem=imagem, cidade=cidade, user=user)
    url = '/pet/detail/{}/'.format(pet.id)
    return redirect(url)

@login_required(login_url='/login/')
def delete_pet(request, id):
    pet = Pet.objects.get(id=id)
    if pet.user == request.user:
        pet.delete()
    return redirect('/')

@login_required(login_url='/login/')
def list_all_pets(request):
    pet = Pet.objects.filter(active=True)
    return render(request, 'list.html', {'pet':pet})

def list_user_pets(request):
    pet = Pet.objects.filter(active=True, user=request.user)
    return render(request, 'list.html', {'pet':pet})

def pet_detail(request, id):
    pet = Pet.objects.get(active=True, id=id)
    return render(request, 'pet.html', {'pet':pet})

def logout_user(request):
    logout(request)
    return redirect('/login/')

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e senha inválidos. Tente novamente')
    return redirect('/login/')

