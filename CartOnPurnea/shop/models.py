from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)       
    cat_title = models.CharField(max_length=200)
    cat_desc = models.TextField()
    cat_slug = models.SlugField(unique=True)
    cat_status = models.BooleanField(default=False)
    image = models.ImageField(upload_to="category/", default='category/default.jpg')

    def __str__(self):
        return self.cat_title

class Brand(models.Model):
    brand_name = models.CharField(max_length=200)
    brand_desc = models.TextField()
    brand_logo = models.ImageField( upload_to='brand/')
    brand_slug = models.SlugField(unique=True)
    brand_status = models.BooleanField(default=False)

    def __str__(self):
        return self.brand_name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_slug = models.CharField(max_length=200, unique=True)
    product_desc = models.TextField()
    product_image = models.ImageField(upload_to='product/')
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    product_qty = models.IntegerField()
    sku = models.CharField(max_length=100, default='DEFAULT-SKU')  
    unit = models.CharField(max_length=10, choices=[('g', 'Gram'), ('kg', 'Kilogram'), ('mg', 'Milligram'), ('lb', 'Pound'), ('oz', 'Ounce'), ('l', 'Liter'), ('ml', 'Milliliter'), ('dozen', 'Dozen'), ('pcs', 'Pieces'), ('bundle', 'Bundle'), ('packet', 'Packet'), ('box', 'Box'), ('bottle', 'Bottle'), ('can', 'Can'), ('jar', 'Jar'), ('bag', 'Bag')], default='g')

    def __str__(self):
        return self.product_name
    
    def per_discount(self):
        return ((self.product_price-self.discount_price)/self.product_price)*100

class Product_variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant_type = models.CharField(max_length=200, default='Standard')
    variant_name = models.CharField(max_length=200, default='Default Variant')
    sku = models.CharField(max_length=100, default='DEFAULT-SKU')  
    image = models.ImageField(upload_to='productVariant/', default='productVariant/default.jpg')
    variant_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  
    variant_qty = models.IntegerField()
    size = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.variant_name

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    item_variant = models.ForeignKey(Product_variant, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)

    def __str__(self):
        return self.item.product_name
    
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    contact = models.BigIntegerField()
    street = models.CharField(max_length=200)
    landmark = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.IntegerField()
    type = models.CharField(max_length=200, choices=(("Home","Home"), ("Office", "Office")))

    def __str__(self):
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    order_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} -Order #{self.id}"