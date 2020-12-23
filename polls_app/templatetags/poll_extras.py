from django import template
from polls_app.utilities.jalali.jalali_services import jalali_date
from blog_app.services.BlogService import BlogService

blog_services = BlogService()
register = template.Library()


@register.filter
def jalali(value):
    return jalali_date(value)


@register.filter
def articles_in_categories(category_name):
    articles = blog_services.get_article_by_category(category_name)
    return articles.count()


@register.filter
def get_article_comments(article_id):
    comments = blog_services.get_article_comments(article_id)
    return comments.count()


@register.simple_tag
def URL(value, name, urlencode=None):
    url = '?{}={}'.format(name, value)

    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0] != name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)

    return url


@register.filter(name='split')
def split(value, arg):
    return value.split(arg)
