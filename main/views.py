from django.shortcuts import render, redirect   
from main.forms import ProductEntryForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
def show_main(request):
    product_entries = Product.objects.all()
    context = {
        'name' : 'Jeremi Felix Adiyatma',
        'npm' : '2306219575',
        'kelas' : 'PBP B',
        'item' : 'Gitar Michael Jackson',
        'description': 'This was the guitar Michael Used on his tour in early 2009 months before he died',
        'satisfaction': product_entries
    }

    return render(request, "main.html", context)
def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_xml_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
# Create your views here.
