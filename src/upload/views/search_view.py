from django.shortcuts import render
from upload.forms import SearchForm
from upload.models import Person
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required
def search(request):
    data = request.GET
    query_fields = data.getlist('query')
    query_types = data.getlist('query_type')
    
    filter_conditions = []
    
    if query_fields and query_types:
        for field, query_type in zip(query_fields, query_types):
            filter_condition = {f"{query_type}__icontains": field}
            filter_conditions.append(Q(**filter_condition))
        
        combined_filter = filter_conditions[0]
        for condition in filter_conditions[1:]:
            combined_filter &= condition
        
        try:
            results = Person.objects.filter(combined_filter, author=request.user)
        except:
            results = Person.objects.all()
    else:
        results = Person.objects.filter(author=request.user)

    paginator = Paginator(results, 4)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    temp = SearchForm(request.GET)
    return render(request, 'search.html', {'page': page, 'form': temp, 'query_fields': query_fields, 'query_types': query_types})



