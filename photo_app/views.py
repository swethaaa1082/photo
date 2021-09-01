from django.shortcuts import render,redirect
from .models import photo
from .forms import ModeForm
# Create your views here.
def home(request):
    return render(request,'index.html')
def photo_view(request):
    product=photo.objects.all()
    return render(request,'home.html',{'products':product})
def detail(request,photo_id):
    detail=photo.objects.get(id=photo_id)
    return render(request,'detail.html',{'details':detail})
def add_product(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        img=request.FILES['img']
        s=photo(name=name,desc=desc,img=img)
        s.save()
        print("product added")
    return render(request,"add_product.html")
def update(request,id):
    obj=photo.objects.get(id=id)
    form=ModeForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('photo_view')
    return render(request,'edit.html',{'form':form,'obj':obj})
def delete(request,id):
    if request.method=='POST':
        obj=photo.objects.get(id=id)
        obj.delete()
        return redirect('photo_view')
    return render(request,'delete.html')
