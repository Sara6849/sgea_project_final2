from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
<<<<<<< HEAD
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.http import HttpResponse
from .models import Event, Certificate
from .forms import RegisterForm, EditProfileForm, LoginForm, EventForm
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import getSampleStyleSheet
from django.conf import settings
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from .models import Event
import os


# --- REST Framework ---
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EventSerializer, EventCreateSerializer, UserSerializer

User = get_user_model()

# -----------------------------
# Home
# -----------------------------
=======
from django.contrib.auth import login, logout, authenticate
from .models import Event, Registration
from .forms import RegisterForm, EditProfileForm, LoginForm

# Home / Página inicial
>>>>>>> d777e06a7afec3224da65659784b0ef318e76793
def home_view(request):
    events = Event.objects.all()
    return render(request, 'core/home.html', {'events': events})

<<<<<<< HEAD
# -----------------------------
# Lista eventos (web)
# -----------------------------
=======
# Lista de eventos
>>>>>>> d777e06a7afec3224da65659784b0ef318e76793
def event_list(request):
    events = Event.objects.all()
    return render(request, 'core/event_list.html', {'events': events})

<<<<<<< HEAD
# -----------------------------
# Detalhe evento (web)
# -----------------------------
@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    registered = request.user in event.participants.all()
    participants = event.participants.all()
    is_organizer = request.user.role == 'organizer'

    if request.method == 'POST':
        if 'subscribe' in request.POST and not registered:
            event.participants.add(request.user)
            messages.success(request, 'Inscrição realizada com sucesso!')
            return redirect('core:event_detail', event_id=event.id)
        elif 'unsubscribe' in request.POST and registered:
            event.participants.remove(request.user)
            messages.success(request, 'Inscrição cancelada!')
            return redirect('core:event_detail', event_id=event.id)

    return render(request, 'core/event_detail.html', {
        'event': event,
        'registered': registered,
        'participants': participants,
        'is_organizer': is_organizer,
    })

# -----------------------------
# Perfil
# -----------------------------
@login_required
def profile_view(request):
    user = request.user
    registered_events = Event.objects.filter(participants=user)
    organized_events = Event.objects.filter(organizer=user) if user.role == 'organizer' else None

    return render(request, 'core/profile.html', {
        'user': user,
        'registered_events': registered_events,
        'organized_events': organized_events,
    })

=======
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
>>>>>>> d777e06a7afec3224da65659784b0ef318e76793
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
<<<<<<< HEAD
            messages.error(request, "Corrija os erros abaixo.")
=======
            messages.error(request, "Por favor, corrija os erros abaixo.")
>>>>>>> d777e06a7afec3224da65659784b0ef318e76793
    else:
        form = EditProfileForm(instance=user)
    return render(request, 'core/edit_profile.html', {'form': form})

<<<<<<< HEAD
# -----------------------------
# Auth
# -----------------------------
=======
# Cadastro de usuário
>>>>>>> d777e06a7afec3224da65659784b0ef318e76793
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
<<<<<<< HEAD
            messages.success(request, 'Cadastro realizado!')
            return redirect('core:home')
        else:
            messages.error(request, 'Corrija os erros.')
=======
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('core:home')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
>>>>>>> d777e06a7afec3224da65659784b0ef318e76793
    else:
        form = RegisterForm()
    return render(request, 'core/signup.html', {'form': form})

<<<<<<< HEAD
=======
# Login de usuário
>>>>>>> d777e06a7afec3224da65659784b0ef318e76793
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
<<<<<<< HEAD
                messages.error(request, 'Login inválido.')
=======
                messages.error(request, 'Usuário ou senha inválidos.')
>>>>>>> d777e06a7afec3224da65659784b0ef318e76793
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})

<<<<<<< HEAD
=======
# Logout
>>>>>>> d777e06a7afec3224da65659784b0ef318e76793
@login_required
def logout_view(request):
    logout(request)
    return redirect('core:login')
<<<<<<< HEAD

# -----------------------------
# Criar evento (web)
# -----------------------------
@login_required
def create_event_view(request):
    if request.user.role != 'organizer':
        messages.error(request, "Apenas organizadores podem criar eventos.")
        return redirect('core:home')

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
=======
from .forms import EventForm

@login_required
def create_event_view(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
>>>>>>> d777e06a7afec3224da65659784b0ef318e76793
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
<<<<<<< HEAD
            messages.success(request, 'Evento criado!')
            return redirect('core:event_detail', event_id=event.id)
        else:
            messages.error(request, 'Corrija os erros.')
    else:
        form = EventForm()
    return render(request, 'core/event_form.html', {'form': form})

# -----------------------------
# Emitir Certificado
# -----------------------------
@login_required
def emitir_certificado(request, event_id, user_id):
    event = get_object_or_404(Event, id=event_id)
    user = get_object_or_404(User, id=user_id)

    if request.user.role != 'organizer':
        return HttpResponse("Sem permissão.", status=403)

    if not event.participants.filter(id=user.id).exists():
        return HttpResponse("Usuário não inscrito.", status=403)

    certificado, created = Certificate.objects.get_or_create(user=user, event=event)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="certificado_{user.username}_{event.title}.pdf"'

    c = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    c.setFillColorRGB(1, 1, 1)
    c.rect(0, 0, width, height, fill=1)
    c.setStrokeColor(colors.HexColor("#43054E"))
    c.setLineWidth(4)
    c.rect(2*cm, 2*cm, width - 4*cm, height - 4*cm, stroke=1, fill=0)

    logo_path = os.path.join(settings.BASE_DIR, 'static', 'image', 'sgea.jpg')
    if os.path.exists(logo_path):
        c.drawImage(logo_path, x=width/2 - 2*cm, y=height - 5.5*cm, width=4*cm, height=4*cm, preserveAspectRatio=True, mask='auto')

    c.setFont("Helvetica-Bold", 26)
    c.setFillColor(colors.HexColor("#43054E"))
    c.drawCentredString(width/2, height - 7*cm, "Certificado de Participação")

    styles = getSampleStyleSheet()
    style = styles['Normal']
    style.alignment = 1
    style.fontName = 'Helvetica'
    style.fontSize = 14
    style.leading = 22
    text = f"""Certificamos que <b>{user.first_name or user.username}</b> participou do evento '<b>{event.title}</b>' realizado de {event.start_date.strftime('%d/%m/%Y')} a {event.end_date.strftime('%d/%m/%Y')}, no local {event.location}."""
    para = Paragraph(text, style)
    frame = Frame(2*cm, height/2 - 3*cm, width - 4*cm, 6*cm, showBoundary=0)
    frame.addFromList([para], c)

    data_hora = datetime.now().strftime('%d/%m/%Y, às %H:%M')
    c.setFont("Helvetica-Oblique", 12)
    c.drawCentredString(width/2, 4*cm, f"Emitido em {data_hora}")
    c.drawString(width - 8*cm, 3.1*cm, "________________________")
    c.drawString(width - 7.6*cm, 2.5*cm, "Assinatura do Organizador")

    c.showPage()
    c.save()
    return response

# -----------------------------
# API REST
# -----------------------------
class EventListAPI(generics.ListAPIView):
    queryset = Event.objects.all().order_by("start_date")
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

class EventCreateAPI(generics.CreateAPIView):
    serializer_class = EventCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role != 'organizer':
            raise PermissionError("Apenas organizadores podem criar eventos.")
        serializer.save(organizer=self.request.user)

class EventRegisterAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, event_id):
        user = request.user
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({"error": "Evento não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        if event.participants.filter(id=user.id).exists():
            return Response({"error": "Usuário já inscrito neste evento."}, status=status.HTTP_400_BAD_REQUEST)

        if event.participants.count() >= event.max_participants:
            return Response({"error": "Limite de participantes atingido."}, status=status.HTTP_400_BAD_REQUEST)

        event.participants.add(user)
        event.save()
        return Response({"success": "Inscrição realizada com sucesso."}, status=status.HTTP_200_OK)
    
class EventCancelAPI(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({"error": "Evento não encontrado."}, status=404)

        if request.user not in event.participants.all():
            return Response({"error": "Você não está inscrito neste evento."}, status=400)

        event.participants.remove(request.user)
        return Response({"success": "Inscrição cancelada com sucesso."})


class MyEventsAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        events = Event.objects.filter(participants=request.user)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
=======
            messages.success(request, 'Evento criado com sucesso!')
            return redirect('core:event_detail', event_id=event.id)
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = EventForm()
    return render(request, 'core/event_form.html', {'form': form})
>>>>>>> d777e06a7afec3224da65659784b0ef318e76793
