from django.core.paginator import Paginator
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from ads.models import Category, Ad
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from homework import settings

def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class CategoryListView(ListView):
    model = Category
    def get(self, request, *args, **kwargs):
        
        super().get(request, *args, **kwargs)
        request.GET.get("cat", None)
        categories = self.object_list.order_by('name')
    
        response = [{"id": cat.id, "name": cat.name} for cat in categories]
        return JsonResponse(response, json_dumps_params={"ensure_ascii": False, "indent": 4}, safe=False)
        
class CategoryDetailView(DetailView):
    model = Category
    def get(self, request, *args, **kwargs):
        category = self.get_object()
    
        return JsonResponse({"id": category.id, "name": category.name},
                            json_dumps_params={"ensure_ascii": False, "indent": 4},
                            safe=False)
       
@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView): 
    model = Category
    fields = ["id", "name"]
    
    def post(self, request, *args, **kwargs):
        cat = json.loads(request.body)
        category = Category.objects.create(id=cat['id'], name=cat['name'])
        
        return JsonResponse({"id": category.id, "name": category.name}, status=200)

@method_decorator(csrf_exempt, name='dispatch')   
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ["id", "name"]
    
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        
        cat = json.loads(request.body)
        self.object.id = cat['id']
        self.object.name = cat['name']
        self.object.save()
        
        return JsonResponse({"id": self.object.id, "name": self.object.name}, status=201)
    
@method_decorator(csrf_exempt, name='dispatch')          
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'
    
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({"status": "ok"}, status=204)
        
        
class AdListView(ListView):
    model = Ad
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)  
        ads = self.object_list.select_related('author', 'category').order_by('-price')
        
        paginator = Paginator(ads, settings.TOTAL_PAGES)
        page_num = request.GET.get('page')
        page_obj = paginator.get_page(page_num)
        response = [{"Id": ad.Id,
                     "name": ad.name,
                     "author_id": ad.author_id,
                     "price": ad.price,
                     "description": ad.description,
                     "is_published": ad.is_published,
                     "image": ad.image.url if ad.image else None,
                     "category_id": ad.category_id} for ad in page_obj]
        return JsonResponse({"items":response, "page": page_num,"total": paginator.num_pages}, json_dumps_params={"ensure_ascii": False, "indent": 4}, safe=False)
    

class AdDetailView(DetailView):
    model = Ad
    
    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        
        return JsonResponse({
            "Id": ad.Id,
            "name": ad.name,
            "author_id": ad.author_id,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "image": ad.image.url if ad.image else None,
            "category_id": ad.category_id},
            json_dumps_params={"ensure_ascii": False, "indent": 4}, safe=False)
        
@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ['Id', 'name', 'author', 'price', 'description', 'is_published', 'image', 'category']
    
    def post(self, request, *args, **kwargs):
        ad = json.loads(request.body)
        ads = Ad.objects.create(Id=ad['Id'], name=ad['name'], author_id=ad['author_id'],
                                  price=ad['price'], description=ad['description'], is_published=ad['is_published'],
                                  image=ad['image'], category_id=ad['category_id'])
        return JsonResponse({'Id': ads.Id,'name':ads.name}, status=201)

@method_decorator(csrf_exempt, name='dispatch')    
class AdUpdateView(UpdateView):
    model = Ad
    fields = ['Id', 'name', 'author', 'price', 'description', 'is_published', 'image', 'category']
    
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        
        ad = json.loads(request.body)
        self.object.Id = ad['Id']
        self.object.name = ad['name']
        self.object.author_id = ad['author_id']
        self.object.price = ad['price']
        self.object.description = ad['description']
        self.object.is_published = ad['is_published']
        self.object.image = ad['image']
        self.object.category_id = ad['category_id']
        self.object.save()
        
        return JsonResponse({"Id": self.object.Id, "name": self.object.name}, status=201)
    
    
@method_decorator(csrf_exempt, name='dispatch')          
class AdDeleteView(DeleteView):
    model = Ad
    success_url = '/'
    
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({"status": "ok"}, status=204)
        