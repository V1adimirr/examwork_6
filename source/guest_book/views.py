from django.shortcuts import render

from guest_book.models import Entry


def index_view(request):
    entry = Entry.objects.order_by('-created_at')
    context = {"entries": entry}
    return render(request, "index.html", context)


def delete_view(request, pk):
    pass