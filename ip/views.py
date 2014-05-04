from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from ip.models import Address
from django.utils import timezone
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse("Hello, world. You're at the ip index.")

def list(request):
    list = Address.objects.order_by('-id').all()[:5]
    return render_to_response('address_list.html', {'ip_list': list})

def add(request, name, ip):
    p = Address(name = name, ip = ip, time = timezone.now())
    p.save()
    return HttpResponse("SUCCESS:name = " + name + ",ip = "  + ip )
