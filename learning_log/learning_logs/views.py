from django.shortcuts import render

from .models import Topic

# Create your views here.


def index(request):
    """ 学习笔记的主页 """
    return render(request, 'learning_logs/index.html')


def topics(request):  # django 从服务器那里收到的 request 对象
    """ 显示所有的主题 """
    topics_v = Topic.objects.order_by('date_added')  # 询数据库 —— 请求提供 Topic
    # 对象,并按属性 date_added 对它们进行排序
    context = {'topics': topics_v}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """ 显示单个主题及其所有的条目 """
    topic_v = Topic.objects.get(id=topic_id)
    entries = topic_v.entry_set.order_by('-date_added')
    context = {'topic': topic_v, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
