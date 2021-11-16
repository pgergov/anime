from typing import Dict

from jikanpy import Jikan

JIKAN_SEARCH_QUERY_MIN_LENGTH = 3
JIKAN_DEFAULT_SEARCH_TYPE = 'anime'
JIKAN_DEFAULT_PAGE_LIMIT = 10


def search_anime_movies(*, search_query: str, page: int) -> Dict:
    result = {'movies': [], 'has_next_page': False}

    if len(search_query) < JIKAN_SEARCH_QUERY_MIN_LENGTH:
        return result

    jikan_client = Jikan()
    response = jikan_client.search(
        query=search_query,
        search_type=JIKAN_DEFAULT_SEARCH_TYPE,
        page=page,
        parameters={'limit': JIKAN_DEFAULT_PAGE_LIMIT},
    )

    result['movies'] = response['results']
    result['has_next_page'] = response['last_page'] > page

    return result
