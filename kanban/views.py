from django.shortcuts import render
from .models import Item

# Create your views here.


def get_kanban(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'kanban/kanban.html', context)
