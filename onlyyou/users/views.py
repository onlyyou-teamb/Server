from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.contrib.auth.models import User
#from .num_of_face import NumOfFace
#from .coordinate_faces_ver2 import CoordinateFaces


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            # Profile object creates
            profile = Profile(user=User.objects.get(username=username))
            profile.save()

            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            profile = Profile.objects.get(user=request.user)
            firstimage = profile.first_image.path
            secondimage = profile.second_image.path
            thirdimage = profile.third_image.path

            if not NumOfFace(firstimage):
                # no face or more than 2 faces appeared
                messages.error(
                    request, f'No face or more than 2 faces appeared at 1st pic!')
                profile.first_image.delete()
                return redirect('profile')

            else if not NumOfFace(secondimage):
                # no face or more than 2 faces appeared
                messages.error(
                    request, f'No face or more than 2 faces appeared at 2nd pic!')
                profile.second_image.delete()
                return redirect('profile')

            else if not NumOfFace(thirdimage):
                # no face or more than 2 faces appeared
                messages.error(
                    request, f'No face or more than 2 faces appeared at 3rd pic!')
                profile.third_image.delete()
                return redirect('profile')

            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


def upload(request):

    return render(request, 'users/upload.html')
