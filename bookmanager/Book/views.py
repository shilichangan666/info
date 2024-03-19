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
from Book.models import Book,PeopleInfo

Book = Book(
    name='Django',
    pub_data='2000-01-01',
    readcount=1000,
    commentcount=2000
)
# Book.save()

# 增加方式二,通过模型类.objects.create()实现
Book.objects.create(
    name = 'java1',
    pub_data = '2202-01-09',
    readcount = 1000002,
    commentcount = 30000
)

# 修改方式一：
book = Book.objects.get(id=7)
book.name = '运维开发部门'
book.save()

# 修改方式二：
personinfo = PeopleInfo.objects.filter(name='虚竹').update(name='传智播客')

# 删除方式一：
person = PeopleInfo.objects.get(name='传智播客')
person.delete()

# 删除方式二：
Book.object.filter(name='袁紫衣').delete()



