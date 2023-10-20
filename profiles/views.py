from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from profiles.forms import ProfileModelForm
from profiles.models import Profile


@login_required
def my_profile_view(request, profile_id):
    profile = Profile.objects.get(user=profile_id)
    form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True

    context = {
        'profile': profile,
        'form': form,
        'confirm': confirm,
    }

    return render(request, 'profiles/myprofile.html', context)


def update_my_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profiles/update_myprofile.html', context)

