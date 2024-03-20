from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest
from django.http import HttpResponse


# 定义视图：提供服务器路径下的数据
def index(request):
    # 准备上下文：定义在字典中（测试数据）
    context = {'title': '测试末班处理数据'}
    # 将上下文交给模版中进行处理，处理后视图响应给客户端
    return render(request, 'Book/index.html', context)


# 增加方式一：
from Book.models import Book

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
book = Book.objects.filter(id__exact=1)
print(book)
# 查询书名包含'湖'的图书
book = Book.objects.filter(name__contains='传')
print(book)
# 查询书名以'部'结尾的图书
book = Book.objects.filter(name__endswith='部')
print(book)
# 查询书名为空的图书
book=Book.objects.filter(name__isnull=True)
print(book)
# 查询编号为1或3或5的图书
book = Book.objects.filter(id__in=[1,3,5])
print(book)
# 查询编号大于3的图书
book = Book.objects.filter(id__gt=3)
print(book)
# 查询1980年发表的图书
book = Book.objects.filter(pub_data__year=1980)
print(book)
# 查询1990年1月1日后发表的图书
book=Book.objects.filter(pub_data__gt='1990-1-1')
print(book)

# F对象
# 查询阅读量大于等于评论量的图书。
from django.db.models import F, Q
book = Book.objects.filter(readcount__gt=F('commentcount'))
print(book)
# 查询阅读量大于2倍评论量的图书。
book = Book.objects.filter(readcount__gt=F('commentcount')*2)
print(book)
# 查询阅读量大于20，并且编号小于3的图书
book = Book.objects.filter(readcount__gt=20,id__lt=3)
print(book)
# 查询阅读量大于20，或编号小于3的图书
book = Book.objects.filter(Q(readcount__gt=20) | Q(id__lt=3))
print(book)
# 查询编号不等于3的图书
book = Book.objects.filter(~Q(id=3))
print(book)
# 查询图书的总阅读量。
from django.db.models import Sum
book = Book.objects.aggregate(Sum('readcount'))
print(book)
# 查询图书总数。
book = Book.objects.count()
print(book)
# 根据阅读量进行排序
book = Book.objects.all().order_by('readcount')
print(book)

