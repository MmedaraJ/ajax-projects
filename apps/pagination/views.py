from math import remainder
from django.shortcuts import redirect, render, reverse
from .models import Users
from datetime import datetime

NUM_PER_PAGE = 4

def index(request):
    return render(request, 'pagination/index.html')

def info(request):
    if request.method == 'POST':
        print(f"Page Number: {request.POST['page_number']}")
        rem = 0
        all_users = {}
        users = {}
        all_users = (Users.objects.filter(first_name__startswith=request.POST['name']) |\
            Users.objects.filter(last_name__startswith=request.POST['name']))\
            .filter(created_at__range=[request.POST['date_from'], request.POST['date_to']])
        users = all_users[NUM_PER_PAGE * (int(request.POST['page_number']) - 1) : NUM_PER_PAGE * int(request.POST['page_number'])]
        print(f"Range: {str(NUM_PER_PAGE * (int(request.POST['page_number']) - 1)) + ':' + str(NUM_PER_PAGE * int(request.POST['page_number']))}")
        if (len(all_users) % NUM_PER_PAGE) > 0: rem = 1
        num_pages =  (len(all_users) // NUM_PER_PAGE) + rem
        print(f'Num Pages: {num_pages}')
        for user in users: print(user.first_name + ' ' + user.last_name)
        print(f'Number of users current displayed: {len(users)}')
        return render(request, 'pagination/users.html', {'all_users':all_users, 'users':users, 'num_pages':range(1, num_pages+1)})

def new(request):
    Users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    return redirect(reverse('pag:index'))