from django.views.generic.base import TemplateView

from apps.movies.services import search_anime_movies


class SearchView(TemplateView):
    template_name = 'movies/search.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        query_params = request.GET.dict()
        search_query = query_params.get('search', '')
        page = query_params.get('page', '1')
        page = int(page)

        movies_data = search_anime_movies(search_query=search_query, page=page)

        context['movies'] = movies_data['movies']
        context['query_params'] = {
            'search': search_query,
            'prev_page': page - 1 if page > 1 else None,
            'next_page': page + 1 if movies_data['has_next_page'] else None,
        }

        return self.render_to_response(context)
