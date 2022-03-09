from django.shortcuts import render

def index(request):
    return render(request, "index.html", {
            "courses": [
                {
                    "name": "Photoshop Basics",
                    "image": "https://images.unsplash.com/photo-1542435503-956c469947f6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1974&q=80",
                    "discription": "Learn the basics of Photoshop in this simple course"
                },
                {
                    "name": "Photoshop Basics",
                    "image": "https://images.unsplash.com/photo-1542435503-956c469947f6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1974&q=80",
                    "discription": "Learn the basics of Photoshop in this simple course"
                },
                {
                    "name": "Photoshop Basics",
                    "image": "https://images.unsplash.com/photo-1542435503-956c469947f6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1974&q=80",
                    "discription": "Learn the basics of Photoshop in this simple course"
                },
            ]
        })