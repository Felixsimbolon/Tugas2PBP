from django.shortcuts import render
def show_main(request):
    context = {
        'Name' : 'Gitar Michael Jackson',
        'Price': 6000000,
        'Description': 'This was the guitar Michael Used on his tour in early 2009 months before he died'
    }

    return render(request, "main.html", context)
# Create your views here.
