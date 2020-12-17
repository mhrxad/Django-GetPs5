from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

# from Makeup_Blog.models import Post
# from Makeup_products.models import Product


class StaticsPage(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return ['home', 'product_list_view']

    def location(self, item):
        return reverse(item)


# class ProductList(Sitemap):
#     changefreq = "daily"
#     priority = 0.9
#
#     def items(self):
#         return Product.objects.filter(active=True)
#
# class PostList(Sitemap):
#     changefreq = "daily"
#     priority = 0.9
#
#     def items(self):
#         return Post.objects.filter(active=True)

