from django.shortcuts import render, redirect, reverse
from blog.models import ProgressPost
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AddPostForm
from user_profiles.models import UserProfile


# Create your views here.
def progress(request):

    default_posts = ProgressPost.objects.all()
    sorted_posts = default_posts.order_by('-date')

    context = {
        'progress_posts': sorted_posts,
    }

    return render(request, 'blog/blog.html', context)


@login_required
def add_post(request):
    """ View for adding posts to the store blog """
    if not request.user.is_superuser:
        messages.error(request, 'Oops, you need to be authorised to do that.')
        return redirect(reverse('progress'))

    if request.method == 'POST':
        author = UserProfile.objects.get(user=request.user)
        form_data = {
            'author': author,
            'post_title': request.POST['post_title'],
            'post_content': request.POST['post_content'],
            'image': request.FILES['image'],
        }

        form = AddPostForm(form_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post successfully published.')
            return redirect(reverse('progress'))
        else:
            messages.error(request, 'Unable to add post. Ensure there are no errors in the form.')
    else:
        form = AddPostForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
