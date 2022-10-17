from django.test import TestCase
from . import models
import datetime
# Create your tests here.


class AutoTest(TestCase):
    def test_create_document(self):
        doc = models.Document(doc_id=-1, doc_class_id=-1, doc_title='test doc title', doc_content='test doc content',
                              doc_pub_date=datetime.datetime(year=2022, month=10, day=14, hour=17, minute=15, second=7),
                              doc_publisher_id=1, doc_type=1)

        self.assertEqual(doc.doc_id, -1)
        self.assertEqual(doc.doc_class_id, -1)
        self.assertEqual(doc.doc_title, 'test doc title')
        self.assertEqual(doc.doc_content, 'test doc content')
        self.assertEqual(doc.doc_pub_date.year, 2022)
        self.assertEqual(doc.doc_pub_date.month, 10)
        self.assertEqual(doc.doc_pub_date.day, 14)
        self.assertEqual(doc.doc_pub_date.hour, 17)
        self.assertEqual(doc.doc_pub_date.minute, 15)
        self.assertEqual(doc.doc_pub_date.second, 7)
        self.assertEqual(doc.doc_publisher_id, 1)
        self.assertEqual(doc.doc_type, 1)

    def test_create_document_class(self):
        doc_class = models.DocumentClass(doc_class_id=-1, doc_class_title='doc class title')
        self.assertEqual(doc_class.doc_class_id, -1)
        self.assertEqual(doc_class.doc_class_title, 'doc class title')

    def test_add_document(self):
        models.ModelOperation.clear_documents()

        self.assertEqual(models.ModelOperation.add_document(doc_class_id=0, doc_title='doc title 1', doc_content='doc content 1', doc_publisher_id=1, doc_type=0), 1)
        self.assertEqual(models.ModelOperation.add_document(doc_class_id=0, doc_title='doc title 2', doc_content='doc content 2', doc_publisher_id=1, doc_type=1), 2)

        self.assertEqual(models.ModelOperation.query_document(1).doc_title, 'doc title 1')
        self.assertEqual(models.ModelOperation.query_document(1).doc_content, 'doc content 1')
        self.assertEqual(models.ModelOperation.query_document(1).doc_type, 0)

        self.assertEqual(models.ModelOperation.query_document(2).doc_title, 'doc title 2')
        self.assertEqual(models.ModelOperation.query_document(2).doc_content, 'doc content 2')
        self.assertEqual(models.ModelOperation.query_document(2).doc_type, 1)
        models.ModelOperation.clear_documents()

    def test_add_document_class(self):
        models.ModelOperation.clear_document_classes()

        self.assertEqual(models.ModelOperation.add_document_class(doc_class_title='doc class title 1'), 1)
        self.assertEqual(models.ModelOperation.add_document_class(doc_class_title='doc class title 2'), 2)

        self.assertEqual(models.ModelOperation.query_document_class(1).doc_class_title, 'doc class title 1')
        self.assertEqual(models.ModelOperation.query_document_class(2).doc_class_title, 'doc class title 2')

        models.ModelOperation.clear_document_classes()

    def test_delete_document(self):
        models.ModelOperation.clear_documents()

        models.ModelOperation.add_document(doc_class_id=0, doc_title='doc title 1', doc_content='doc content 1', doc_publisher_id=1, doc_type=0)
        models.ModelOperation.add_document(doc_class_id=1, doc_title='doc title 2', doc_content='doc content 2', doc_publisher_id=1, doc_type=1)

        self.assertIs(models.ModelOperation.exist_document(1), True)
        self.assertIs(models.ModelOperation.exist_document(2), True)

        models.ModelOperation.delete_document(1)
        models.ModelOperation.delete_document(2)

        self.assertIs(models.ModelOperation.exist_document(1), False)
        self.assertIs(models.ModelOperation.exist_document(2), False)

        models.ModelOperation.clear_documents()

    def test_delete_document_class(self):
        models.ModelOperation.clear_document_classes()

        models.ModelOperation.add_document_class(doc_class_title='doc class title 1')
        models.ModelOperation.add_document_class(doc_class_title='doc class title 2')

        self.assertIs(models.ModelOperation.exist_document_class(1), True)
        self.assertIs(models.ModelOperation.exist_document_class(2), True)

        models.ModelOperation.delete_document_class(1)
        models.ModelOperation.delete_document_class(2)

        self.assertIs(models.ModelOperation.exist_document_class(1), False)
        self.assertIs(models.ModelOperation.exist_document_class(2), False)

        models.ModelOperation.clear_document_classes()

    def test_clear_documents(self):
        models.ModelOperation.clear_documents()

        models.ModelOperation.add_document(doc_class_id=0, doc_title='doc title 1', doc_content='doc content 1', doc_publisher_id=1, doc_type=0)
        models.ModelOperation.add_document(doc_class_id=0, doc_title='doc title 2', doc_content='doc content 2', doc_publisher_id=1, doc_type=0)

        models.ModelOperation.clear_documents()

        self.assertEqual(models.ModelOperation.num_of_documents(), 0)

    def test_clear_document_classes(self):
        models.ModelOperation.clear_document_classes()

        models.ModelOperation.add_document_class(doc_class_title='doc class title 1')
        models.ModelOperation.add_document_class(doc_class_title='doc class title 2')

        models.ModelOperation.clear_document_classes()

        self.assertEqual(models.ModelOperation.num_of_document_classes(), 0)

    def test_query_document(self):
        models.ModelOperation.clear_documents()

        models.ModelOperation.add_document(doc_class_id=0, doc_title='doc title 1', doc_content='doc content 1', doc_publisher_id=1, doc_type=0)
        models.ModelOperation.add_document(doc_class_id=0, doc_title='doc title 2', doc_content='doc content 2', doc_publisher_id=1, doc_type=0)
        models.ModelOperation.add_document(doc_class_id=0, doc_title='doc title 3', doc_content='doc content 3', doc_publisher_id=1, doc_type=0)

        self.assertEqual(models.ModelOperation.query_document(1).doc_title, 'doc title 1')
        self.assertEqual(models.ModelOperation.query_document(1).doc_content, 'doc content 1')
        self.assertEqual(models.ModelOperation.query_document(1).doc_type, 0)

        self.assertEqual(models.ModelOperation.query_document(2).doc_title, 'doc title 2')
        self.assertEqual(models.ModelOperation.query_document(2).doc_content, 'doc content 2')
        self.assertEqual(models.ModelOperation.query_document(2).doc_type, 0)

        self.assertEqual(models.ModelOperation.query_document(3).doc_title, 'doc title 3')
        self.assertEqual(models.ModelOperation.query_document(3).doc_content, 'doc content 3')
        self.assertEqual(models.ModelOperation.query_document(3).doc_type, 0)

        models.ModelOperation.clear_documents()

    def test_query_document_class(self):
        models.ModelOperation.clear_document_classes()

        models.ModelOperation.add_document_class(doc_class_title='doc class title 1')
        models.ModelOperation.add_document_class(doc_class_title='doc class title 2')
        models.ModelOperation.add_document_class(doc_class_title='doc class title 3')

        self.assertEqual(models.ModelOperation.query_document_class(1).doc_class_title, 'doc class title 1')
        self.assertEqual(models.ModelOperation.query_document_class(2).doc_class_title, 'doc class title 2')
        self.assertEqual(models.ModelOperation.query_document_class(3).doc_class_title, 'doc class title 3')

        models.ModelOperation.clear_document_classes()

    def test_modify_document(self):
        models.ModelOperation.clear_documents()

        models.ModelOperation.add_document(doc_class_id=0, doc_title='doc title 1', doc_content='doc content 1', doc_publisher_id=1, doc_type=0)
        models.ModelOperation.add_document(doc_class_id=0, doc_title='doc title 2', doc_content='doc content 2', doc_publisher_id=1, doc_type=0)
        models.ModelOperation.add_document(doc_class_id=0, doc_title='doc title 3', doc_content='doc content 3', doc_publisher_id=1, doc_type=0)

        self.assertEqual(models.ModelOperation.query_document(1).doc_title, 'doc title 1')
        self.assertEqual(models.ModelOperation.query_document(2).doc_title, 'doc title 2')
        self.assertEqual(models.ModelOperation.query_document(3).doc_title, 'doc title 3')
        self.assertEqual(models.ModelOperation.query_document(1).doc_content, 'doc content 1')
        self.assertEqual(models.ModelOperation.query_document(2).doc_content, 'doc content 2')
        self.assertEqual(models.ModelOperation.query_document(3).doc_content, 'doc content 3')

        models.ModelOperation.modify_document_title(1, 'new doc title 1')
        models.ModelOperation.modify_document_title(2, 'new doc title 2')
        models.ModelOperation.modify_document_title(3, 'new doc title 3')
        models.ModelOperation.modify_document_content(1, 'new doc content 1')
        models.ModelOperation.modify_document_content(2, 'new doc content 2')
        models.ModelOperation.modify_document_content(3, 'new doc content 3')

        self.assertEqual(models.ModelOperation.query_document(1).doc_title, 'new doc title 1')
        self.assertEqual(models.ModelOperation.query_document(2).doc_title, 'new doc title 2')
        self.assertEqual(models.ModelOperation.query_document(3).doc_title, 'new doc title 3')
        self.assertEqual(models.ModelOperation.query_document(1).doc_content, 'new doc content 1')
        self.assertEqual(models.ModelOperation.query_document(2).doc_content, 'new doc content 2')
        self.assertEqual(models.ModelOperation.query_document(3).doc_content, 'new doc content 3')

        models.ModelOperation.clear_documents()

    def test_modify_document_class(self):
        models.ModelOperation.clear_document_classes()

        models.ModelOperation.add_document_class(doc_class_title='doc class title 1')
        models.ModelOperation.add_document_class(doc_class_title='doc class title 2')
        models.ModelOperation.add_document_class(doc_class_title='doc class title 3')

        self.assertEqual(models.ModelOperation.query_document_class(1).doc_class_title, 'doc class title 1')
        self.assertEqual(models.ModelOperation.query_document_class(2).doc_class_title, 'doc class title 2')
        self.assertEqual(models.ModelOperation.query_document_class(3).doc_class_title, 'doc class title 3')

        models.ModelOperation.modify_document_class_title(1, 'new doc class title 1')
        models.ModelOperation.modify_document_class_title(2, 'new doc class title 2')
        models.ModelOperation.modify_document_class_title(3, 'new doc class title 3')

        self.assertEqual(models.ModelOperation.query_document_class(1).doc_class_title, 'new doc class title 1')
        self.assertEqual(models.ModelOperation.query_document_class(2).doc_class_title, 'new doc class title 2')
        self.assertEqual(models.ModelOperation.query_document_class(3).doc_class_title, 'new doc class title 3')

        models.ModelOperation.clear_document_classes()