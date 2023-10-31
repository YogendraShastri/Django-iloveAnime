from django.http import HttpResponse
from django.shortcuts import render

def AboutUs(request):
    data = {
        'title':'About Us Page',
        'content': "Welcome to About us Page"
    }
    return render(request, 'aboutus.html', data)

def Home(request):
    data = {
        'title':'Home Page',
        'content': "Welcome to Home Page",
        'pages': ['1','2','3','4','5'],
        'subjects':[
            {'name':'python', 'id':123},
            {'name':'java', 'id':234}
        ]
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
    data = 0
    try:
        if request.method == "POST":
            Number1 = int(request.POST.get("Num1"))
            Number2 = int(request.POST.get("Num2"))
            Cal_option = request.POST.get("cal_option")
            print(f"Number1 = {Number1} , Number2 = {Number2}, Cal = {Cal_option}")
            if Cal_option == 'Addition':
                data = Number1 + Number2
            elif Cal_option == 'Substraction':
                data = Number1 - Number2
            elif Cal_option == 'Multiplication':
                data = Number1 * Number2
            else:
                data = Number1/Number2
    except Exception as e:
        print("Error Occured")
    print(data)
    return render(request, 'calculator.html', {data: data})