from django import forms
from . import models
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    search_content = forms.CharField(label='search content', max_length=100)


class DocumentForm(forms.Form):
    doc_class_id = forms.ChoiceField(label='doc class id', choices=tuple([(doc_class.doc_class_id, doc_class.doc_class_title) for doc_class in models.DocumentClass.objects.all()]))  # 文档分类的编号
    doc_title = forms.CharField(label='doc title', max_length=50)  # 文档标题
    doc_content = forms.CharField(label='doc content', max_length=1000)  # 文档内容
    doc_publisher_id = forms.ChoiceField(label='doc publisher id', choices=tuple([(user.id, user.id) for user in User.objects.all()]))
    doc_type = forms.IntegerField(label='doc type')


class ModifyDocumentForm(forms.Form):
    doc_class_id = forms.ChoiceField(label='doc class id', choices=tuple([(doc_class.doc_class_id, doc_class.doc_class_title) for doc_class in models.DocumentClass.objects.all()]))  # 文档分类的编号
    doc_title = forms.CharField(label='doc title', max_length=50)  # 文档标题
    doc_content = forms.CharField(label='doc content', max_length=1000)  # 文档内容


class SignInForm(forms.Form):
    username = forms.CharField(label='username', max_length=50)  # 用户名
    password = forms.CharField(label='password', max_length=50)  # 密码