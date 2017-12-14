from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Studio, tags
from django.http import Http404
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    studios = Studio.objects.all()
    tag = tags.objects.all()
    return render(request, 'index.html', {"studios": studios, "all_tags": tag})


@login_required
def studio(request, studio_id):

    # print(studio_id)
    try:
        studio = Studio.get_studios(id=studio_id)

    except Studio.DoesNotExist:
        raise Http404()

    return render(request, 'studio.html', {"studio": studio})


def images(request, image_id):
    try:
        image = Studio.objects.get(id=image_id)

    except Studio.DoesNotExist:
        raise Http404()

    return render(request, 'images.html', {"image": image})


def tag(request, tag_id):
    # all_tags = tags.display_tags()
    try:
        tag = tags.objects.get(id=tag_id)
        images = Studio.objects.filter(tag=tag).all()

    except DoesNotExist:
        raise Http404()

    return render(request, 'tag.html', {"tag": tag, "images": images})


def categories(request):
    try:
        image = Studio.objects.get(id=image_id)

    except Studio.DoesNotExist:
        raise Http404()

    return render(request, 'image.html', {"image": image})


def locations(request):
    studios = Studio.objects.all()
    return render(request, 'location.html', {"studios": studios})


def search_results(request):

    if 'tag' in request.GET and request.GET['tag']:
        search_term = request.GET.get('tag')
        print('Search term: ' + search_term)
        search_tags = tags.search_for_tag(search_term)
        print(search_tags)
        studios = Studio.objects.filter(tags=search_tags[0]).all()
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "search_tags": search_tags, "studios": studios})

    else:
        message = "You haven't searched for any term"

        return render(request, 'search.html', {"message": message})
