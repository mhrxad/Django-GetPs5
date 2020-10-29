from django.shortcuts import render


def home(request):
    context = {
        'page_title': 'Get PS5 | خرید کنسول و بازی های PS5',
    }
    return render(request, 'Home.html', context)


# region " Partial View "
def top_header(request):
    context = {

    }
    return render(request, 'shared/_TopHeaderPartial.html', context)


def bottom_header(request):
    context = {

    }
    return render(request, 'shared/_BottomHeaderPartial.html', context)

def footer(request):
    context = {

    }
    return render(request, 'shared/_FooterPartial.html', context)
# endregion " Partial View "
