from django.contrib import admin

# Register your models here.
# 导入模型
from Book.models import Book,PeopleInfo
# 注册书籍模型
admin.site.register(Book)
# 注册人物模型
admin.site.register(PeopleInfo)