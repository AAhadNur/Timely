from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.



@login_required
def myaccount(request):

    context = {   
    }

    return render(request, 'userprofile/myaccount.html', context)



@login_required
def edit_profile(request):
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email = request.POST.get('email', '')
        request.user.save()

        if request.FILES:
            avatar = request.FILES['avatar']
            userprofile = request.user.userprofile
            userprofile.avatar = avatar
            userprofile.save()

        messages.info(request, 'The changes was saved')

        return redirect('myaccount')
    
    return render(request, 'userprofile/edit_profile.html')






