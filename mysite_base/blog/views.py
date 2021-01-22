from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView
from django.views.generic.dates import MonthArchiveView, DayArchiveView, TodayArchiveView
from blog.models import Post

# Search 기능 추가 
from blog.forms import PostSearchForm
from django.views.generic.edit import FormView
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = "blog/post_all.html"
    context_object_name = "posts" #object_list 
    
    paginate_by = 3

class PostDV(DetailView):
    model = Post

class PostAV(ArchiveIndexView):
    model = Post
    date_field = "modify_date"

class PostYAV(YearArchiveView):
    model = Post
    make_object_list = True
    date_field = "modify_date"

class PostMAV(MonthArchiveView):
    model = Post
    date_field = "modify_date"
    month_format = "%m"

class PostDAV(DayArchiveView):
    model = Post
    date_field = "modify_date"
    month_format = "%m"

class PostTAV(TodayArchiveView):
    model = Post
    date_field = "modify_date"
    month_format = "%m"

class SearchFormView(FormView):
    form_class = PostSearchForm # forms.py에 생성
    template_name = "blog/post_search.html"

    def form_valid(self, form):
        schword = self.request.POST['search_word']
        post_list = Post.objects.filter(Q(title__icontains=schword) | Q(description__icontains=schword) | Q(content__icontains=schword)).distinct()

        # 검색된 결과 
        context = {}
       
        context['form'] = form
        context['search_keyword'] = schword
        context['search_list'] = post_list

        return render(self.request, self.template_name, context)