from django.http import HttpRequest,HttpResponse
from django.shortcuts import get_object_or_404

from .models import User
import json

def users(request:HttpRequest) -> HttpResponse:

    if request.method=='GET':

        users=User.objects.all()
        serialized_user=[user.name for user in users]
        return HttpResponse(json.dumps(serialized_user))

    if request.method=='POST':
        body=json.loads(request.body)
        user1=User(name=body['name'],email=body['email'],address=body['address'])
        user1.save()
        return HttpResponse(json.dumps({'id':user1.id, 'name':user1.name}))
def get_or_update_or_delete_user(request: HttpRequest, id: int) -> HttpResponse:

    if request.method=='GET':

        users= get_object_or_404(User,id=id)
       # users=User.objects.get(id=id)
       # users=User.objects.filter(id=id).first()
       # serialized_user=[user.name for user in users]
        return HttpResponse(json.dumps({'id':users.id, 'name':users.name,'address': users.address}))

    if request.method == 'PUT':
        body = json.loads(request.body)
        user = get_object_or_404(User, id=id)
        user.name = body['name']
        user.email = body['email']
        user.address = body['address']
        user.save()
        return HttpResponse(json.dumps({'id': user.id, 'name': user.name}))

    if request.method == 'DELETE':

        #User.objects.all()

        user = get_object_or_404(User, id=id)
        user.delete()
        return HttpResponse(json.dumps({'id': id, 'deleted': True}))

