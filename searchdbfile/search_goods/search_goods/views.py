from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
import logging
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Product
from .forms import ImageUploadForm

logger = logging.getLogger(__name__)

def search(request):
    return render(request, 'search.html')

def search_results(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(product_name__icontains=query).distinct()
    logger.debug(f"Products found: {products}")
    logger.debug(f"Number of products found: {products.count()}")

    return render(request, 'search_results.html', {'products': products, 'query': query})

from django.http import JsonResponse





def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['image']
            product_name = image.name.rsplit('.', 1)[0]
            try:
                product = Product.objects.get(product_name=product_name)
                data = {
                    "ProductName": product.product_name,
                    "Block": product.block,
                    "Shelf": product.shelf,
                    "Level": product.level,
                    "Price": str(product.price),
                    "Unit": product.unit,  # 确保这个字段存在
                }
                return JsonResponse(data)
            except Product.DoesNotExist:
                return JsonResponse({"error": "Product not found"}, status=404)
        else:
            return JsonResponse({"error": "Invalid form"}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)
