class IBlogService:

    def get_all_articles(self): raise NotImplementedError

    def get_article_by_id(self, article_id): raise NotImplementedError

    def search_query(self, query): raise NotImplementedError

    def get_article_comments(self, article_id): raise NotImplementedError

    def send_comment(self, text, owner_id, article_id, create_date, name): raise NotImplementedError

    def get_all_comments(self): raise NotImplementedError

    def get_all_categories(self): raise NotImplementedError

    def get_category_by_title(self, title): raise NotImplementedError

    def get_related_articles(self, article): raise NotImplementedError

    def get_parenet_comment_by_id(self, comment_id): raise NotImplementedError

    def get_last_articles(self): raise NotImplementedError

    def get_article_by_category(self, category_title): raise NotImplementedError

    def count_all_articles(self): raise NotImplementedError

    def get_invalid_views(self, ip, article): raise NotImplementedError

    def create_view(self, ip, time, article): raise NotImplementedError

    def count_views_of_article(self, article_id): raise NotImplementedError

    def set_views_in_article(self, article_id, number): raise NotImplementedError

    def set_comments_in_article(self, article_id, number): raise NotImplementedError

    def get_article_tags(self, article_id): raise NotImplementedError

