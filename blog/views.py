from django.views.generic import ListView, DetailView
from django.shortcuts import render,  get_object_or_404
from django.db.models import Q
from .models import Post


# Create your views here.

class PostList(ListView):
    template_name = 'post.html'
    paginate_by: int = 9
    queryset = Post.objects.filter(status=1).order_by('-created_on')


class PostDetail(DetailView):
    model = Post
    template_name = 'post-detail.html'
    



def search(request):

    keywords=''

    if request.method=='POST': # form was submitted

        keywords = request.POST.get("keywords", "") # <input type="text" name="keywords">
        all_queries = None
        search_fields = ('title','content','resume') # change accordingly
        for keyword in keywords.split(' '): # keywords are splitted into words (eg: john science library)
            keyword_query = None
            for field in search_fields:
                each_query = Q(**{field + '__icontains': keyword})
                if not keyword_query:
                    keyword_query = each_query
                else:
                    keyword_query = keyword_query | each_query
                    if not all_queries:
                        all_queries = keyword_query
                    else:
                        all_queries = all_queries & keyword_query

        articles = Post.objects.filter(all_queries).distinct()
        context = {'articles':articles}
        return render(request, 'search.html', context)

    else: # no data submitted

        context = {}
        return render(request, 'index.html', context)