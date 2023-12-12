#Importing modules to configure the views
from .models import Post
from django.views import generic
from django.http import JsonResponse

#Allows for the tags to be referenced by their ID
TAGS = (
    (0, "---"),
    (1, "Entertainment"),
    (2, "Sport"),
    (3, "Technology"),
    (4, "World")
    )

#RCreates the API call to pass the information needed into React
def return_news_articles(request):
    #Allows the API request to only work with a GET request
    if request.method == "GET":
        try:
            arr = []
            #Loops through all of the created articles in the database
    if request.method == "GET":
        try:
            arr = []
            for story in Post.objects.values():
                categoryName = TAGS[story['category']][1]
                #Return the data to the FE in the same structure as provided by the news api for external stories
                arr.append({ 'title': categoryName + ": " + story['title'], 'content': story['content'],'image_url': story['imageURl'] })
            return JsonResponse({"results": arr})
        except Exception as e:
            #Sets the error response if the creation of the JSOn is incorrect
            return JsonResponse({"error": str(e)}, status=400)
    #Returns an error if GET request is not used
    return JsonResponse({"error": "Invalid Request Method"}, status=405)

#User views the articles filtered by published articles sorted by created articles
class PostList(generic.ListView):
    model = Post
    template_name = 'index.html'
    #Filter the queryset by articles that are published
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

    #Filters the articles by the search input by the user by title
    def get_queryset(self):
        query = self.request.GET.get('category')
        #Fetch the articles when the title contains the search terms
        return Post.objects.filter(category__icontains=query).order_by('title')
