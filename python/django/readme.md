<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [初识 Django](#初识-django)
- [请求和响应](#请求和响应)
  - [1. 快速安装指南](#1-快速安装指南)
    - [1. 虚拟环境准备](#1-虚拟环境准备)
  - [2. 请求和响应](#2-请求和响应)
    - [1. Create project and app](#1-create-project-and-app)
    - [2. Write your first view](#2-write-your-first-view)
    - [3. path() 的四个参数](#3-path-的四个参数)
- [模型和 admin 站点](#模型和-admin-站点)
  - [1. Database setup](#1-database-setup)
  - [2. Creating models](#2-creating-models)
  - [3. Include the app in our project](#3-include-the-app-in-our-project)
  - [4. Activating models](#4-activating-models)
  - [5. Playing with the API](#5-playing-with-the-api)
  - [6. Creating an admin user](#6-creating-an-admin-user)
  - [7. Make the poll app modifiable in the admin](#7-make-the-poll-app-modifiable-in-the-admin)
- [视图和模板](#视图和模板)
  - [1. 编写更多视图](#1-编写更多视图)
  - [2. 写一个真正有用的视图](#2-写一个真正有用的视图)
  - [3. 快捷函数 render()](#3-快捷函数-render)
  - [4. 快捷函数 get_object_or_404()](#4-快捷函数-get_object_or_404)
  - [5. 使用模板系统](#5-使用模板系统)
  - [6. 去掉模板中的硬编码 URL](#6-去掉模板中的硬编码-url)
  - [7. 为 URL 名称添加命名空间](#7-为-url-名称添加命名空间)
- [表单和通用视图](#表单和通用视图)
  - [1. 简单的表单](#1-简单的表单)
  - [2. 使用通用视图](#2-使用通用视图)
- [测试](#测试)
  - [1. 创建一个测试](#1-创建一个测试)
  - [2. 运行测试](#2-运行测试)
  - [3. 修复 bug](#3-修复-bug)
  - [4. 更全面的测试](#4-更全面的测试)
  - [5. 测试视图](#5-测试视图)
- [静态文件](#静态文件)
  - [1. 自定义 _应用_ 的界面和风格](#1-自定义-_应用_-的界面和风格)
  - [2. 添加一个背景图](#2-添加一个背景图)
- [自定义 admin 站点](#自定义-admin-站点)
  - [1. 自定义后台表单](#1-自定义后台表单)
  - [2. 添加关联的对象](#2-添加关联的对象)
  - [3. 自定义后台更改列表](#3-自定义后台更改列表)
  - [4. 自定义后台界面和风格](#4-自定义后台界面和风格)
  - [5. 修改管理站点标题头](#5-修改管理站点标题头)
- [可复用的应用](#可复用的应用)
  - [1. 安装必须环境](#1-安装必须环境)
  - [2. 打包应用](#2-打包应用)
  - [3. 使用你自己的包名](#3-使用你自己的包名)
  - [4. 发布你的应用](#4-发布你的应用)
  - [5. 通过 virtualenv 安装 Python 包](#5-通过-virtualenv-安装-python-包)
- [单独使用 django orm](#单独使用-django-orm)
- [连接 SQL Server](#连接-sql-server)
  - [1. 引入模块](#1-引入模块)
  - [2. 创建数据源](#2-创建数据源)
  - [3. 配置 setting.py](#3-配置-settingpy)
- [settings](#settings)
  - [时区设置](#时区设置)
  - [语言设置](#语言设置)

<!-- /code_chunk_output -->

# 初识 Django

设计模型 -> 应用数据模型 -> 使用 API 访问数据库 -> 注册模型到管理站点

规划 URLs -> 编写试图 -> 设计模板

# 请求和响应

## 1. 快速安装指南

### 1. 虚拟环境准备

1. Linux 系统

```bash
# 创建虚拟环境
$ virtualenv --no-site-packages venv
# 进入虚拟环境
$ cd venv
$ source /bin/activate
# 退出虚拟环境
$ deactivate
```

2. Windows 系统

```cmd
rem 进入虚拟环境
> cd venv/Scripts
> activate
rem 退出虚拟环境
> deactivate
```

3. install an official release

```bash
$ pip install Django
```

4. Verifying

```python
>>> import django
>>> print(django.get_version())
```

```bash
# -m 相当于将 django以模块引入后执行
$ python -m django --version
```

## 2. 请求和响应

### 1. Create project and app

```bash
# Creating a project
$ django-admin startproject datamaster
# 初始化 db
$ python manage.py migrate
# The development server
$ python manage.py runserver [ip:port]
# Creating the Polls app
$ python manage.py startapp dashboard
```

### 2. Write your first view

```python
# 在 dashboard/views.py 编写一个url请求的相应
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

```python
# 给 dashboard创建urls.py，设置urlpatterns
# 设置 dashboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

```python
# 在 datamaster/urls.py 将 dashboard 的urls 包含进去
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),
]
```

### 3. path() 的四个参数

route(必录)：是一个匹配 URL 的准则（类似正则表达式）。当 Django 响应一个请求时，它会从 `urlpatterns` 的第一项开始，按顺序依次匹配列表中的项，直到找到匹配的项。

view(必录)：当 Django 找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个 [`HttpRequest`](https://docs.djangoproject.com/zh-hans/2.1/ref/request-response/#django.http.HttpRequest) 对象作为第一个参数，被“捕获”的参数以关键字参数的形式传入。稍后，我们会给出一个例子。

kwargs(可选)：任意个关键字参数可以作为一个字典传递给目标视图函数。

name(可选)：为你的 URL 取名能使你在 Django 的任意地方唯一地引用它，尤其是在模板中。这个有用的特性允许你只改一个文件就能全局地修改某个 URL 模式。

# 模型和 admin 站点

## 1. Database setup

```bash
$ pip install mysqlclient
```

## 2. Creating models

```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

## 3. Include the app in our project

```python
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

## 4. Activating models

```bash
# 生成迁移文件
$ python manage.py makemigrations polls
# 执行指定迁移
$ python manage.py migrate polls 0001
# 执行全部迁移
$ python manage.py migrate
```

## 5. Playing with the API

```bash
# 进入Database API
$ python manage.py shell
```

```python
# Import the model classes we just wrote.
>>> from polls.models import Choice, Question

# No questions are in the system yet.
>>> Question.objects.all()
<QuerySet []>

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID.
>>> q.id
1

# Access model field values via Python attributes.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# Change values by changing the attributes, then calling save().
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() displays all the questions in the database.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
```

```python
# 通过给polls/models.py 中的模型添加__str__()方法
# 让Question.objects.all()的调用显示对于的值
from django.db import models

class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
```

```python
>>> from polls.models import Choice, Question

# Make sure our __str__() addition worked.
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith='What')
<QuerySet [<Question: What's up?>]>

# Get the question that was published this year.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: What's up?>

# Make sure our custom method worked.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
>>> q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
<QuerySet []>

# Create three choices.
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Question objects.
>>> c.question
<Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Let's delete one of the choices. Use delete() for that.
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
```

## 6. Creating an admin user

```bash
$ python manage.py createsuperuser
Username: admin
Email address: admin@example.com
Password: **********
Password (again): *********
Superuser created successfully.
```

## 7. Make the poll app modifiable in the admin

```python
# polls/admin.py
from django.contrib import admin
from .models import Question

admin.site.register(Question)
```

# 视图和模板

## 1. 编写更多视图

```python
# polls/views.py
# views response
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

```python
# polls/urls.py
# adding the following path calls
from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

## 2. 写一个真正有用的视图

```python
# polls/views.py
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

# Leave the rest of the views (detail, results, vote) unchanged
```

```python
# polls/templates/polls/index.html
# Put the following code in that template
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

```python
# polls/views.py
# update our index view in polls/views.py to use the template
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

## 3. 快捷函数 render()

```python
# polls/views.py
from django.shortcuts import render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```

## 4. 快捷函数 get_object_or_404()

```python
# polls/views.py
# Raising a 404 error
from django.http import Http404
from django.shortcuts import render

from .models import Question
# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
```

```html
<!-- polls/templates/polls/detail.html -->
{{ question }}
```

```python
# polls/views.py
from django.shortcuts import get_object_or_404, render
from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```

## 5. 使用模板系统

```html
<!-- polls/templates/polls/detail.html -->
<h1>{{ question.question_text }}</h1>
<ul>
  {% for choice in question.choice_set.all %}
  <li>{{ choice.choice_text }}</li>
  {% endfor %}
</ul>
```

## 6. 去掉模板中的硬编码 URL

```html
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li></pre>
```

```python
# the 'name' value as called by the {% url %} template tag
path('<int:question_id>/', views.detail, name='detail'),
# added the word 'specifics'
path('specifics/<int:question_id>/', views.detail, name='detail'),
```

## 7. 为 URL 名称添加命名空间

```python
# polls/urls.py
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

```html
polls/templates/polls/index.html
<li>
  <a href="{% url 'detail' question.id %}">{{ question.question_text }}</a>
</li>
to point at the namespaced detail view:
```

```html
<!-- 指定命名空间 -->
polls/templates/polls/index.html
<li>
  <a href="{% url 'polls:detail' question.id %}"
    >{{ question.question_text }}</a
  >
</li>
```

# 表单和通用视图

## 1. 简单的表单

```html
<!-- polls/templates/polls/detail.html -->
<h1>{{ question.question_text }}</h1>

{% if error_message %}
<p><strong>{{ error_message }}</strong></p>
{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
  {% csrf_token %} {% for choice in question.choice_set.all %}
  <input
    type="radio"
    name="choice"
    id="choice{{ forloop.counter }}"
    value="{{ choice.id }}"
  />
  <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label
  ><br />
  {% endfor %}
  <input type="submit" value="Vote" />
</form>
```

```python
# polls/urls.py
path('<int:question_id>/vote/', views.vote, name='vote'),
```

```python
# polls/views.py
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question
# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

```python
# polls/views.py
from django.shortcuts import get_object_or_404, render

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
```

```html
<!-- polls/templates/polls/results.html -->
<h1>{{ question.question_text }}</h1>

<ul>
  {% for choice in question.choice_set.all %}
  <li>
    {{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize
    }}
  </li>
  {% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```

## 2. 使用通用视图

```python
# Amend URLconf
polls/urls.py
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

```python
# Amend views
# polls/views.py
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    ... # same as above, no changes needed.
```

# 测试

## 1. 创建一个测试

```bash
$ python manage.py shell
```

```python
# identify a bug
>>> import datetime
>>> from django.utils import timezone
>>> from polls.models import Question
>>> # create a Question instance with pub_date 30 days in the future
>>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
>>> # was it published recently?
>>> future_question.was_published_recently()
True
```

```python
# polls/tests.py
import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```

## 2. 运行测试

```bash
$ python manage.py test polls
```

```bash
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionModelTests)
----------------------------------------------------------------------
Traceback (most recent call last):
File "/path/to/mysite/polls/tests.py", line 16, in test_was_published_recently_with_future_question
    self.assertIs(future_question.was_published_recently(), False)
AssertionError: True is not False

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
Destroying test database for alias 'default'...
```

## 3. 修复 bug

```python
# polls/models.py
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

```bash
# run the test again
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
Destroying test database for alias 'default'...
```

## 4. 更全面的测试

```python
# polls/tests.py
def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() returns False for questions whose pub_date
    is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)

def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() returns True for questions whose pub_date
    is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)
```

## 5. 测试视图

```bash
# The Django test client
$ python manage.py shell
```

```python
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
```

```python
>>> from django.test import Client
>>> # create an instance of the client for our use
>>> client = Client()
```

```python
>>> # get a response from '/'
>>> response = client.get('/')
Not Found: /
>>> # we should expect a 404 from that address; if you instead see an
>>> # "Invalid HTTP_HOST header" error and a 400 response, you probably
>>> # omitted the setup_test_environment() call described earlier.
>>> response.status_code
404
>>> # on the other hand we should expect to find something at '/polls/'
>>> # we'll use 'reverse()' rather than a hardcoded URL
>>> from django.urls import reverse
>>> response = client.get(reverse('polls:index'))
>>> response.status_code
200
>>> response.content
b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#39;s up?</a></li>\n    \n    </ul>\n\n'
>>> response.context['latest_question_list']
<QuerySet [<Question: What's up?>]>
```

```python
# Improving our view
# polls/views.py
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
```

```python
# polls/views.py
from django.utils import timezone
```

```python
# polls/views.py
def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
```

```python
# Testing our new view
# polls/tests.py
# from django.urls import reverse
```

```python
# polls/tests.py
def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )
```

```python
# Testing the DetailView
# polls/views.py
class DetailView(generic.DetailView):
    ...
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
```

```python
# polls/tests.py
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
```

# 静态文件

## 1. 自定义 _应用_ 的界面和风格

```css
/* polls/static/polls/style.css */
li a {
  color: green;
}
```

```html
<!-- polls/templates/polls/index.html -->
{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}" />
```

## 2. 添加一个背景图

```css
/* polls/static/polls/style.css */
body {
  background: white url("images/background.gif") no-repeat;
}
```

# 自定义 admin 站点

## 1. 自定义后台表单

```python
# polls/admin.py
from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
```

```python
# polls/admin.py
from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
```

## 2. 添加关联的对象

```python
# polls/admin.py
from django.contrib import admin
from .models import Choice, Question
# ...
admin.site.register(Choice)
```

```python
# polls/admin.py
from django.contrib import admin
from .models import Choice, Question

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
```

```python
# polls/admin.py
class ChoiceInline(admin.TabularInline):
    #...
```

## 3. 自定义后台更改列表

```python
polls/admin.py
class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ('question_text', 'pub_date')
```

```python
# polls/admin.py
class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ('question_text', 'pub_date', 'was_published_recently')
```

```python
# polls/models.py
class Question(models.Model):
    # ...
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
```

```python
list_filter = ['pub_date']
```

```python
search_fields = ['question_text']
```

## 4. 自定义后台界面和风格

```python
# mysite/settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

```bash
# Where are the Django source files?
$ python -c "import django; print(django.__path__)"
```

```html
{% block branding %}
<h1 id="site-name">
  <a href="{% url 'admin:index' %}">Polls Administration</a>
</h1>
{% endblock %}
```

## 5. 修改管理站点标题头

```python
# settings.py
ADMIN_SITE_HEADER ="DataMaster"
```

```python
# urls.py
from django.conf import settings

admin.site.site_header = settings.ADMIN_SITE_HEADER
```

# 可复用的应用

## 1. 安装必须环境

```bash
# 使用 setuptools 打包程序
$ pip install setuptools
```

## 2. 打包应用

1. 首先，在你的 Django 项目目录外创建一个名为 `django-polls` 的文件夹，用于盛放 `polls`。
2. 将 `polls` 目录移入 `django-polls` 目录。
3. 创建一个名为 `django-polls/README.rst` 的文件，包含以下内容：

```bash
# django-polls/README.rst
=====
Polls
=====

Polls is a simple Django app to conduct Web-based polls. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'polls',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('polls/', include('polls.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.
```

4. 创建一个 `django-polls/LICENSE` 文件。选择一个非本教程使用的授权协议，但是要足以说明发布代码没有授权证书是 _不可能的_ 。Django 和很多兼容 Django 的应用是以 BSD 授权协议发布的；不过，你可以自己选择一个授权协议。只要确定你选择的协议能够限制未来会使用你的代码的人。
5. 下一步我们将创建 `setup.py` 用于说明如何构建和安装应用的细节。关于此文件的完整介绍超出了此教程的范围，但是 [setuptools docs](https://setuptools.readthedocs.io/en/latest/) 有详细的介绍。创建文件 `django-polls/setup.py` 包含以下内容：

```python
# django-polls/setup.py
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-polls',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',  # example license
    description='A simple Django app to conduct Web-based polls.',
    long_description=README,
    url='https://www.example.com/',
    author='Your Name',
    author_email='yourname@example.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: X.Y',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
```

6. 默认包中只包含 Python 模块和包。为了包含额外文件，我们需要创建一个名为 `MANIFEST.in` 的文件。上一步中关于 setuptools 的文档详细介绍了这个文件。为了包含模板、`README.rst` 和我们的 `LICENSE` 文件，创建文件 `django-polls/MANIFEST.in` 包含以下内容：

```in
django-polls/MANIFEST.in
include LICENSE
include README.rst
recursive-include polls/static *
recursive-include polls/templates *
```

7. 在应用中包含详细文档是可选的，但我们推荐你这样做。创建一个空目录 `django-polls/docs` 用于未来编写文档。额外添加一行至 `django-polls/MANIFEST.in`

```in
recursive-include docs *
```

8. 试着构建你自己的应用包通过 `ptyhon setup.py sdist` （在 ` django-polls``目录内）。这将创建一个名为 ``dist ` 的目录并构建你自己的应用包， `django-polls-0.1.tar.gz`。

## 3. 使用你自己的包名

```bash
$ pip install --user django-polls/dist/django-polls-0.1.tar.gz
$ pip uninstall django-polls
```

## 4. 发布你的应用

- 通过邮件将你的包发送给朋友。
- 将这个包上传至你的网站。
- 将你的包发布至公共仓库，比如 [the Python Package Index (PyPI)](https://docs.djangoproject.com/zh-hans/2.1/intro/reusable-apps/#the-python-package-index-pypi)。 [packaging.python.org](https://packaging.python.org/) 有一个不错的 [教程](https://packaging.python.org/distributing/#uploading-your-project-to-pypi) 说明如何发布至公共仓库。

## 5. 通过 virtualenv 安装 Python 包

​ 一般来说，这些状况只在你同时运行多个 Django 项目时出现。当这个问题出现时，最好的解决办法是使用 [virtualenv](https://virtualenv.pypa.io/)。这个工具允许你同时运行多个相互独立的 Python 环境，每个环境都有各自库和应用包命名空间的拷贝。

# 单独使用 django orm

```python
import os,django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings")
django.setup()
```

# 连接 SQL Server

## 1. 引入模块

```bash
pip install django-crontab
pip install django-mssql
pip install django-pyodbc
pip install django-pyodbc-azure
pip install django-pytds
pip install django-sqlserver
```

## 2. 创建数据源

windows -> 管理工具 -> ODBC 数据源 -> SQL Server Native Client 11.0

## 3. 配置 setting.py

```python
DATABASES = {
    'default': {
        'NAME': 'dw',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': 'Aurelius',
        'PORT': '1433',
        'USER': 'sa',
        'PASSWORD': 'xxxxxx',
        'OPTIONS': {
            'driver': 'SQL Server Native Client 11.0',
        }
    },
}
```

# settings

## 时区设置

**TIME_ZONE**

```python
TIME_ZONE = 'Asia/Shanghai'
```

## 语言设置

**LANGUAGE_CODE**

```python
LANGUAGE_CODE = 'zh-hans'
```
