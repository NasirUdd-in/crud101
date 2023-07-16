from django.shortcuts import render,get_object_or_404,HttpResponseRedirect, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

# Create your views here.
from .models import GeeksModel
from .forms import GeeksForm

def create_view(request):
    context = {}

    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']=form
    return render(request, "create_view.html",context)


def list_view(request):
    context = {}

    context['dataset'] = GeeksModel.objects.all()

    return render(request, "list_view.html", context)

def detail_view(request, id):
    context = {}

    context['data'] = GeeksModel.objects.get(id =id)

    return render(request, "detail_view.html", context)

def update_view(request, id):
    context = {}

    obj = get_object_or_404(GeeksModel, id = id)

    form = GeeksForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
    
    context["form"] = form

    return render(request, "update_view.html", context)


def delete_view(request, id):
    context = {}

    obj = get_object_or_404(GeeksModel, id = id)

    if request.method == "POST":
            obj.delete()

            return HttpResponseRedirect("/")
        
    return render(request, "delete_view.html", context)


#################### index#######################################

def index(request):
    return render(request, 'user/index.html', {'title': 'indext'})


########### register here #####################################
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
######################### mail system ####################################
            # htmly = get_template('user/Email.html')
            # d = {'username': username}
            # subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            # html_content = htmly.render(d)
            # msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title':'register here'})
  
################ login forms###################################################
def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'log in'})

