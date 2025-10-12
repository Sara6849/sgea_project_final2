from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import Event, Registration
from .forms import RegisterForm, EditProfileForm, LoginForm

# Home / Página inicial
def home_view(request):
    events = Event.objects.all()
    return render(request, 'core/home.html', {'events': events})

# Lista de eventos
def event_list(request):
    events = Event.objects.all()
    return render(request, 'core/event_list.html', {'events': events})

# Detalhe de evento + inscrição
@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    registered = Registration.objects.filter(user=request.user, event=event).exists()

    if request.method == 'POST':
        if 'subscribe' in request.POST and not registered:
            Registration.objects.create(user=request.user, event=event)
            messages.success(request, 'Inscrição realizada com sucesso!')
            return redirect('core:event_detail', event_id=event.id)
        elif 'unsubscribe' in request.POST and registered:
            Registration.objects.filter(user=request.user, event=event).delete()
            messages.success(request, 'Inscrição cancelada com sucesso!')
            return redirect('core:event_detail', event_id=event.id)

    return render(request, 'core/event_detail.html', {'event': event, 'registered': registered})

# Perfil do usuário + eventos inscritos
@login_required
def profile_view(request):
    user = request.user
    registered_events = Event.objects.filter(registration__user=user)
    return render(request, 'core/profile.html', {'user': user, 'registered_events': registered_events})

# Editar perfil
@login_required
def edit_profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect('core:profile')
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form = EditProfileForm(instance=user)
    return render(request, 'core/edit_profile.html', {'form': form})

# Cadastro de usuário
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('core:home')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = RegisterForm()
    return render(request, 'core/signup.html', {'form': form})

# Login de usuário
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('core:home')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})

# Logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('core:login')
from .forms import EventForm

@login_required
def create_event_view(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            messages.success(request, 'Evento criado com sucesso!')
            return redirect('core:event_detail', event_id=event.id)
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = EventForm()
    return render(request, 'core/event_form.html', {'form': form})
