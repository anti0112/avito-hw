import json
from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from users.models import User, Location
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Count
from django.core.paginator import Paginator
from homework import settings

class UserListView(ListView):
    model = User
    
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        users = self.object_list.select_related('location').order_by('username')
        users_ads = users.filter(ad__is_published=True).annotate(total_ads=Count('ad'))
        
        paginator = Paginator(users_ads, settings.TOTAL_PAGES)
        page_num = request.GET.get('page')
        page_obj = paginator.get_page(page_num)
        response = [{
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "password": user.password,
            "role": user.role,
            "age": user.age,
            "location_id": user.location.name.split()[-1]} for user in page_obj]
        return JsonResponse({"items": response,
                             "page": page_num,
                             "total": paginator.num_pages}, json_dumps_params={"ensure_ascii": False, "indent": 4}, safe=False)
    

class UserDetailView(DetailView):
    model = User
    
    def get(self, request, *args, **kwargs):
        user = self.get_object()
        
        return JsonResponse({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "password": user.password,
            "role": user.role,
            "age": user.age,
            "location_id": user.location.name.split()[-1]},
            json_dumps_params={"ensure_ascii": False, "indent": 4}, safe=False)
    
        
@method_decorator(csrf_exempt, name='dispatch')     
class UserCreateView(CreateView):
    model = User
    fields = ['id', 'first_name', 'last_name', 'username', 'password', 'role', 'age', 'location']
    
    def post(self, request, *args, **kwargs):
        
        us = json.loads(request.body)
        user = User.objects.create(id=us['id'], first_name=us['first_name'], last_name=us['last_name'],
                                   username=us['username'], password=us['password'], role=us['role'],
                                   age=us['age'], location_id=us['location_id'])
        return JsonResponse({"id": us['id'], "username": us['username'], 'location': us.location.name}, status=201)
 
    
@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ['id', 'first_name', 'last_name', 'username', 'password', 'role', 'age', 'location']
    
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        
        user = json.loads(request.body)
        self.object.id = user['id']
        self.object.first_name = user['first_name']
        self.object.last_name = user['last_name']
        self.object.username = user['username']
        self.object.password = user['password']
        self.object.role = user['role']
        self.object.age = user['age']
        self.object.location_id = user['location_id']
        self.object.save()
        
        return JsonResponse({"id": self.object.id, "username": self.object.username}, status=201)
    

@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = '/'
    
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({"status": "ok"}, status=204)
     