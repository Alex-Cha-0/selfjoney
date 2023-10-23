from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from .models import Post, Like
from profiles.models import Profile
from .forms import PostModelForm, CommentModelForm


def create_post(request):
    profile = Profile.objects.get(user=request.user)
    form = PostModelForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        instance = form.save(commit=False)
        instance.author = profile
        instance.save()
        form = PostModelForm()

    context = {
        'form': form
    }
    return render(request, 'posts/create_post.html', context)


def post_comment_create_and_list_view(request):
    qs = Post.objects.all()
    profile = Profile.objects.get(user=request.user)

    # p_form = PostModelForm()
    c_form = CommentModelForm()

    # if 'submit_p_form' in request.POST:
    #     p_form = PostModelForm(request.POST, request.FILES)
    #     if p_form.is_valid():
    #         instance = p_form.save(commit=False)
    #         instance.author = profile
    #         instance.save()
    #         p_form = PostModelForm()

    if 'submit_c_form' in request.POST:
        c_form = CommentModelForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = profile
            instance.post = Post.objects.get(id=request.POST.get('post_id'))
            instance.save()
            c_form = CommentModelForm

    context = {
        'qs': qs,
        'profile': profile,
        # 'p_form': p_form,
        'c_form': c_form,
    }
    return render(request, 'posts/main.html', context)


def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        profile = Profile.objects.get(user=user)

        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)

        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        else:
            like.value = 'Like'

            post_obj.save()
            like.save()

    return redirect('posts:main-post-view')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/confirm_del.html'
    success_url = reverse_lazy('posts:main-post-view')

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = Post.objects.get(pk=pk)
        if not obj.author.user == self.request.user:
            messages.warning(self.request, "Вы должны быть автором этого поста")
        return obj

class PostUpdateView(DeleteView):
    form_class = PostModelForm
    template_name = 'post/update.html'
    success_url = reverse_lazy('posts:main-post-view')

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        if form.instance.author == profile:
            return super().form_valid(form)
        else:
            form.add_error(None, "Вы должны быть автором этого поста")
            return super().form_invalid(form)