from django.shortcuts import render

# Create your views here.
from Bigbig.models import Guest


def bigindex(request):
    guest_list = Guest.objects.all()
    return render(request, 'bigindex.html', {'guests': guest_list})


def test(request):
    return render(request, 'test.html')
