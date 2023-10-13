from django.shortcuts import render


def prediction(request):
    return render(request, 'prediction.html')
