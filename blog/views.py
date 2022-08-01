from django.shortcuts import render
from django.db.models import Q
from . import models

# Create your views here.

def post_view(request):
    return render(request, 'post.html')


def post_detail_view(request):
    return render(request, 'post-detail.html')


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

        articles = models.Post.objects.filter(all_queries).distinct()
        context = {'articles':articles}
        return render(request, 'search.html', context)

    else: # no data submitted

        context = {}
        return render(request, 'index.html', context)