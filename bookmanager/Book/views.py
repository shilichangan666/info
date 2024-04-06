from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect


# 定义视图：提供服务器路径下的数据
def index(request):
    # 准备上下文：定义在字典中（测试数据）
    context = {'title': '测试末班处理数据'}
    # 将上下文交给模版中进行处理，处理后视图响应给客户端
    return render(request, 'Book/index.html', context)


# 增加方式一：
from Book.models import Book, PeopleInfo

# Book = Book(
#     name='Django',
#     pub_data='2000-01-01',
#     readcount=1000,
#     commentcount=2000
# )
# Book.save()

# 增加方式二,通过模型类.objects.create()实现
# Book.objects.create(
#     name = 'java1',
#     pub_data = '2202-01-09',
#     readcount = 1000002,
#     commentcount = 30000
# )

# 修改方式一：
# book = Book.objects.get(id=7)
# book.name = '运维开发部门'
# book.save()

# 修改方式二：
# personinfo = PeopleInfo.objects.filter(name='虚竹').update(name='传智播客')

# 删除方式一：
# person = PeopleInfo.objects.get(name='传智播客')
# person.delete()

# 删除方式二：
# Book.object.filter(name='袁紫衣').delete()

# 查询
# 基础查询
# (get)
# Book = Book.objects.get(id=6)
# (all)
# Book = Book.objects.all()
# (count)
# book = Book.objects.count()
# print(book)

#####################################过滤查询##########################################
# 查询编号为1的图书
# book = Book.objects.filter(id__exact=1)
# print(book)
# 查询书名包含'湖'的图书
# book = Book.objects.filter(name__contains='传')
# print(book)
# 查询书名以'部'结尾的图书
# book = Book.objects.filter(name__endswith='部')
# print(book)
# 查询书名为空的图书
# book=Book.objects.filter(name__isnull=True)
# print(book)
# 查询编号为1或3或5的图书
# book = Book.objects.filter(id__in=[1,3,5])
# print(book)
# 查询编号大于3的图书
# book = Book.objects.filter(id__gt=3)
# print(book)
# 查询1980年发表的图书
# book = Book.objects.filter(pub_data__year=1980)
# print(book)
# 查询1990年1月1日后发表的图书
# book=Book.objects.filter(pub_data__gt='1990-1-1')
# print(book)

# F对象
# 查询阅读量大于等于评论量的图书。
# from django.db.models import F, Q
# book = Book.objects.filter(readcount__gt=F('commentcount'))
# print(book)
# 查询阅读量大于2倍评论量的图书。
# book = Book.objects.filter(readcount__gt=F('commentcount')*2)
# print(book)
# 查询阅读量大于20，并且编号小于3的图书
# book = Book.objects.filter(readcount__gt=20,id__lt=3)
# print(book)
# 查询阅读量大于20，或编号小于3的图书
# book = Book.objects.filter(Q(readcount__gt=20) | Q(id__lt=3))
# print(book)
# 查询编号不等于3的图书
# book = Book.objects.filter(~Q(id=3))
# print(book)
# 查询图书的总阅读量。
# from django.db.models import Sum
# book = Book.objects.aggregate(Sum('readcount'))
# print(book)
# 查询图书总数。
# book = Book.objects.count()
# print(book)
# 根据阅读量进行排序
# book = Book.objects.all().order_by('readcount')
# print(book)

# 级联查询
# 关联查询
# 查询书籍为1的所有人物信息
book = Book.objects.get(id=1)
person = book.peopleinfo_set.all()
print(person)
# 查询人物为1的书籍信息
people = PeopleInfo.objects.get(id=1)
book = people.book
print(book)

# 关联过滤查询
# 查询图书，要求图书人物为"郭靖"
book = Book.objects.filter(peopleinfo__name='郭靖')
print(book)
# 查询图书，要求图书中人物的描述包含"八"
book = Book.objects.filter(peopleinfo__discription__contains='八')
print(book)
# 查询书名为“天龙八部”的所有人物
person = PeopleInfo.objects.filter(book__name='天龙八部')
print(person)
# 查询图书阅读量大于30的所有人物
person = PeopleInfo.objects.filter(book__readcount__gt=30)
print(person)

# 分页
# 查询结果集
book = Book.objects.all()
# 导入分页类
from django.core.paginator import Paginator

# 创建分页实例
paginator = Paginator(book, 2)
# 获取制定页码的数据
page_book = paginator.page(1)
# 获取分页数据
total = paginator.num_pages


# URL路径参数
def goods(request, cat_id, id):
    return JsonResponse({'cat_id': cat_id, 'id': id})


# 查询字符串参数
"""
    http://ip/port/path/?key=value&key1=value1
"""


def shops(request):
    query_params = request.GET
    # 查询字符串参数使用get只能通过键获取一个值，当一个键有多个值的时候，则使用get只能获取最后值
    order = query_params.get('order')
    print(order)
    # 使用getlist()方法，当一个键有多个值的时候，则可以获取所有的值
    order_list = query_params.getlist('order')
    print(order_list)
    # 获取到请求字符串的所有参数
    print(query_params)
    return HttpResponse('这是我的饭店')


def register(request):
    data = request.POST
    print(data)
    return HttpResponse('ok')


def json(request):
    body = request.body
    print(body)
    # b'{\n    "name":"dwj",\n    "age":"123"\n\n}'
    body_str = body.decode()
    print(body_str)
    import json
    body_dict = json.loads(body_str)
    print(body_dict)
    # 请求头对象
    print(request.META)
    # 请求头的端口参数
    print(request.META['SERVER_PORT'])
    # 请求的方法
    print(request.method)
    # 请求的用户对象
    print(request.user)
    # 请求的路径
    print(request.path)
    # 请求的编码
    print(request.encoding)
    # 上传的文件
    print(request.FILES)
    return HttpResponse('ok')


def response(request):
    response = HttpResponse('djangoPython')
    response.status_code = 200
    response['dwj'] = 'xmut'
    return response


# JsonResponse
def jsonresponse(request):
    girl_friend = {
        'name': '小美',
        'age': 20
    }
    return JsonResponse(data=girl_friend, safe=False)
    # return JsonResponse({'city': 'begin', 'subject': 'python'})


# Redirect重定向
def redirectresponse(request):
    return redirect('/index')


# Cookie
# 设置cookie
def cookie(request):
    response = HttpResponse('ok')
    response.set_cookie('username', 'dwj')
    response.set_cookie('usernames', 'dwj1', max_age=3600)  # 设置cookie，有效期为一小时
    return response

    # 读取cookie


def cookieread(request):
    cookie = request.COOKIES.get('usernames')
    print(cookie)
    return HttpResponse('ok')


# 删除cookie
def delcookie(request):
    response = HttpResponse('Cookie delete')
    response.delete_cookie('usernames')
    return response


# session
def set_session(request):
    # 1. 模拟用户信息
    username = request.GET.get('username')

    # 2. 设置session信息
    user_id = 1
    request.session['user_id'] = user_id
    request.session['username'] = username

    # clear 删除session里的数据，但是key有保留
    #request.session.clear()
    # flush是删除所有，包括key
    #request.session.flush()
    #del request.session['username']
    request.session.set_expiry(3600)
    return HttpResponse("set_session")


# 获取session数据
def get_session(request):
    user_id = request.session['user_id']
    username = request.session['username']
    content = '{},{}'.format(user_id,username)
    return HttpResponse(content)
