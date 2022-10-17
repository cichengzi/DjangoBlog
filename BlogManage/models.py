from django.contrib.auth.models import User
from django.db import models
import datetime

# Create your models here.


class Document(models.Model):
    doc_id = models.IntegerField(unique=True)  # 文档编号，唯一标识文档
    doc_class_id = models.IntegerField()  # 文档类别编号
    doc_title = models.CharField(max_length=50, unique=True)  # 文档名称
    doc_content = models.TextField()  # 文档内容
    doc_pub_date = models.DateTimeField()  # 文档发布时间
    doc_publisher_id = models.IntegerField(default=1)  # 文档发布者
    doc_type = models.IntegerField(default=0)  # 文档类型，0为普通文档，1为博客，2为项目

    def get_publisher(self):
        return User.objects.get(id=self.doc_publisher_id)

    def __str__(self):
        return f'[doc title: {self.doc_title}, doc publisher: {self.get_publisher()}]'


class DocumentClass(models.Model):
    doc_class_id = models.IntegerField(unique=True)  # 文档类别编号
    doc_class_title = models.CharField(max_length=50)  # 文档类别名称

    def get_documents(self):
        return list(Document.objects.filter(doc_class_id=self.doc_class_id))

    def __str__(self):
        return f'[doc class title: {self.doc_class_title}]'


class Util:
    @staticmethod
    def exist_document(doc_id: int) -> bool:
        return len(Document.objects.filter(doc_id=doc_id)) > 0

    @staticmethod
    def exist_document_class(doc_class_id: int) -> bool:
        return len(DocumentClass.objects.filter(doc_class_id=doc_class_id)) > 0

    @staticmethod
    def get_documents():
        return Document.objects.all()

    @staticmethod
    def get_document_classes():
        return DocumentClass.objects.all()

    @staticmethod
    def clear_documents():
        Document.objects.all().delete()

    @staticmethod
    def clear_document_classes():
        DocumentClass.objects.all().delete()

    @staticmethod
    def num_of_documents():
        return len(Document.objects.all())

    @staticmethod
    def num_of_document_classes():
        return len(DocumentClass.objects.all())


class Add:
    @staticmethod
    def add_document(doc_class_id: int, doc_title: str, doc_content: str,
                     doc_publisher_id: int, doc_type: int) -> int:
        doc_id = 1 if len(Document.objects.all()) == 0 else Document.objects.last().doc_id + 1
        doc_pub_date = datetime.datetime.now().replace(microsecond=0)
        document = Document(doc_id=doc_id, doc_class_id=doc_class_id, doc_title=doc_title, doc_content=doc_content,
                            doc_pub_date=doc_pub_date, doc_publisher_id=doc_publisher_id, doc_type=doc_type)
        document.save()
        return doc_id

    @staticmethod
    def add_document_class(doc_class_title: str) -> int:
        doc_class_id = 1 if len(DocumentClass.objects.all()) == 0 else DocumentClass.objects.last().doc_class_id + 1
        document_class = DocumentClass(doc_class_id=doc_class_id, doc_class_title=doc_class_title)
        document_class.save()
        return doc_class_id


class Delete:
    @staticmethod
    def delete_document(doc_id: int) -> bool:
        if Util.exist_document(doc_id):
            Document.objects.filter(doc_id=doc_id).delete()
            return True
        else:
            return False

    @staticmethod
    def delete_document_class(doc_class_id: int) -> bool:
        if Util.exist_document_class(doc_class_id):
            DocumentClass.objects.filter(doc_class_id=doc_class_id).delete()
            return True
        else:
            return True


class Query:
    @staticmethod
    def query_document(doc_id: int) -> Document:
        return Document.objects.get(doc_id=doc_id) if Util.exist_document(doc_id) else None

    @staticmethod
    def query_document_class(doc_class_id: int) -> DocumentClass:
        return DocumentClass.objects.get(doc_class_id=doc_class_id) if Util.exist_document_class(doc_class_id) else None


class Modify:
    @staticmethod
    def modify_document_title(doc_id: int, doc_title: str) -> bool:
        if Util.exist_document(doc_id):
            Document.objects.filter(doc_id=doc_id).update(doc_title=doc_title)
            return True
        else:
            return False

    @staticmethod
    def modify_document_content(doc_id: int, doc_content: str) -> bool:
        if Util.exist_document(doc_id):
            Document.objects.filter(doc_id=doc_id).update(doc_content=doc_content)
            return True
        else:
            return False

    @staticmethod
    def modify_document_class_id(doc_id: int, doc_class_id: int) -> bool:
        if Util.exist_document(doc_id):
            Document.objects.filter(doc_id=doc_id).update(doc_class_id=doc_class_id)
            return True
        else:
            return False

    @staticmethod
    def modify_document_pub_date(doc_id: int, doc_pub_date: datetime.datetime) -> bool:
        if Util.exist_document(doc_id):
            Document.objects.filter(doc_id=doc_id).update(doc_pub_date=doc_pub_date)
            return True
        else:
            return False

    @staticmethod
    def modify_document_class_title(doc_class_id: int, doc_class_title: str) -> bool:
        if Util.exist_document_class(doc_class_id):
            DocumentClass.objects.filter(doc_class_id=doc_class_id).update(doc_class_title=doc_class_title)
            return True
        else:
            return False


class ModelOperation:
    @staticmethod
    def exist_document(doc_id: int) -> bool:
        return Util.exist_document(doc_id)

    @staticmethod
    def exist_document_class(doc_class_id: int) -> bool:
        return Util.exist_document_class(doc_class_id)

    @staticmethod
    def add_document(doc_class_id: int, doc_title: str, doc_content: str,
                     doc_publisher_id: int, doc_type: int) -> int:
        return Add.add_document(doc_class_id, doc_title, doc_content, doc_publisher_id, doc_type)

    @staticmethod
    def add_document_class(doc_class_title: str) -> int:
        return Add.add_document_class(doc_class_title)

    @staticmethod
    def delete_document(doc_id: int) -> bool:
        return Delete.delete_document(doc_id)

    @staticmethod
    def delete_document_class(doc_class_id: int) -> bool:
        return Delete.delete_document_class(doc_class_id)

    @staticmethod
    def query_document(doc_id: int) -> Document:
        return Query.query_document(doc_id)

    @staticmethod
    def query_document_class(doc_class_id: int) -> DocumentClass:
        return Query.query_document_class(doc_class_id)

    @staticmethod
    def modify_document_title(doc_id: int, doc_title: str) -> bool:
        return Modify.modify_document_title(doc_id, doc_title)

    @staticmethod
    def modify_document_content(doc_id: int, doc_content: str) -> bool:
        return Modify.modify_document_content(doc_id, doc_content)

    @staticmethod
    def modify_document_pub_date(doc_id: int, doc_pub_date: datetime.datetime) -> bool:
        return Modify.modify_document_pub_date(doc_id, doc_pub_date)

    @staticmethod
    def modify_document_class_id(doc_id: int, doc_class_id: int) -> bool:
        return Modify.modify_document_class_id(doc_id, doc_class_id)

    @staticmethod
    def modify_document_class_title(doc_class_id: int, doc_class_title: str) -> bool:
        return Modify.modify_document_class_title(doc_class_id, doc_class_title)

    @staticmethod
    def get_documents():
        return Util.get_documents()

    @staticmethod
    def get_document_classes():
        return Util.get_document_classes()

    @staticmethod
    def clear_documents():
        Util.clear_documents()

    @staticmethod
    def clear_document_classes():
        Util.clear_document_classes()

    @staticmethod
    def num_of_documents():
        return Util.num_of_documents()

    @staticmethod
    def num_of_document_classes():
        return Util.num_of_document_classes()

