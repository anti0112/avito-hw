import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from ads.models import Categories, Ads
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return JsonResponse({"status": "ok"}, status=200)

@csrf_exempt
def get_cat(request):
    if request.method == 'GET':
        categories = Categories.objects.all()
        response = [{"id": cat.id, "name": cat.name} for cat in categories]
        return JsonResponse(response, json_dumps_params={"ensure_ascii": False, "indent": 4}, safe=False)
    if request.method == 'POST':
        cat = json.loads(request.body)
        save_cat = Categories(**cat)
        save_cat.save()
        return JsonResponse({"status": "ok"}, status=200)
    

def get_cat_id(request, cid):
    if request.method == 'GET':
        category = Categories.objects.filter(id=cid)
        response = [{"id": cat.id, "name": cat.name} for cat in category]
        return JsonResponse(response, json_dumps_params={"ensure_ascii": False, "indent": 4}, safe=False)
        

@csrf_exempt
def get_ads(request):
    if request.method == "GET":
        ads = Ads.objects.all()
        response = [{'Id': ad.Id,
                    'name': ad.name,
                    'author': ad.author,
                    'description': ad.description,
                    'price': ad.price,
                    'address': ad.address,
                    'is_published': ad.is_published} for ad in ads]
        return JsonResponse(response, status=200, safe=False,
                            json_dumps_params={'ensure_ascii': False, 'indent': 4})
        
    if request.method == 'POST':
        ad = json.loads(request.body)
        u = Ads(**ad)
        u.save()
        return JsonResponse({"status": "ok"}, status=200)

def get_ads_by_id(request, aid):
    if request.method == "GET":
        ads = Ads.objects.filter(Id=aid)
        response = [{'Id': ad.Id,
                    'name': ad.name,
                    'author': ad.author,
                    'description': ad.description,
                    'price': ad.price,
                    'address': ad.address,
                    'is_published': ad.is_published} for ad in ads]
        return JsonResponse(response, status=200, safe=False,
                            json_dumps_params={'ensure_ascii': False, 'indent': 4}
                            )