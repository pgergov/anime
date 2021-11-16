from unittest import TestCase, mock

from apps.movies.services import (
    JIKAN_DEFAULT_PAGE_LIMIT,
    JIKAN_DEFAULT_SEARCH_TYPE,
    JIKAN_SEARCH_QUERY_MIN_LENGTH,
    search_anime_movies,
)


class SearchAnimeMoviesTestCase(TestCase):
    def setUp(self):
        self.service = search_anime_movies

    def test_short_search_query(self):
        short_search_query = 'a' * (JIKAN_SEARCH_QUERY_MIN_LENGTH - 1)

        result = self.service(search_query=short_search_query, page=1)
        expected_result = {'movies': [], 'has_next_page': False}

        self.assertEqual(expected_result, result)

    @mock.patch('apps.movies.services.Jikan')
    def test_jikan_response_handling(self, jikan_mock):
        movies = [1, 2]
        last_page = 2
        jikan_mock.return_value.search.return_value = {'results': movies, 'last_page': last_page}

        page = 1
        search_query = 'a' * JIKAN_SEARCH_QUERY_MIN_LENGTH

        result = self.service(search_query=search_query, page=page)
        expected_result = {'movies': movies, 'has_next_page': True}

        jikan_mock.return_value.search.assert_called_once_with(
            query=search_query,
            search_type=JIKAN_DEFAULT_SEARCH_TYPE,
            page=page,
            parameters={'limit': JIKAN_DEFAULT_PAGE_LIMIT},
        )
        self.assertEqual(expected_result, result)
