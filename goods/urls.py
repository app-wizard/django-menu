from django.urls import path
from goods import views

app_name = "goods"

urlpatterns = [
    # Path for searching goods
    path("search/", views.catalog, name="search"),
    # Path for displaying goods by category
    path("<slug:category_slug>/", views.catalog, name="index"),
    # Path for displaying a specific product
    path("product/<slug:product_slug>/", views.product, name="product"),
    # Path for editing a comment on a product
    path(
        "product/<slug:product_slug>/edit_comment/<int:comment_id>",
        views.comment_edit,
        name="comment_edit",
    ),
    # Path for deleting a comment on a product
    path(
        "product/<slug:product_slug>/delete_comment/<int:comment_id>",
        views.comment_delete,
        name="comment_delete",
    ),
]
