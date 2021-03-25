from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ItemForm
from .models import Item


# Create your views here.

def index(request):
    item_list = Item.objects.all()
    # template = loader.get_template('food/index.html')
    params = {
        "item_list": item_list
    }

    return render(request, 'food/index.html', params)


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    params = {
        "item": item,
    }
    return render(request, "food/detail.html", params)


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, "food/item-form.html", {'form': form})


def update_item(request, id):
    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=item)

    if (form.is_valid()):
        form.save()
        return redirect('food:index')

    return render(request, "food/item-form.html", {'form': form, 'item': item})


def delete_item(request, id):
    item = Item.objects.get(pk=id)

    if (request.method == "POST"):
        item.delete()
        return redirect('food:index')

    return render(request, "food/item-delete.html", {'item': item})
