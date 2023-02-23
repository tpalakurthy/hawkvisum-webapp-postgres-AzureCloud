from django.shortcuts import render


def error_404(request, exception):
        data = {}
        return render(request,'404.html', data)

def error_500(request, *args):
        data = {}
        return render(request,'500.html', data)