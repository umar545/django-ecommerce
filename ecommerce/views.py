from django.shortcuts import render
from django.views import View
from .models import Item , Order , OrderItem
# Create your views here.
class HomeView(View):
    def get(self , request , *args, **kwargs):
        context = {
            'items' : Item.objects.all(),
        }
        return render(request, './index.html' , context=context)
