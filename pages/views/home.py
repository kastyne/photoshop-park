from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {
        "courses": [{
            "name": "Photoshop Basics",
            "image": "",
            "discription": "Learn"
        }]
    })