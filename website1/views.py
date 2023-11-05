from ast import Num
from curses.ascii import isdigit
from django.http import HttpResponse
from django.shortcuts import render
from services import models
from services.models import Service, Notification
# from .forms import Usersform

def Notify(request, page_id):
    Notic_details = Notification.objects.get(id=page_id)
    data = {

        'Notic_details': Notic_details
    }
    return render(request, 'notify.html', data)

def AboutUs(request):
    data = {
        'title':'About Us Page',
        'content': "Welcome to About us Page",
    }
    return render(request, 'aboutus.html', data)

def Home(request):
    service_data = Service.objects.all()
    notice_data = Notification.objects.all()
    data = {
        'title':'Home Page',
        'content': "Welcome to Home Page",
        'pages': ['1','2','3','4','5'],
        'subjects':[
            {'name':'python', 'id':123},
            {'name':'java', 'id':234}
        ],
        'service_data' : service_data,
        'notice_data' : notice_data
    }
    return render(request, 'bootstrap5.html', data)
    # return render(request, 'index.html', data)

def blogs(request, blog_id):
    return HttpResponse(f"Blog No {blog_id}")

def Contact(request):
    data = {
        'title':'Contact US Page',
        'content': "Welcome to Contact US Page"
    }
    return render(request, 'contact.html', data)

def Calculator(request):
    data = {}
    try:
        if request.method == "POST":
            Number1 = int(request.POST.get("Num1"))
            Number2 = int(request.POST.get("Num2"))
            Cal_option = request.POST.get("cal_option")
            print(f"{Number1} {Cal_option} {Number2} = ")
            if Cal_option == 'Addition':
                data = Number1 + Number2
            elif Cal_option == 'Substraction':
                data = Number1 - Number2
            elif Cal_option == 'Multiplication':
                data = Number1 * Number2
            elif Cal_option == 'Division':
                data = Number1/Number2
            else:
                return render(request, 'calculator.html', { 'error': True })  
            data = {
                'result': data,
                'Number1' : Number1,
                'Number2' : Number2,
            }
    except Exception as e:
        print("Error Occured")
    print(data)
    return render(request, 'calculator.html', data)

def adminPanel(request):
    return render(request, 'admin_panel.html')

def EditService(request):
    return render(request, 'edit_service.html')
