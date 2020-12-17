def return_visitor_ip(view_request):
    return view_request.META.get('REMOTE_ADDR')

