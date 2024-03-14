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
