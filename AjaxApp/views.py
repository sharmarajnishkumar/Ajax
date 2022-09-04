from django.http import JsonResponse
from django.shortcuts import render

from .models import User

def index(request):
    data=User.objects.all()
    return render(request,'index.html',{'user':data})

# Create your views here.
def add(request):
    if request.method == 'POST':
        nm = request.POST['name']
        em = request.POST['email']
        mb = request.POST['mobile']
        ct = request.POST['city']
        reg = User(
            name=nm,
            email=em,
            mobile=mb,
            city=ct
        )
        reg.save()
        data=User.objects.values()
        std=list(data)
        return JsonResponse({'Status':'Saved','std':std})
    else:
        return JsonResponse({'Status':0})
             


    # if request.method == 'POST':
    #     fm = UserForms(request.POST)
    #     if fm.is_valid():
    #         nm = fm.cleaned_data['name']
    #         em = fm.cleaned_data['email']
    #         mb = fm.cleaned_data['mobile']
    #         ct = fm.cleaned_data['city']
    #         reg = User(
    #             name=nm,
    #             email=em,
    #             mobile=mb,
    #             city=ct
    #         )
    #         reg.save()
    #         fm = UserForms()
    # else:
    #     fm = UserForms() 
    #     data=User.objects.all()   
    # return render(request,'index.html',{'form':fm,'data':data})