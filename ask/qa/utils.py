from django.core.paginator import Paginator, EmptyPage


def paginate(query_set, limit=10, page=1):
    paginator = Paginator(query_set, limit)

    try:
        paginator_page = paginator.page(page)
    except EmptyPage:
        paginator_page = paginator.page(paginator.num_pages)

    return paginator_page
