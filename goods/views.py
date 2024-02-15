from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from goods.form import CommentForm
from goods.models import Products, Comment
from goods.util import q_search


def catalog(request, category_slug=None):
    """
    View function for displaying products in a category or performing a search.
    """
    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    query = request.GET.get("q", None)

    if category_slug == "all":
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    if on_sale:
        goods = goods.filter(discount__gt=0)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context = {
        "title": "Restaurant menu",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    """
    View function for displaying a product details page and handling comments.
    """
    product_item = get_object_or_404(Products, slug=product_slug)
    comments = product_item.comments.filter(approved=True).order_by("-created_on")
    comment_count = comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.dish = product_item
            comment.save()
            messages.success(request, "Comment submitted and awaiting approval")

    comment_form = CommentForm()

    context = {
        "product": product_item,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        "title": "DISH DETAILS",
    }
    return render(request, "goods/product.html", context)

@login_required
def comment_edit(request, product_slug, comment_id):
    """
    View function for editing a comment.
    """
    if request.method == "POST":
        product_item = get_object_or_404(Products, slug=product_slug)
        comment = get_object_or_404(Comment, pk=comment_id)

        if comment.author == request.user:
            comment_form = CommentForm(data=request.POST, instance=comment)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.dish = product_item
                comment.approved = False
                comment.save()
                messages.success(request, "Comment Updated!")
            else:
                messages.error(request, "Error updating comment!")
        else:
            messages.error(request, "You can only edit your own comments!")

    return HttpResponseRedirect(reverse("goods:product", args=[product_slug]))

@login_required
def comment_delete(request, product_slug, comment_id):
    """
    View function for deleting a comment.
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, "Comment deleted!")
    else:
        messages.error(request, "You can only delete your own comments!")

    return HttpResponseRedirect(reverse("goods:product", args=[product_slug]))
