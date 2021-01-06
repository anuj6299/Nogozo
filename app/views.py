from django.shortcuts import render, get_object_or_404


def service(request):
    context = {
     }
    return render(request, 'app/service.html', context)


def shoplist(request):
    data = 10
    context = {
        'data' : range(data)
     }
    return render(request, 'app/shoplist.html', context)

