# import menu as menu
from django.db.models import Count
from django.core.cache import cache


class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs

    # user_menu = menu.copy()


