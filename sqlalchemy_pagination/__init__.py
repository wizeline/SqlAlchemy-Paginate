import math
from flask import request

__version__ = '0.0.1'


class Page(object):

    def __init__(self, items, page, page_size, total_count):
        self.items = items
        self.previous_page = None
        self.next_page = None
        self.has_previous = page > 1
        if self.has_previous:
            self.previous_page = page - 1

        previous_items = (page - 1) * page_size
        self.has_next = previous_items + len(items) < total_count
        if self.has_next:
            self.next_page = page + 1

        self.total_count = total_count
        self.total_pages = int(math.ceil(total_count / float(page_size)))
        self.page = page
        self.page_size = page_size


def paginate(query, max_per_page=1000):
    default_per_page = 20
    default_page = 1
    page = request.args.get('page', type=int) or default_page
    page_size = request.args.get('per_page', type=int) or default_per_page
    if page <= 0:
        raise ValueError('page needs to be >= 1')
    if page_size <= 0:
        raise ValueError('page_size needs to be >= 1')

    page_size = min(page_size, max_per_page)
    items = query.limit(page_size).offset((page - 1) * page_size).all()
    # We remove the ordering of the query since it doesn't matter for getting a count and
    # might have performance implications as discussed on this Flask-SqlAlchemy issue
    # https://github.com/mitsuhiko/flask-sqlalchemy/issues/100
    total = query.order_by(None).count()
    return Page(items, page, page_size, total)
