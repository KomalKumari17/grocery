from django.shortcuts import render, redirect
from .forms import CategoryInsertForm, BrandInsertForm, ProductInsertForm, ProductVariantInsertForm
from .models import *
from django.utils.text import slugify

# public-panel
def index(req):
    data = {}
    data['category'] = Category.objects.filter(product__isnull=False).distinct()
    data['categories'] = Category.objects.all()
    products = Product.objects.all()
    data['products'] = products
    return render(req, "public_panel/index.html", data)

# view all
def showAll(req, id):
    data = {}
    category = Category.objects.get(id=id)
    data['products'] = Product.objects.filter(category=category)
    data['category'] = category
    return render(req, "public_panel/showAll.html", data)

def view(req, id):
    data = {}
    product = Product.objects.get(id=id)
    data['product'] = product
    cat = product.category
    data['category'] = Category.objects.filter(id=cat.id, product__isnull=False).distinct()
    rp = Product.objects.filter(category=cat).exclude(id=id)
    data['rp'] = rp
    data['rp_count'] = rp.count()
    data['variant'] = Product_variant.objects.all()
    return render(req, "public_panel/viewProduct.html", data)

def cart(req):
    return render(req, "public_panel/cart.html")


# admin-panel
def dashboard(req):
    return render(req, "admin_panel/dashboard.html")

# category
def InsertCategory(req):
    form = CategoryInsertForm(req.POST or None, req.FILES or None)
    if form.is_valid():
        data = form.save(commit=False)
        data.cat_slug = slugify(req.POST.get('cat_title'), allow_unicode=True)
        data.save()
        return redirect(manageCategory)
    return render(req, "admin_panel/insertCategory.html", {'form':form} )

def manageCategory(req):
    categories = Category.objects.all()
    return render(req, "admin_panel/manageCategory.html", {'categories':categories} )

def deleteCategory(req, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect(manageCategory)

def editCategory(req, id):
    data = {}
    category = Category.objects.get(id=id)
    form = CategoryInsertForm(req.POST or None, req.FILES or None, instance=category)
    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(manageCategory)
    data['form'] = form
    return render(req, 'admin_panel/editCategory.html', data)

# Brand
def editBrand(req, id):
    data = {}
    brand = Brand.objects.get(id=id)
    form = BrandInsertForm(req.POST or None, req.FILES or None, instance=brand)
    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(manageBrand)
    data['form'] = form
    return render(req, "admin_panel/editBrand.html", data)

def manageBrand(req):
    brands = Brand.objects.all()
    return render(req, "admin_panel/manageBrands.html", {'brands':brands} )

def deleteBrand(req, id):
    brand = Brand.objects.get(id=id)
    brand.delete()
    return redirect(manageBrand)

def InsertBrand(req):
    form = BrandInsertForm(req.POST or None, req.FILES or None)
    if form.is_valid():
        data = form.save(commit=False)
        data.brand_slug = slugify(req.POST.get('brand_name'), allow_unicode=True)
        data.save()
        return redirect(manageBrand)
    return render(req, "admin_panel/insertBrand.html", {'form':form} )

# product
def InsertProduct(req):
    form = ProductInsertForm(req.POST or None, req.FILES or None )
    if form.is_valid():
        data = form.save(commit=False)
        data.product_slug = slugify(req.POST.get('product_name'), allow_unicode=True)
        data.save()
        return redirect(manageProduct)
    return render(req, 'admin_panel/insertProduct.html', {'form':form})

def manageProduct(req):
    data = {}
    data['products'] = Product.objects.all()
    return render(req, 'admin_panel/manageProduct.html', data)

def deleteProduct(req, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect(manageProduct)

def editProduct(req, id):
    data = {}
    product = Product.objects.get(id=id)
    form = ProductInsertForm(req.POST or None, req.FILES or None, instance=product)
    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(manageProduct)
    data['form'] = form
    return render(req, 'admin_panel/editProduct.html', data)

# product variant
def insertProductVariant(req):
    data = {}
    form = ProductVariantInsertForm(req.POST or None, req.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(manageProductVariant)
    data['form'] = form
    return render(req, 'admin_panel/insertProduct.html', data)

def manageProductVariant(req):
    data = {}
    data['variants'] = Product_variant.objects.all()
    return render(req, 'admin_panel/manageProductVariant.html', data)

def deleteProductVariant(req, id):
    variant = Product_variant.objects.get(id=id)
    variant.delete()
    return redirect(manageProductVariant)

def editProductVariant(req, id):
    data = {}
    variant = Product_variant.objects.get(id=id)
    form = ProductVariantInsertForm(req.POST or None, req.FILES or None, instance=variant)
    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(manageProductVariant)
    data['form'] = form
    return render(req, 'admin_panel/editProductVariant.html', data)

