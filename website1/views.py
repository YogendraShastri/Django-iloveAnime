
from asyncio import constants
from django.shortcuts import render
from services.models import Service, Notification, NotesModel, VideosModel
from django.core.paginator import Paginator
from  website1.constants import param
from django.core.mail import send_mail
from django.core.mail import EmailMessage, get_connection
from django.conf import settings




def Notify(request, slug):
    Notic_details = Notification.objects.get(Notification_slug=slug)
    all_notices = Notification.objects.all()
    if request.method == 'GET':
        search_term = request.GET.get("search_keyword")
        if search_term != None :
            all_notices = Notification.objects.filter(Notification_desc__icontains=search_term)
    paginator = Paginator(all_notices, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    total_pages = page_obj.paginator.num_pages
    data = {

        'Notic_details': Notic_details,
        'all_notices': page_obj,
        'total_pages': total_pages,
        'notification_page_list' : [i+1 for i in range(total_pages)],
    }
    return render(request, 'notify.html', data)

def Open_blogs(request, slug):
    blog_details = Service.objects.get(service_slug=slug)
    data = {
        'blog_data': blog_details
    }
    return render(request, 'open_blog.html', data)

def AboutUs(request):
    data = {
        'title': param['About_us_title'],
        'content': param['About_us_desc'],
    }
    return render(request, 'aboutus.html', data)

def Home(request):
    service_data = Service.objects.all()
    notice_data = Notification.objects.all()
    if request.method == 'GET':
        search_term = request.GET.get("search_keyword")
        if search_term != None :
            service_data = Service.objects.filter(service_desc__icontains=search_term)
    paginator = Paginator(service_data, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    total_pages = page_obj.paginator.num_pages
    data = {
        'title':'Home Page',
        'content': param['Front_page_content'],
        'pages': ['1','2','3','4','5'],
        'subjects':[
            {'name':'python', 'id':123},
            {'name':'java', 'id':234}
        ],
        'service_data' : page_obj,
        'total_pages' : total_pages,
        'service_page_list' : [i+1 for i in range(total_pages)],
        'notice_data' : notice_data,
        'writer': param['writer'],
        'testimonial': param['testimonial']
    }
    return render(request, 'bootstrap5.html', data)
    # return render(request, 'index.html', data)

def blogs(request):
    service_data = Service.objects.all()
    if request.method == 'GET':
        search_term = request.GET.get("search_keyword")
        if search_term != None :
            service_data = Service.objects.filter(service_desc__icontains=search_term)
    paginator = Paginator(service_data, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    total_pages = page_obj.paginator.num_pages
    data = {
        'service_data' : page_obj,
        'total_pages' : total_pages,
        'service_page_list' : [i+1 for i in range(total_pages)]
    }
    return render(request, 'blogs.html', data)

def Contact(request):
    data = {
        'email_sent': False
    }
    if request.method == "POST": 
       with get_connection(  
           host=settings.EMAIL_HOST, 
           port=settings.EMAIL_PORT,  
           sender_email=settings.EMAIL_HOST_USER, 
           sender_password=settings.EMAIL_HOST_PASSWORD, 
           use_tls=settings.EMAIL_USE_TLS
            ) as connection:
           subject = request.POST.get('YourSub')  
           email_user = request.POST.get('YourEmail')
           email_from = settings.EMAIL_HOST_USER  
           recipient_list = ['cgcoder1@gmail.com', ]  
           message =request.POST.get('YourMsg')
           Name = request.POST.get('YourName')
           MSG = f"{Name} sent a Massage : {message} \nentered Emailid is {email_user}"
           EmailMessage(subject, MSG, email_from, recipient_list, connection=connection).send()
           data['email_sent']  = True
    return render(request, 'contact.html', data)

def Calculator(request):
    data = {}
    try:
        if request.method == "POST":
            Number1 = int(request.POST.get("Num1"))
            Number2 = int(request.POST.get("Num2"))
            Cal_option = request.POST.get("cal_option")
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

def admin_panel(request):
    if request.method == "POST":
        username = request.POST.get('inputUsername')
        password = request.POST.get('inputPassword')
        if username == param['admin'] and password == param['adminPassword']:
            return render(request, 'admin_panel.html')

def admin_login(request):
    data = {}
    if request.method == 'POST':
        username = request.POST.get('inputUsername')
        password = request.POST.get('inputPassword')
        if username == param['admin']  and password == param['adminPassword']:
            return render(request, 'admin_panel.html')
        elif username != param['admin']:
            print("Username not correct")
            data  = {
                'tags': 'danger',
                'message':'User does not Exist'
            }
            return render(request, 'admin_login.html', data)
        elif password != param['adminPassword']:
            print("incorrect Password")
            data  = {
                'tags':'danger',
                'message':'Incorrect Password'
            }
            return render(request, 'admin_login.html', data)
    else:
        return render(request, 'admin_login.html')
    return render(request, 'admin_login.html')

def videos(request):
    allVideos = VideosModel.objects.all()
    video_id = 0
    for video in allVideos:
        video_id = video.video_link.split('/')[-1]
    if request.method == 'GET':
        search_term = request.GET.get("search_keyword")
        if search_term != None :
            allVideos = VideosModel.objects.filter(video_desc__icontains=search_term)
    paginator = Paginator(allVideos, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    total_pages = page_obj.paginator.num_pages
    data = {
        'videos_data' : page_obj,
        'total_pages' : total_pages,
        'videos_page_list' : [i+1 for i in range(total_pages)],
        'video_id': video_id
    }
    return render(request, 'videos.html', data)

def Notes(request):
    allNotes = NotesModel.objects.all()
    if request.method == 'GET':
        search_term = request.GET.get("search_keyword")
        if search_term != None :
            allNotes = NotesModel.objects.filter(Notes_desc__icontains=search_term)
    paginator = Paginator(allNotes, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    total_pages = page_obj.paginator.num_pages
    data = {
        'notes_data' : page_obj,
        'total_pages' : total_pages,
        'notes_page_list' : [i+1 for i in range(total_pages)]
    }
    return render(request, 'notes.html', data)

def EditService(request):
    if request.method == "POST":
        icon = request.FILES.get('service_icon')
        title = request.POST.get('service_title')
        desc = request.POST.get('service_small_desc')
        detailed_desc = request.POST.get('service_detailed_desc')
        en = Service(service_icon=icon, service_title=title,service_desc=desc,service_detailed_desc=detailed_desc)
        en.save()
    return render(request, 'edit_service.html')
