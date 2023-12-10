#Importing modules to configure the views
from .models import Post
from django.views import generic
from django.http import JsonResponse

TAGS = (
    (0, "---"),
    (1, "Entertainment"),
    (2, "Sport"),
    (3, "Technology"),
    (4, "World")
    )


def return_news_articles(request):
    if request.method == "GET":
        try:
            arr = []
            for story in Post.objects.values():
                categoryName = TAGS[story['category']][1]
                arr.append({ 'title': categoryName + ": " + story['title'], 'content': story['content'],'image_url': story['imageURl'] })
            return JsonResponse({"results": arr})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid Request Method"}, status=405)

#User views the articles filtered by published articles sorted by created articles
class PostList(generic.ListView):
    model = Post
    template_name = 'index.html'
    queryset = Post.objects.all().order_by('title')

#Setting the view of the article once user clicks on it
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogSearchView(generic.ListView):
    model = Post
    template_name = "index.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(title__icontains=query).order_by('title')

class BlogTagView(generic.ListView):
    model = Post
    template_name = "index.html"

    def get_queryset(self):
        query = self.request.GET.get('category')
        return Post.objects.filter(category__icontains=query).order_by('title')
