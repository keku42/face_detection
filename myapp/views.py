from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def myindex(request):
    return render(request,'index.html')


# def submitquery(request):
#     if request.method == 'POST' :
#         from Main import face_recognition 

#         # emp_ID = int(request.POST.get('emp_ID'))
#         labelname,ctime,tdate = face_recognition(0)
        
#         print(labelname)
#         return render(request,'index.html',{"labelname":labelname,'tdate': tdate, 'ctime': ctime })
    
#     else:
#         return render(request,'index.html')

# def submitquery(request):
#     if request.method == 'POST' :
#         from Main import face_recognition 
#         from query import queryclass
#         # emp_ID = int(request.POST.get('emp_ID'))
#         labelname,tdate,ctime = face_recognition(0)
#         b = queryclass()
#         # b.insert_emp_attandace(labelname[2:3],tdate,ctime)
#         b.insert_emp_attandace(int(labelname.split("_")[0]),tdate,ctime)
                
#         print(labelname)
#         return render(request,'index.html',{"labelname":labelname,'tdate': tdate, 'ctime': ctime })
    
#     else:
#         return render(request,'index.html')

def submitquery(request):
    if request.method == 'POST' :
        from Main import newFD

        labelname = newFD()
        return render(request,'index.html')
        # return render(request,'index.html',{"labelname":labelname })
    
        # from query import queryclass
        # emp_ID = int(request.POST.get('emp_ID'))
        # labelname,tdate,ctime = face_recognition(0)
        # b = queryclass()
        # b.insert_emp_attandace(labelname[2:3],tdate,ctime)

        # b.insert_emp_attandace(int(labelname.split("_")[0]),tdate,ctime)
                
        # print(labelname)
        # return render(request,'index.html',{"labelname":labelname,'tdate': tdate, 'ctime': ctime })
    
    else:
        return render(request,'index.html')