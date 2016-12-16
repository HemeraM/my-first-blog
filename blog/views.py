#coding: utf-8
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from blog.models import Post

#class PostsListView(ListView): # представление в виде списка
#    model = Post                   # модель для представления

#class PostDetailView(DetailView): # детализированное представление модели
#    model = Post

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

def show_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return  render(request, 'blog/post.html', {'post': post})

def contact(request):
    return render(request, 'blog/contact.html')


def search_fts(search_text):
    query = "SELECT id, title, created_date, ts_headline('russian', text, query, 'StartSel = <mark>, StopSel = </mark>, MaxFragments=3, ShortWord=10, FragmentDelimiter=...') AS headline, rank FROM "
    sub_query = "(SELECT id, title, text, created_date, query, ts_rank_cd(fts, query) AS rank FROM blog_post, to_tsquery(%s) query WHERE fts @@ query ORDER BY rank DESC LIMIT 10) AS fts_search;"

    results = []
    with connection.cursor() as cursor:
        cursor.execute(query + sub_query, ["&".join(search_text.split())])
        desc = cursor.description
        rows = cursor.fetchall()

        for row in rows:
            results.append(dict(zip([col[0] for col in desc], row)))

    return results


def search(request):
    try:
        search_text = request.POST['search_text']
    except KeyError:
        search_text = 'книга'

    search_results = search_fts(search_text)
    if 'search_text' in request.POST:
        message = 'Результат поиска по запросу: %r' % request.POST['search_text']
    else:
        message = 'Некорректный поисковый запрос'
    context = {
        'message': message,
        "search_results": search_results
    }

    return render(request, 'blog/search.html', context)



