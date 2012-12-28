from django.shortcuts import render, HttpResponse


def admin_cachekill(request):
    from django.template.loader import template_source_loaders
    if template_source_loaders is None:
        # Render it twice. The first time will populate the loaders
        render(request, 'admin/template1.html', {})
    from django.template.loader import template_source_loaders
    cached_loader = None

    for loader in template_source_loaders:
        if hasattr(loader, 'template_cache'):
            if request.method == "POST":
                remove_from_cache(dict(request.POST), cached_loader, loader)
            cached_loader = loader.template_cache
            break

    context = {'globals': template_source_loaders,
               'cached_loader': cached_loader}
    response = render(request, 'admin/template1.html', context)
    return response


def remove_from_cache(post_data, template_dict, loader):
    for template_name in post_data.get('template_name', []):
        loader.template_cache.pop(template_name, None)


def admin_testview(request):
    from django.template.loaders.cached import Loader
    print "***************"
    print getattr(Loader, 'template_cache', "Nothing to see here")
    print "***************"
    return HttpResponse("foo")


def user_view(request):
    return render(request, 'template_test.html', {})

