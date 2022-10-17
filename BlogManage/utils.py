import markdown
import string
import nltk
from zhon.hanzi import punctuation
from django.utils.safestring import mark_safe
from . import models


extensions = [
    'markdown.extensions.extra',
    'markdown.extensions.codehilite',
    'markdown.extensions.toc',
    'markdown.extensions.tables',
    'markdown.extensions.fenced_code',
]


def get_mark_safe_doc(doc: models.Document) -> models.Document:  # 让前端能够正确显示markdown转换的html
    doc.doc_content = markdown.markdown(doc.doc_content, extensions=extensions)
    doc.doc_content = mark_safe(doc.doc_content)
    return doc


def tokenize(doc_content: str) -> list:
    other_tokens = []  # 存储英文字符意外的其他字符
    new_doc_content = ''  # 去掉非英文字符后的新doc content
    for ch in doc_content:  # 遍历doc content
        if ord(ch) > 256:  # 如果非英文字符
            other_tokens.append(ch)  # 将ch添加到other_tokens
            new_doc_content += ' '  # new doc content添加一个空格
        else:  # 如果英文字符
            new_doc_content += ch  # new doc content连接上ch
    en_tokens = nltk.word_tokenize(new_doc_content)  # 对new doc content进行分词
    tokens = en_tokens + other_tokens  # 拼接两个tokens
    punctuations = string.punctuation + punctuation  # 获取中文标点和英文标点
    for p in punctuations:
        if p in tokens:
            tokens.remove(p)  # 从tokens中删掉所有标点
    return tokens


def query_similar_documents(search_content, threshold=0.01):
    def get_similarity(c1, c2):
        intersection = set(tokenize(c1)).intersection(set(tokenize(c2)))
        union = set(tokenize(c1)).union(set(tokenize(c2)))
        return len(intersection) / len(union)

    documents = []
    for doc in models.ModelOperation.get_documents():
        if get_similarity(doc.doc_content, search_content) >= threshold:
            documents.append(doc)
    return documents
