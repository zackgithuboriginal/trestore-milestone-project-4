from django.shortcuts import render, redirect, reverse, get_object_or_404
from blog.models import ProgressPost, Comment
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


@login_required
def edit_post(request, post_id):
    """ View for editing a post in the progress blog """
    if not request.user.is_superuser:
        messages.error(request, 'Oops, you need to be authorised to do that.')
        return redirect(reverse('progress'))

    post = get_object_or_404(ProgressPost, pk=post_id)
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post successfully updated.')
            return redirect(reverse('progress'))
        else:
            messages.error(request, 'Unable to update post. Ensure there are no errors in the form.')
    else:
        form = AddPostForm(instance=post)
        messages.info(request, 'Now editing post.')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    """ View for delete a post from the progress blog """
    if not request.user.is_superuser:
        messages.error(request, 'Oops, you need to be authorised to do that.')
        return redirect(reverse('progress'))

    post = get_object_or_404(ProgressPost, pk=post_id)
    post.delete()

    messages.success(request, 'Post successfully deleted from the progress blog.')

    return redirect(reverse('progress'))


@login_required
def add_comment(request, post_id):
    """ View for adding a comment to a post """

    if request.method == 'POST':
        try:
            post = get_object_or_404(ProgressPost, pk=post_id)
            author = UserProfile.objects.get(user=request.user)
            comment = Comment(
                post_id=post_id,
                comment_content=request.POST['comment_content'],
                author=author,
            )
            comment.save()
            messages.success(request, 'Comment successfully added.')
            return redirect(reverse('progress'))

        except ProgressPost.DoesNotExist:
            messages.error(request, (
                "Unfortunately one of the items in your basket is unavailable!")
            )
            comment.delete()
            return redirect(reverse('progress'))

@login_required
def delete_comment(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)
    if not request.user.is_superuser and request.user != comment.author:
        messages.error(request, 'Oops, you need to be authorised to do that.')
        return redirect(reverse('progress'))
    else:
        comment.delete()
        messages.success(request, 'Comment successfully deleted.')

    return redirect(reverse('progress'))


@login_required
def edit_comment(request, comment_id):
    """ View for adding a comment to a post """

    if not request.user.is_superuser and request.user != comment.author:
        messages.error(request, 'Oops, you need to be authorised to do that.')
        return redirect(reverse('progress'))
    else:
        if request.method == 'POST':
            try:
                comment = get_object_or_404(Comment, pk=comment_id)
                comment.comment_content = request.POST['comment-content']
                comment.save()
                messages.success(request, 'Comment successfully edited.')
                return redirect(reverse('progress'))

            except ProgressPost.DoesNotExist:
                messages.error(request, (
                    "Unfortunately that comment no longer exists!")
                )
                comment.delete()
                return redirect(reverse('progress'))