from django.shortcuts import render, redirect

from glamping_project import services
from .models import Service

def listar_services(request):
    Service_list = Service.objects.all()
    return render(request, 'services/index.html', {'service_list': Service_list})

def cambiar_estado_servicio(request, service_id):
    Services = Service.objects.get(pk=service_id)
    services.status = not Service.status
    services.save()
    return redirect('listar_services')
