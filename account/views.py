from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import registerd_user
from .models import addProduct
from .models import addReturn
from .models import salesAdd


# Create your views here.


def login_set(request):
    if request.method == "POST":
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = name,password =password)
        if user is not None:
            login(request,user)
            return redirect('account:home')

        else:
            print(False)
            messages.error(request,'something went wrong please try again!')

    return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect('account:login')

def dashboard(request):
    dataset = addProduct.objects.all()
    dataset_count = dataset.count()
    datasetreturn = addReturn.objects.all()
    returncount_set = datasetreturn.count()
    datasetsale = salesAdd.objects.all()
    countsale = datasetsale.count()
    datauser = registerd_user.objects.all()
    countuser = datauser.count()


    context = {
        'product_counts':dataset_count,
        'return_counts':returncount_set,
        'datasetsale':datasetsale,
        'countsale':countsale,
        'countuser': countuser,


    }

    return render(request,'dashboard.html',context)


def product_set(request):
    dataset = addProduct.objects.all()

    context = {
        'set':dataset
    }

    return render(request,'products.html',context)


def return_set(request):
    dataset = addReturn.objects.all()
    #count_set = dataset.count()

    contex = {
        'dataset': dataset,
    }
    return  render(request, 'returns.html',contex)

def sales_set(request):
    dataset = salesAdd.objects.all()
    countsale = dataset.count()

    context = {
        'saledata': dataset,
        'salecount' : countsale
    }

    return  render(request, 'sales.html',context)

def addSale_set(request):

    if request.method == "POST":
        name = request.POST.get('ad_name')
        code = request.POST.get('ad_code')
        category = request.POST.get('ad_type')
        price = request.POST.get('ad_price')
        qnt = request.POST.get('ad_qnt')

        saleData = salesAdd(
            name = name,
            code = code,
            category = category,
            price = price,
            qnt = qnt
        )
        saleData.save()
        return redirect('account:addsale')
    messages.success(request,"added new sales!")

    return render(request, 'newsale.html')



def user_set(request):
    datauser = registerd_user.objects.all()

    context = {
        "userinfo":datauser
    }

    return  render(request, 'user.html',context)

def addProduct_set(request):
    if request.method == "POST":
        name = request.POST.get('name')
        code = request.POST.get('code')
        category = request.POST.get('type')
        price = request.POST.get('price')
        qnt = request.POST.get('qnt')

        P_data = addProduct(
            P_name =name,
            P_code = code,
            P_category =category,
            P_price = price,
            P_quantity = qnt
        )

        if P_data.save():
            return redirect('account:addproducts')
        messages.success(request, 'New Products added!')

    return render(request, 'addproduct.html')


def addReturn_set(request):
    if request.method == "POST":
        name = request.POST.get('rp_name')
        code = request.POST.get('rp_code')
        category = request.POST.get('rp_type')
        qnt = request.POST.get('rp_qnt')

        dataReturn = addReturn(
            P_name = name,
            P_code = code,
            P_category = category,
            P_quantity = qnt
        )
        if dataReturn.save():
            return redirect('account:addreturn')
    messages.success(request, "Return Product added!")
    return render(request, 'addreturns.html')

def addUser_set(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        mobile = request.POST.get('mobile')
        u_type = request.POST.get('type')
        email = request.POST.get('email')
        username = request.POST.get('username')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        datauser = registerd_user(
            first_name = fname,
            last_name = lname,
            mobile = mobile,
            email = email,
            user_type = u_type,
            username = username,
            password1 = pass1,
            password2 = pass2
        )
        datauser.save()

    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password1']
        confirm_password = request.POST['password2']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request,'This user name already exist, try another')
            #same here can email validatoin allowed

            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                messages.success(request,"new user registered!")
                return redirect('account:addmy_user')

    return render(request, 'adduser.html')




# def pageUser_set(request):
#     return render(request, 'page-user.html')
















