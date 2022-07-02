from django.shortcuts import render, get_object_or_404, redirect

from guest_book.models import Entry


def index_view(request):
    entry = Entry.objects.order_by('-created_at')
    context = {"entries": entry}
    return render(request, "index.html", context)


def create_view(request):
    if request.method == "GET":
        return render(request, "create.html")
    else:
        author = request.POST.get("author")
        author_mail = request.POST.get("author_mail")
        content = request.POST.get("content")
        new_entry = Entry.objects.create(author=author, author_mail=author_mail, content=content)
        new_entry.save()
        return redirect("index")


def delete_view(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == "GET":
        return render(request, "delete.html", {"entry": entry})

    else:
        entry.delete()
        return redirect("index")
