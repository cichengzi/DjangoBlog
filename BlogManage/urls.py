from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_home, name='home'),
    path('docs/<int:doc_id>/', views.page_docs, name='docs'),
    path('blog/', views.page_blog, name='blog'),
    path('examples/', views.page_examples, name='examples'),
    path('about/', views.page_about, name='about'),
    path('search/', views.page_search, name='search'),
    path('add_doc/', views.page_add_doc, name='add_doc'),
    path('delete_doc/<int:doc_id>', views.page_delete_doc, name='delete_doc'),
    path('modify_doc/<int:doc_id>', views.page_modify_doc, name='modify_doc'),
    path('404/', views.page_404, name='404'),
    path('sign_in/', views.page_sign_in, name='sign_in'),
]