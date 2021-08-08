from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import ListView, DetailView, TemplateView, UpdateView
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from .models import pubg_registered_id
from .models import pubg_registered_id_10_taka
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import freefire_registered_id


# class home(ListView):
#     template_name="index.html"
#     model=post
#     ordering=['-id']

#     def get_queryset(self):
#         query_set=super().get_queryset()
#         return query_set.select_related


def home(request):
    return render(request, "index.html")


def pubg(request):
    return render(request, "pubg.html")


def freefire(request):
    return render(request, "freefire.html")


def pes(request):
    return render(request, "coming_soon.html")


def pubg_join(request):
    return render(request, "pubg_join.html")


def pubg_join_10_taka(request):
    return render(request, "pubg_join_10_taka.html")


def freefire_join(request):
    return render(request, "freefire_join.html")


def contact(request):
    return render(request, "contact.html")


class account(ListView):
    template_name = "account.html"
    model = pubg_registered_id
    ordering = ['-id']

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related

    def get_context_data(self, *args, **kwargs):
        context = super(account, self).get_context_data(*args, **kwargs)
        context['pubg_registered_id_10_taka_list'] = pubg_registered_id_10_taka.objects.all()
        context['freefire_registered_id_list'] = freefire_registered_id.objects.all()
        return context


def register_form_pubg(request):
    if request.method == "POST":
        username = request.POST['username']
        tournament_name = request.POST['tournament_name']
        tournament = request.POST['tournament']
        pubg_id_1 = request.POST['pubg_id_1']
        pubg_id_2 = request.POST['pubg_id_2']
        phone = request.POST['phone']
        transactionid = request.POST['transactionid']
        phone_4_digit = request.POST['phone_4_digit']
        registration_status = request.POST['registration_status']
        room_id = request.POST['room_id']
        room_password = request.POST['room_password']
        slot = request.POST['slot']
        time = request.POST['time']

        if tournament == "Select Tournament":
            messages.error(request,"You have to select a tournament first")
            return render(request, 'pubg_join.html')
            

        elif pubg_id_1 == "":
            messages.error(request,"Please insert 1st team member name")
            return render(request, 'pubg_join.html')
          

        elif phone == "":
            messages.error(request,"Please insert your phone number")
            return render(request, 'pubg_join.html')
    

        elif transactionid == "":
            messages.error(request,"Please insert your Transacction ID or type Free")
            return render(request, 'pubg_join.html')
          

        elif phone_4_digit == "":
            messages.error(request,"Please insert your phone last 4 digit or type Free")
            return render(request, 'pubg_join.html')
           

        elif tournament == "PUBG 10 TAKA (Solo)" and transactionid == "Free" or tournament == "PUBG 10 TAKA (Solo)" and transactionid == "free":
            messages.error(request,"It is not a free match bro.You must be insert your transaction ID.")
            return render(request, 'pubg_join.html')
          

        elif tournament == "PUBG 20 TAKA (Duo)" and transactionid == "Free":
            messages.error(request,"It is not a free match bro.You must be insert your transaction ID.")
            return render(request, 'pubg_join.html')
           

        elif pubg_registered_id.objects.filter(username=username,tournament=tournament).exists():
            # if pubg_registered_id.objects.filter(tournament=tournament).exists():
            messages.error(request,"You are already request for the tournament.Try to register same category tournament in the next match or try to register another tournament.")
            return render(request, 'pubg_join.html')
            # return HttpResponse("You are already request for the tournament.Try to register same category tournament in the next match or try to register another tournament.")
            # else:
            #     pubg_registered_id_database = pubg_registered_id(username=username, tournament_name=tournament_name, tournament=tournament,
            #                                                  pubg_id_1=pubg_id_1, pubg_id_2=pubg_id_2, phone=phone, transactionid=transactionid,
            #                                                   phone_4_digit=phone_4_digit, registration_status=registration_status,
            #                                                   room_id=room_id,room_password=room_password,slot=slot,time=time)
            #     pubg_registered_id_database.save()
        
        else:

            pubg_registered_id_database = pubg_registered_id(username=username, tournament_name=tournament_name, tournament=tournament,
                                                             pubg_id_1=pubg_id_1, pubg_id_2=pubg_id_2, phone=phone, transactionid=transactionid,
                                                              phone_4_digit=phone_4_digit, registration_status=registration_status,
                                                              room_id=room_id,room_password=room_password,slot=slot,time=time)
            pubg_registered_id_database.save()
            return redirect('account')


def register_form_pubg_10_taka(request):
    if request.method == "POST":
        username = request.POST['username']
        pubg_id = request.POST['pubg_id']
        phone = request.POST['phone']
        transactionid = request.POST['transactionid']
        phone_4_digit = request.POST['phone_4_digit']

        pubg_registered_id_10_taka_database = pubg_registered_id_10_taka(
            username=username, pubg_id=pubg_id, phone=phone, transactionid=transactionid, phone_4_digit=phone_4_digit)
        pubg_registered_id_10_taka_database.save()
        return redirect('account')


def signinn(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request,"Username or password incorrect")

    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already taken")
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, password=password, email=email)
                user.save()
                # messages.success(request, "Account created successfully.")
                login(request, user)
                return redirect('/')

        else:
            messages.error(request, 'Password not matched')

    return render(request, 'signup.html')


def signout(request):
    logout(request)
    return redirect("/")

def register_form_freefire(request):
    if request.method == "POST":
        username = request.POST['username']
        tournament_name = request.POST['tournament_name']
        tournament = request.POST['tournament']
        freefire_id_1 = request.POST['freefire_id_1']
        freefire_id_2 = request.POST['freefire_id_2']
        phone = request.POST['phone']
        transactionid = request.POST['transactionid']
        phone_4_digit = request.POST['phone_4_digit']
        registration_status = request.POST['registration_status']
        room_id = request.POST['room_id']
        room_password = request.POST['room_password']
        slot = request.POST['slot']
        time = request.POST['time']
        email = request.POST['email']

        if tournament == "Select Tournament":
            messages.error(request,"You have to select a tournament first")
            return render(request, 'freefire_join.html')
            

        elif freefire_id_1 == "":
            messages.error(request,"Please insert 1st team member name")
            return render(request, 'freefire_join.html')
          

        elif phone == "":
            messages.error(request,"Please insert your phone number")
            return render(request, 'freefire_join.html')
    

        elif transactionid == "":
            messages.error(request,"Please insert your Transacction ID or type Free")
            return render(request, 'freefire_join.html')
          

        elif phone_4_digit == "":
            messages.error(request,"Please insert your phone last 4 digit or type Free")
            return render(request, 'freefire_join.html')
           

        elif tournament == "PUBG 10 TAKA (Solo)" and transactionid == "Free":
            messages.error(request,"It is not a free match bro.You must be insert your transaction ID.")
            return render(request, 'freefire_join.html')
          

        elif tournament == "PUBG 20 TAKA (Duo)" and transactionid == "Free":
            messages.error(request,"It is not a free match bro.You must be insert your transaction ID.")
            return render(request, 'freefire_join.html')
           

        elif freefire_registered_id.objects.filter(username=username,tournament=tournament).exists():
            messages.error(request,"You are already request for the tournament.Try to register same category tournament in the next match or try to register another tournament.")
            return render(request, 'freefire_join.html')
        
        else:

            freefire_registered_id_database = freefire_registered_id(username=username, tournament_name=tournament_name, tournament=tournament,
                                                             freefire_id_1=freefire_id_1, freefire_id_2=freefire_id_2, phone=phone, transactionid=transactionid,
                                                              phone_4_digit=phone_4_digit, registration_status=registration_status,
                                                              room_id=room_id,room_password=room_password,slot=slot,time=time,email=email)
            freefire_registered_id_database.save()
            return redirect('account')
