from django.shortcuts import render
from .forms import PostForm

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance =  form.save(commit=False)
        instance.save()

    context = {
        "form": form,
    }
    return render(request, "blog/post_form.html", context)

