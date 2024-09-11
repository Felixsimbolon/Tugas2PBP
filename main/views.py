from django.shortcuts import render
def show_main(request):
    context = {
        'name' : 'Jeremi Felix Adiyatma',
        'npm' : '2306219575',
        'kelas' : 'PBP B',
        'item' : 'Gitar Michael Jackson',
        'price': 6000000,
        'description': 'This was the guitar Michael Used on his tour in early 2009 months before he died'
    }

    return render(request, "main.html", context)
# Create your views here.
