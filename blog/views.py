from django.shortcuts import render

posts = [
    {
        'title': "blog 1",
        'author': "Aniket",
        'content':"my first post",
        'date_posted':'1 Jan 2020'
    },
    {
        'title': "blog 2",
        'author': "Aniket",
        'content':"my second post",
        'date_posted':'2 Jan 2020'
    }
]

def home(request):
    context = {
        'posts':posts,
        'title':"Home"
    }
    return render(request,"blog/home.html",context)


def about(request):
    return render(request,'blog/about.html',{'title':'About'})
