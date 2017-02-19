from django.utils.decorators import method_decorator


def class_view_decorator1(decorator_fn):
    print("cvd 1 called")

    def simple_decorator1(View):
        View.dispatch = method_decorator(decorator_fn)(View.dispatch)
        print("Inside simple decorator1")
        return View
    print("Inside class view decorator 1")
    return simple_decorator1


def class_view_decorator2(decorator_fn):
    print("cvd 2 called")

    def simple_decorator2(View):
        View.dispatch = method_decorator(decorator_fn)(View.dispatch)
        print("Inside simple decorator2")
        return View
    print("Inside class view decorator 2")
    return simple_decorator2
