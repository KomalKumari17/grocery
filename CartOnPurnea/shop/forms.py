from django.forms import ModelForm
from .models import *

class CategoryInsertForm(ModelForm):
    class Meta:
        model = Category
        fields = ['parent', 'cat_title', 'cat_desc', 'image', 'cat_status']
        
class BrandInsertForm(ModelForm):
    class Meta:
        model = Brand
        fields = ['brand_name', 'brand_desc', 'brand_logo', 'brand_status']

class ProductInsertForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'brand', 'product_name', 'product_desc', 'product_image', 'product_price', 'discount_price', 'product_qty','unit', 'sku']
 
class ProductVariantInsertForm(ModelForm):
    class Meta:
        model = Product_variant
        fields = ['product', 'variant_type', 'variant_name', 'sku', 'image', 'variant_price', 'discount_price', 'variant_qty', 'size', 'color']

