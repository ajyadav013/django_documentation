from django.utils.decorators import method_decorator


def class_view_decorator(decorator_fn):

    def simple_decorator(View):
        View.dispatch = method_decorator(decorator_fn)(View.dispatch)
        return View
    return simple_decorator
