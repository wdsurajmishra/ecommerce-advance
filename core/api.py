from ninja import NinjaAPI
from inventory.models import Category

api = NinjaAPI()

@api.get("/hello")
def hello(request):
    qs = Category.objects.all()
    return qs

@api.get("/hi")
def hi(request):
    qs = Category.objects.all()
    return qs

@api.post("/hello")
def helloPost(request):
    qs = Category.objects.all()
    return qs