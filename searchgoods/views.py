from django.http import HttpResponse
from django.shortcuts import render
from managegoods.models import Product
import logging
from django.shortcuts import render, redirect
from django.http import JsonResponse
from managegoods.models import Product
from .forms import ImageUploadForm
from django.db.models import Q

from django.http import JsonResponse

from .intention import use_gpt
import json

logger = logging.getLogger(__name__)


def search(request):
    return render(request, 'search.html')


def search_results(request):
    query = request.GET.get('query', '')
    model_output = use_gpt(query)
    logger.debug(model_output)
    try:
        model_output_dict = json.loads(model_output)
    except json.JSONDecodeError:
        print("Error: model_output is not a valid JSON string.")

    logger.debug(model_output_dict)

    # 提取动作和对象
    action = model_output_dict.get("Action")
    details = model_output_dict.get("Details")

    product_names = details["ProductName"]

    if action == "find":

        query = Q()

        for product_name in product_names:
            query |= Q(ProductName__icontains=product_name)

        products = Product.objects.filter(query).distinct()

        logger.debug(f"Products found: {products}")
        logger.debug(f"Number of products found: {products.count()}")

        return render(request, 'searchgoods/search_results.html', {'products': products, 'query': product_names})


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['image']
            product_name = image.name.rsplit('.', 1)[0]
            try:
                product = Product.objects.get(ProductName=product_name)
                data = {
                    "ProductName": product.ProductName,
                    "Block": product.Block,
                    "Shelf": product.Shelf,
                    "Level": product.Level,
                    "Price": str(product.Price),
                    "Unit": product.Unit,
                }
                print(data)
                return JsonResponse(data)
            except Product.DoesNotExist:
                return JsonResponse({"error": "Product not found"}, status=404)
    return JsonResponse({"error": "Invalid form"}, status=400)
