from django.contrib import admin
from django.urls import path
from shop.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # public url
    path('', index, name="public.homepage"),
    # admin url
    path('admin/', admin.site.urls),
    path("dashboard/", dashboard, name='admin.dashboard'),
    path("admin-panel/insertCategory/", InsertCategory, name='admin.category.insert'),
    path("admin-panel/insertBrand/", InsertBrand, name='admin.brand.insert'),
    path("admin-panel/insertProduct/", InsertProduct, name='admin.product.insert'),
    path("admin-panel/insertProductVariants/", insertProductVariant, name='admin.productVariant.insert'),
    path("admin-panel/manageCategory/", manageCategory, name='admin.category'),
    path("admin-panel/manageBrand/", manageBrand, name='admin.brand'),
    path("admin-panel/manageProduct/", manageProduct, name='admin.product'),
    path("admin-panel/manageProductVariant/", manageProductVariant, name='admin.productVariant'),
    path("admin-panel/editProduct/<int:id>/edit", editProduct, name='admin.edit.product'),
    path("admin-panel/editProductVariant/<int:id>/edit", editProductVariant, name='admin.edit.variant'),
    path("admin-panel/editCategory/<int:id>/edit", editCategory, name='admin.edit.category'),
    path("admin-panel/editBrand/<int:id>/edit", editBrand, name='admin.edit.brand'),
    path("admin-panel/category/<int:id>/delete/", deleteCategory, name='admin.category.delete'),
    path("admin-panel/brand/<int:id>/delete/", deleteBrand, name='admin.brand.delete'),
    path("admin-panel/product/<int:id>/delete/", deleteProduct, name='admin.product.delete'),
    path("admin-panel/productVariant/<int:id>/delete/", deleteProductVariant, name='admin.Variant.delete'),

    # public panel
    path("public-panel/showAll/<int:id>/", showAll, name='public.showall.product'),
    path("public-panel/viewProduct/<int:id>/", view, name='public.view.product'),
    path("public-panel/cart", cart, name="public.cart"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
