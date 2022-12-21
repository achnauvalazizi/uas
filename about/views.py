from django.shortcuts import render


def index(request):
    #queryset
    about = About.objects.all() # select * from about

    context = {
        'about': about
    }
    return render(request, 'about/about.html', context)