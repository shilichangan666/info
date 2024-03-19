from django.db import models

# Create your models here.
"""
1.  我们的模型类需要继承自model.Model
2.  系统会自动为我们添加一个主键--id
3.  字段
    字段名=model.类型（选项）
    
    字段名就是数据表的字段名
    
    char(M)
    varchar(M)
    M就是选项
"""


class Book(models.Model):
    name = models.CharField(max_length=10,verbose_name='名称')
    pub_data = models.DateField(verbose_name='发布日期',null=True)
    readcount = models.IntegerField(default=0,verbose_name='阅读量')
    commentcount = models.IntegerField(default=0,verbose_name='评论量')
    is_delete = models.BooleanField(default=False,verbose_name='逻辑删除')

    class Meta:
        db_table = 'bookinfo' # 指明数据库表名
        verbose_name = '图书' # 在admin站点中显示的名称
    def __str__(self):
        """将模型类以字符串的方式输出"""
        return self.name


class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0,'male'),
        (1,'female')
    )
    name = models.CharField(max_length=10,verbose_name='名称')
    gender = models.BooleanField(choices=GENDER_CHOICES,default=0,verbose_name='性别')
    discription = models.CharField(max_length=200,null=True,verbose_name='描述信息')
    book = models.ForeignKey(Book,on_delete=models.CASCADE,verbose_name='图书')
    is_delete = models.BooleanField(default=False,verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name


