import re
from django.http import HttpResponse
from django.shortcuts import render
from services import models
from services.models import Service, Notification, NotesModel, VideosModel
from django.core.paginator import Paginator

def Notify(request, slug):
    Notic_details = Notification.objects.get(Notification_slug=slug)
    data = {

        'Notic_details': Notic_details
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
        'title':'About Us Page',
        'content': "Welcome to About us Page",
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
        'content': "Welcome to Home Page",
        'pages': ['1','2','3','4','5'],
        'subjects':[
            {'name':'python', 'id':123},
            {'name':'java', 'id':234}
        ],
        'service_data' : page_obj,
        'total_pages' : total_pages,
        'service_page_list' : [i+1 for i in range(total_pages)],
        'notice_data' : notice_data
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
    print(f"Blogs are {data['service_data']}")
    return render(request, 'blogs.html', data)

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
        print(f"{icon} + {title} + {desc} + {detailed_desc}")
        en = Service(service_icon=icon, service_title=title,service_desc=desc,service_detailed_desc=detailed_desc)
        en.save()
    return render(request, 'edit_service.html')
