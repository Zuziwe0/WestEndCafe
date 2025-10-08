from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from .forms import ReviewForm

@login_required
def review_list(request):
    reviews = Review.objects.all().order_by('-date_created')
    return render(request, 'review/review_list.html', {'reviews': reviews})

@login_required
def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'review/review_detail.html', {'review': review})

@login_required
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, "Review submitted successfully!")
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'review/review_create.html', {'form': form})

@login_required
def review_edit(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review updated successfully!")
            return redirect('review_list')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'review/review_edit.html', {'form': form})

@login_required
def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    if request.method == 'POST':
        review.delete()
        messages.info(request, "Review deleted.")
        return redirect('review_list')
    return render(request, 'review/review_delete.html', {'review': review})

@login_required
def review_user_list(request):
    reviews = Review.objects.filter(user=request.user).order_by('-date_created')
    return render(request, 'review/review_user_list.html', {'reviews': reviews})

@login_required
def review_user_detail(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    return render(request, 'review/review_user_detail.html', {'review': review})

@login_required
def review_user_edit(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Your review has been updated.")
            return redirect('review_user_list')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'review/review_user_edit.html', {'form': form})

@login_required
def review_user_delete(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    if request.method == 'POST':
        review.delete()
        messages.info(request, "Your review has been deleted.")
        return redirect('review_user_list')
    return render(request, 'review/review_user_delete.html', {'review': review})

# Admin views
@login_required
def admin_review_list(request):
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to access this page.")
        return redirect('review_list')
    reviews = Review.objects.all().order_by('-date_created')
    return render(request, 'review/admin_review_list.html', {'reviews': reviews})

@login_required
def admin_review_delete(request, pk):
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to access this page.")
        return redirect('review_list')
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.delete()
        messages.info(request, "Review deleted.")
        return redirect('admin_review_list')
    return render(request, 'review/admin_review_delete.html', {'review': review})

@login_required
def admin_review_detail(request, pk):
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to access this page.")
        return redirect('review_list')
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'review/admin_review_detail.html', {'review': review})

@login_required
def admin_review_edit(request, pk):
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to access this page.")
        return redirect('review_list')
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review updated successfully!")
            return redirect('admin_review_list')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'review/admin_review_edit.html', {'form': form})

@login_required
def admin_review_create(request):
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to access this page.")
        return redirect('review_list')
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, "Review created successfully!")
            return redirect('admin_review_list')
    else:
        form = ReviewForm()
    return render(request, 'review/admin_review_create.html', {'form': form})
# The above code provides views for managing reviews in a Django application. It includes functionality for users to create, edit, delete, and view their own reviews, as well