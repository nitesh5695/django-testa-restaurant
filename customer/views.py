from django.shortcuts import render,redirect
import pyrebase
config={    "apiKey": "AIzaSyC-x73AHgduv4CTXeYJu4rTjnrwDfj1yls",
    "authDomain": "enterschool-a70f5.firebaseapp.com",
    "databaseURL": "https://enterschool-a70f5.firebaseio.com",
    "projectId": "enterschool-a70f5",
    "storageBucket": "enterschool-a70f5.appspot.com",
    "messagingSenderId": "408802600224",
    "appId": "1:408802600224:web:3fe1983eb48f8cc0c4a345",
    "measurementId": "G-PVJMPYECRW"
    }
firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
db=firebase.database()
# Create your views here.
def login_page(request):
    return render(request,'index.html')
def login_validate(request):
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        request.session['username']=email
        request.session['pass']=password
        if request.session['username'] and request.session['pass']:
            try:
                
                user=auth.sign_in_with_email_and_password(email,password)
                return redirect('home')
            except:
                return render(request,'index.html',{"error":"invalid username or password"})
        else:
                return render(request,'index.html')
    else:
        return render(request,'index.html',error="something wrong with form posting")    
def home(request):        
    if  'username' in request.session :
        return render(request,'home.html')
    else:
        return render(request,"index.html",{"error":"please login first"})
def logout(request):
    if 'username' in request.session:
       request.session.pop('username')
    
    return render(request,'index.html',{"error":"Logout successful"})
def create_customer(request):
    try:
        user=request.session['username']
        return render(request,'create_customer.html')
    except:
        return render(request,'index.html')
def upload_customer_data(request):
    if request.method=='POST':
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        mobile=request.POST.get('mobile')
        items=request.POST.get('items')
        price=request.POST.get('price')
        tip=request.POST.get('tip')
        pay_mode=request.POST.get('pay_mode')
        address=request.POST.get('address')
        data={"name":name,
        "mobile":mobile,
        "gender":gender,
        "items":items,
        "price":price,
        "tip":tip,
        "pay_mode":pay_mode,
        "address":address
            }
        customer=db.child('customer').child(mobile).get()
        if customer.val()==None:
            db.child('customer').child(mobile).set(data)
            return render(request,'create_customer.html',{"message":"successfully customer created"})
            
        else:    
            return render(request,'create_customer.html',{"message":"customer already exist"})        
    
    
def edit_customer(request):
    try:
        user=request.session['username']
        return render(request,'edit_customer.html')
    except:
        return render(request,'index.html')
def edit_customer_data(request):
    if request.method=='POST':
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        update_name=request.POST.get('update_name')
        value=request.POST.get('value')
        data={update_name:value
            }
        customer=db.child('customer').child(mobile).get()
        if customer.val()==None:
            return render(request,'edit_customer.html',{"message":"customer does not exist"})
        else:    
            db.child('customer').child(mobile).update(data)
            return render(request,'edit_customer.html',{"message":"successfully updated"})        
def delete_customer(request):
    try:
        user=request.session['username']
        return render(request,'delete_customer.html')
    except:
        return render(request,'index.html')
def delete_customer_data(request):
    if request.method=='POST':
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        try:
            customer=db.child('customer').child(mobile).get()
            if customer.val()==None:
               return render(request,'delete_customer.html',{"message":"customer does not exist"})
            else:
               db.child('customer').child(mobile).remove()
               return render(request,'delete_customer.html',{"message":"successfully deleted"})
        except:
          return render(request,'delete_customer.html',{"message":"not deleted something wrong with database"})        
def view_customer(request):
    try:
        user=request.session['username']
        customer=db.child('customer').get()
        data=customer.val()
        print(data.values())
        
        return render(request,'view_customer.html',{"customers":data.values()})
    except Exception as e:
        print(e)
        return render(request,'index.html',{"error":e})
def search_customer(request):
    if request.method=="POST":
        customer_name=request.POST.get('search')
        customer=db.child("customer").order_by_child("name").equal_to(customer_name).get()
        print("data get")
        try:
            data=customer.val()
            return render(request,'view_customer.html',{"customers":data.values()})
        except:    
            
            #print(data.values())
            return render(request,'view_customer.html',{"message":"no data matched"})        
          
            
