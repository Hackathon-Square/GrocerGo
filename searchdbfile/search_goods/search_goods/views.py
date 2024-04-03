from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
import logging
logger = logging.getLogger(__name__)

def search(request):
    return render(request, 'search.html')

def search_results(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(ProductName__icontains=query).distinct()
    logger.debug(f"Products found: {products}")
    logger.debug(f"Number of products found: {products.count()}")

    return render(request, 'search_results.html', {'products': products, 'query': query})
