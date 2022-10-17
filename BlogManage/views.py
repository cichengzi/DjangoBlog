from django.shortcuts import render
from . import forms
from django.shortcuts import HttpResponseRedirect
from . import models
import datetime
from . import utils
# Create your views here.


def page_home(request):
    if request.method == 'POST':
        search_form = forms.SearchForm(request.POST)
        if search_form.is_valid():
            search_content = search_form.cleaned_data.get('search_content')
            return HttpResponseRedirect(f'/search/?search_content={search_content}')
    else:
        search_form = forms.SearchForm()
    return render(request, 'home.html', {'search_form': search_form})


def page_docs(request, doc_id: int = 0):
    """
        显示文档的页面
        :param request: WSGIRequest
        :param doc_id: int
        :return:
        """
    context = {'doc_class_list': []}
    for doc_class in models.DocumentClass.objects.all():
        items = {'doc_class_title': doc_class.doc_class_title, 'doc_list': doc_class.get_documents(),
                 'doc_class_name': str('-'.join(doc_class.doc_class_title.split(' ')))}
        context['doc_class_list'].append(items)

    if not models.ModelOperation.exist_document(doc_id):
        return HttpResponseRedirect('/404')
    current_doc = models.ModelOperation.query_document(doc_id)  # 获取doc_id对应的Doc对象
    current_doc = utils.get_mark_safe_doc(current_doc)  # 将current_doc的doc_content转换成html

    context['current_doc'] = current_doc  # 当前文档

    if request.method == 'POST':
        search_form = forms.SearchForm(request.POST)  # 获取SearchForm表单
        if search_form.is_valid():  # 如果合法form
            search_content = search_form.cleaned_data.get('search_content')  # 获取当前搜索的内容
            return HttpResponseRedirect(f'/search/?search_content={search_content}')  # 重定向
    else:
        search_form = forms.SearchForm()

    context['search_form'] = search_form  # 当前搜索表单
    return render(request, 'docs.html', context)


def page_add_doc(request):
    if request.method == 'POST':
        doc_form = forms.DocumentForm(request.POST)
        if doc_form.is_valid():
            doc_class_id = int(doc_form.cleaned_data.get('doc_class_id'))
            doc_title = doc_form.cleaned_data.get('doc_title')
            doc_content = doc_form.cleaned_data.get('doc_content')
            doc_publisher_id = int(doc_form.cleaned_data.get('doc_publisher_id'))
            doc_type = doc_form.cleaned_data.get('doc_type')
            doc_id = models.ModelOperation.add_document(doc_class_id, doc_title, doc_content, doc_publisher_id, doc_type)
            return HttpResponseRedirect(f'/docs/{doc_id}')
    else:
        doc_form = forms.DocumentForm()
    return render(request, 'add_doc.html', {'doc_form': doc_form})


def page_delete_doc(request, doc_id: int = -1):
    if models.ModelOperation.exist_document(doc_id):
        models.ModelOperation.delete_document(doc_id)
    return HttpResponseRedirect(f'/')


def page_modify_doc(request, doc_id: int = -1):
    if request.method == 'POST':
        modify_doc_form = forms.ModifyDocumentForm(request.POST)
        if modify_doc_form.is_valid():
            doc_class_id = int(modify_doc_form.cleaned_data.get('doc_class_id'))
            doc_title = modify_doc_form.cleaned_data.get('doc_title')
            doc_content = modify_doc_form.cleaned_data.get('doc_content')

            models.ModelOperation.modify_document_title(doc_id, doc_title)
            models.ModelOperation.modify_document_content(doc_id, doc_content)
            models.ModelOperation.modify_document_pub_date(doc_id, datetime.datetime.now().replace(microsecond=0))
            models.ModelOperation.modify_document_class_id(doc_id, doc_class_id)
            return HttpResponseRedirect(f'/docs/{doc_id}')
    else:
        modify_doc_form = forms.ModifyDocumentForm()
    return render(request, 'modify_doc.html', {'modify_doc_form': modify_doc_form})


def page_blog(request):
    if request.method == 'POST':
        search_form = forms.SearchForm(request.POST)
        if search_form.is_valid():
            search_content = search_form.cleaned_data.get('search_content')
            return HttpResponseRedirect(f'/search/?search_content={search_content}')
    else:
        search_form = forms.SearchForm()
    return render(request, 'blog.html', {'search_form': search_form})


def page_examples(request):
    if request.method == 'POST':
        search_form = forms.SearchForm(request.POST)
        if search_form.is_valid():
            search_content = search_form.cleaned_data.get('search_content')
            return HttpResponseRedirect(f'/search/?search_content={search_content}')
    else:
        search_form = forms.SearchForm()
    return render(request, 'examples.html', {'search_form': search_form})


def page_about(request):
    if request.method == 'POST':
        search_form = forms.SearchForm(request.POST)
        if search_form.is_valid():
            search_content = search_form.cleaned_data.get('search_content')
            return HttpResponseRedirect(f'/search/?search_content={search_content}')
    else:
        search_form = forms.SearchForm()
    return render(request, 'about.html', {'search_form': search_form})


def page_search(request):
    if request.method == 'POST':
        search_form = forms.SearchForm(request.POST)
        if search_form.is_valid():
            search_content = search_form.cleaned_data.get('search_content')
            return HttpResponseRedirect(f'/search/?search_content={search_content}')
    else:
        search_form = forms.SearchForm()

    search_content = request.GET.get('search_content', '')
    docs = utils.query_similar_documents(search_content) if len(search_content) > 0 else []
    return render(request, 'search.html', {'docs': docs, 'search_form': search_form})


def page_404(request):
    return render(request, '404.html')


def page_sign_in(request):
    return render(request, 'sign_in.html')