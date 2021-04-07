from django.shortcuts import render,redirect
from Emp.models import UsrRg,NewData
from Emp.forms import UsregForm,Userupdate,NewUsrForm
from django.http import HttpResponse 
# Create your views here.
def home(request):
    return render(request,'html/home.html')
def about(request):
    return render(request,'html/about.html')

def contact(request):
    return render(request,'html/contact.html')
def login(request):
    return render(request,'html/login.html')

def register(request):
    if request.method=="POST":
    	u=request.POST['uname']
    	p=request.POST['pd']
    	m=request.POST['eml']
    	a=request.POST['ag']
    	d={'us':u,'em':m,'age':a,'ps':p}
    	return render(request,'html/details.html',{'d':d})
    return render(request,'html/register.html')
def crud(request):
	if request.method=="POST":
		un=request.POST['username']
		pwd=request.POST['password']
		em=request.POST['email']
		ag=request.POST['age']
		if len(un)!=0:
			data=UsrRg.objects.create(username=un,password=pwd,email=em,age=ag)
			data2 = UsrRg.objects.all()
			return render(request,'html/actions.html',{'info':data2})
	data2 = UsrRg.objects.all()
	return render(request,'html/actions.html',{'info':data2})
def delete(req,id):
	data=UsrRg.objects.get(id=id)
	data.delete()
	return redirect('/crud')
def dform(request):
	if request.method == "POST":
		e = UsregForm(request.POST)
		if e.is_valid():
			q=e.save()
			y=NewData.objects.create(pi_id=q.id)
			return redirect('/show')
	e = UsregForm()
	return render(request,'html/dyform.html',{'tu':e})
def show(request):
	data=UsrRg.objects.all()
	return render(request,'html/show.html',{'info':data})
def infodelete(req,et):
	data=UsrRg.objects.get(id=et)
	if req.method == "POST":
		data.delete()
		return redirect('/show')
	return render(req,'html/undeleted.html',{'sd':data})
def edit(req,id):
	data=UsrRg.objects.get(id=id)
	if req.method=="POST":
		data.username=req.POST["username"]
		data.age=req.POST["age"]
		data.password=req.POST["password"]
		data.email=req.POST["email"]
		data.save()
		return HttpResponse("datasaved")
	return render(req,'html/useredit.html',{'info':data}) 
def userupdate(up,si):
	t=UsrRg.objects.get(id=si)
	y=NewData.objects.get(pi_id=si)
	if up.method=="POST":
			d=Userupdate(up.POST,instance=t)
			k=NewUsrForm(up.POST,instance=y)
			if d.is_valid() and k.is_valid():
				d.save()
				k.save()
				return redirect('/show')
	d=Userupdate(instance=t)
	k=NewUsrForm(instance=y)
	return render(up,'html/updateuser.html',{'us':d,'nt':k})
def userinfo(ty,uname):
	p = UsrRg.objects.get(username=uname)
	h = NewData.objects.get(pi_id=p.id)
	return render(ty,'html/viewinfo.html',{'y':p,'yu':h})










