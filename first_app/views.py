
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from first_app.models import AccessRecord, Topic, Webpage
from first_app.forms import FormName, UserForm, UserProfileInfoForm

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    context = {'access_records': webpages_list, 'text':'hello world', 'number':100}
    return render(request, 'first_app/index.html', context=context)

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'first_app/registration.html',
                    {   'user_form': user_form,
                        'profile_form': profile_form,
                        'registered': registered })


@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('first_app:index'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('first_app:index'))
            else:
                return HttpResponse("ACCOUNT IS NOT ACTIVE!")

        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid login. Details supplied.")

    return render(request, 'first_app/user_login.html', {})

def other(request):
    return render(request, 'first_app/other.html')

def relative(request):
    return render(request, 'first_app/relative_url_templates.html')

def form_name_view(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            print("Form received. Validation Success!")
            print("NAME " + form.cleaned_data['name'])
            print("EMAIL " + form.cleaned_data['email'])
            print("TEXT " + form.cleaned_data['text'])


    return render(request, 'first_app/form_name.html', {'form': form})
