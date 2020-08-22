from django.shortcuts import render, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .forms import ArticleForm
from .models import Article

from django.shortcuts import render


def blog(request, *args, **kwargs):
    return render(request, "blog.html", context={"articles": Article.objects.all()[0:10]})


@require_http_methods(["GET"])
def details(request, *args, pk, **kwargs):
    try:
        article = Article.objects.get(id=pk)
    except Article.DoesNotExist:
        return HttpResponseRedirect('/')

    return render(request, "blog_details.html", context={"article": article})


@require_http_methods(["GET", "POST"])
@csrf_exempt
def create(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, "blog_create.html")

    # elif request.method == 'POST':
    else:
        form = ArticleForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            article = form.save()

            return HttpResponseRedirect(reverse("article_details", kwargs={"pk": article.id}))
        else:
            print(form.errors)

        return render(request, "blog_create.html")
