from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Count

from .models import Resources
from apps.user.models import User
from .utils import generate_cat_count_list

from .form import PostResourceForm


# Create your views here.


def home_page(request):
    cnt = Resources.objects.all().count()
    user_cnt = User.objects.filter(is_active=True).count()
    res_per_cat = Resources.objects.values("cat_id__cat").annotate(cnt=Count("cat_id"))

    context = {
        "cnt": cnt,
        "user_cnt": user_cnt,
        "res_per_cat": res_per_cat,
    }
    return render(
        request=request,
        template_name="resources/home.html",
        context=context,
    )


def resource_post(request):

    if request.method == "GET":
        form = PostResourceForm()
        return render(
            request,
            "resources/resource_post.html",
            {'form': form},
        )

    else:
        form = PostResourceForm(request.POST)
        return render(
            request,
            "resources/resource_post.html"
        )
        if form.is_valid():
            data = form.cleaned_data
            breakpoint()



def home_page_old(request):
    cnt = Resources.objects.all().count()
    user_cnt = User.objects.filter(is_active=True).count()
    res_per_cat = Resources.objects.values("cat_id__cat").annotate(cnt=Count("cat_id"))

    response = f"""
      <html>
         <h1>Welcome to ResourceShare</h1>

         <h3>All Users</h3>
         <p>{user_cnt} and counting!</p>

         <p>{cnt} resources and counting!</p>

         <h3>Resources per category</h3>
         <ol>
            {generate_cat_count_list(res_per_cat)}
         </ol>
      </html>
    """

    return HttpResponse(response)


def resource_detail(request, id):
    res = (
        Resources.objects.select_related("user_id", "cat_id")
        .prefetch_related("tags")
        .get(pk=id)
    )

    response = f"""
      <html>
         <h1>{res.title}</h1>
         <p><b>User</b>: {res.user_id.username}</p>
         <p><b>Link</b>: {res.link}</p>
         <p><b>Description</b>: {res.description}</p>
         <p><b>Category</b>: {res.cat_id.cat}</p>
         <p><b>Tags</b>: {res.all_tags()}
      </html>
   """
    return HttpResponse(response)


class HomePage(TemplateView):
    template_name = "home_page.html"