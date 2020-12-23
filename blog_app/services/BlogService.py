from django.db.models import Q
from blog_app.models import Article, ArticleComment, ArticleCategories, PageViews
from blog_app.services.IBlogService import IBlogService


class BlogService(IBlogService):

    # ------------------------ used -------------------------
    def get_all_articles(self):
        return Article.objects.get_queryset().filter(is_delete=False).prefetch_related('article_comments').all()

    def count_all_articles(self):
        return Article.objects.get_queryset().filter(is_active=True).count()

    # ------------------------------- used ------------------------------------
    def get_article_comments(self, article_id):
        return ArticleComment.objects.get_queryset().filter(article_id=article_id, is_delete=False).select_related(
            'owner').all()

    # ------------------------------- used ------------------------------------
    def get_article_by_id(self, article_id):
        qs = Article.objects.get_queryset().filter(id=article_id, is_delete=False).select_related('author').first()
        return qs

    def search_query(self, query):
        lookup = Q(title__icontains=query) | Q(description__icontains=query) | Q(shortdescription__icontains=query)
        return Article.objects.get_queryset().filter(lookup, is_delete=False).prefetch_related(
            'article_comments').distinct().all()

    def send_comment(self, text, owner_id, article_id, parent_comment):
        return ArticleComment.objects.create(text=text, owner_id=owner_id, article_id=article_id,
                                             parent_comment=parent_comment)

    def get_all_comments(self):
        return ArticleComment.objects.get_queryset().filter(is_active=True, is_delete=False).all()

    # ----------------------------- used ------------------------------
    def get_all_categories(self):
        return ArticleCategories.objects.get_queryset().prefetch_related('children').all()

    def get_article_by_category(self, category_name):
        return Article.objects.filter(categories__url_title__iexact=category_name, is_delete=False).prefetch_related(
            'article_comments').all()

    def get_category_by_title(self, title):
        return ArticleCategories.objects.get_queryset().filter(title__iexact=title)

    def get_category_by_name(self, category_name):
        return ArticleCategories.objects.get_queryset().filter(url_title__iexact=category_name).first()

    # ------------------------------- used ------------------------------------
    def get_related_articles(self, article):
        try:
            return Article.objects.get_queryset().filter(categories__children=article, is_delete=False).distinct()[
                   :3].all()
        except:
            return None

    def get_parenet_comment_by_id(self, comment_id):
        return ArticleComment.objects.filter(id=comment_id).first()

    def get_last_articles(self):
        return Article.objects.get_queryset().filter(is_active=True).order_by('-time')[:3].all()

    # ------------------------------- used ------------------------------------
    def get_invalid_views(self, ip, article, user):
        return PageViews.objects.filter(user_ip=ip, article=article, user=user).all()

    def create_view(self, ip, time, article, user):
        return PageViews.objects.create(user_ip=ip, create_date=time, article=article, user=user)

    def count_views_of_article(self, article_id):
        return PageViews.objects.get_queryset().filter(article_id=article_id).count()

    def set_views_in_article(self, article_id, number):
        return Article.objects.filter(id=article_id).update(view_counter=int(number))

    # ---------------------------- used ----------------------------------------
    def get_favorite_articles(self):
        return Article.objects.get_queryset().order_by('-view_counter')[:3].all()

    def get_article_tags(self, article_id):
        return Article.objects.get(id=article_id).tags.all()
