from django.shortcuts import render


def admin_cachekill(request):
    from django.template.loader import template_source_loaders
    if template_source_loaders is None:
        # Render it twice. The first time will populate the loaders
        render(request, 'cachekill/admin/template1.html', {})
    from django.template.loader import template_source_loaders
    context = {'globals': template_source_loaders}
    response = render(request, 'cachekill/admin/template1.html', context)
    return response


def user_view(request):
    return render(request, 'cachekill/template_test.html', {})
