#coding=utf-8
from django.shortcuts import render,render_to_response

from django.http import HttpResponse,HttpResponseRedirect

from django.template import RequestContext, loader

from .models import Movie,User

from .forms import SearchForm,UserForm
# Create your views here.
def home(request):
	movies=Movie.objects.all()
	context = {'movies':movies}
#	if request.method == 'POST':
#		form=SearchForm(request.POST)
#		if form.is_valid():
#			searchname=form.cleaned_data['moviename']
#			filter_movie= Movie.objects.filter(title__contains= searchname)
#			if filter_movie:
#				#context={'movie':filter_movie}
#				#return render(request,'movieapp/search.html',context)
#				#response = HttpResponseRedirect('/movieapp/search')
#				#response.set_cookie('filter_movie',filter_movie,3600)
#				return render_to_response('movieapp/search.html' ,{'movie':filter_movie})
#	else:
	form=SearchForm()
	return render(request, 'movieapp/home.html', {'movies':movies,'form': form})

def detail(request,movie_id):
	movie=Movie.objects.get(pk=movie_id)
	context = {'movie':movie}
	return render(request, 'movieapp/detail.html', context)

def search(request):
	if request.method == 'POST':
		form=SearchForm(request.POST)
		if form.is_valid():
			searchname=form.cleaned_data['moviename']
			filter_movie= Movie.objects.filter(title__contains= searchname)
			#filter_movie=filter_movie[0]    #这一步非常关键，因为使用filter过滤出来的是一个列表
			if filter_movie:
				count=len(filter_movie)
				context={'movies':filter_movie,'count':count}   #计算一共有几部电影
				#return render(request,'movieapp/search.html',context)
				#response = HttpResponseRedirect('/movieapp/search')
				#response.set_cookie('filter_movie',filter_movie,3600)
				return render_to_response('movieapp/search.html' ,context)
	else:
		form=SearchForm()
	return HttpResponse('对不起了，没有找到你想要的结果')

#注册
def regist(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            #获得表单数据
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            #添加到数据库
            User.objects.create(username= username,password=password)
            return HttpResponse('regist success!!')
    else:
        userform = UserForm()
    return render_to_response('movieapp/regist.html',{'userform':userform}, context_instance=RequestContext(request))

#登陆
def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            #获取表单用户密码
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/movieapp/index/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/movieapp/login/')
    else:
        userform = UserForm()
    return render_to_response('movieapp/login.html',{'userform':userform},context_instance=RequestContext(request))

#登陆成功
def index(request):
    username = request.COOKIES.get('username','')
    return render_to_response('movieapp/index.html' ,{'username':username})

#退出
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response

