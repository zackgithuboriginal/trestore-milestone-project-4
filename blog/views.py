from django.shortcuts import render
from blog.models import ProgressPost

# Create your views here.
def progress(request):

    progress_posts = ProgressPost.objects.all()
    print(progress_posts)

    context = {
        'progress_posts': progress_posts,
    }

    return render(request, 'blog/blog.html', context)
