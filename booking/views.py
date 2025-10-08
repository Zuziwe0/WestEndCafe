from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from .forms import BookingForm
from django.utils import timezone

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-date')
    return render(request, 'booking/booking_list.html', {'bookings': bookings})

@login_required
def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    return render(request, 'booking/booking_detail.html', {'booking': booking})

@login_required
def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking created successfully!')
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'booking/booking_form.html', {'form': form})

@login_required
def booking_edit(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking updated successfully!')
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking/booking_edit.html', {'form': form})

@login_required
def booking_cancel(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.status = 'Cancelled'
        booking.save()
        messages.info(request, 'Booking cancelled.')
        return redirect('booking_list')
    return render(request, 'booking/booking_cancel.html', {'booking': booking})

@login_required
def booking_complete(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.status = 'Completed'
        booking.save()
        messages.success(request, 'Booking marked as completed.')
        return redirect('booking_list')
    return render(request, 'booking/booking_complete.html', {'booking': booking}) 

@login_required
def booking_search(request):
    query = request.GET.get('q')
    bookings = Booking.objects.filter(user=request.user, name__icontains=query) if query else []
    return render(request, 'booking/booking_search.html', {'bookings': bookings, 'query': query})

@login_required
def upcoming_bookings(request):
    bookings = Booking.objects.filter(user=request.user, date__gte=timezone.now()).order_by('date')
    return render(request, 'booking/upcoming_bookings.html', {'bookings': bookings})

@login_required
def past_bookings(request):
    bookings = Booking.objects.filter(user=request.user, date__lt=timezone.now()).order_by('-date')
    return render(request, 'booking/past_bookings.html', {'bookings': bookings})

@login_required
def booking_reminder(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    # Logic to send reminder (e.g., email) would go here
    messages.info(request, f'Reminder sent for booking on {booking.date}.')
    return redirect('booking_list')
    return render(request, 'booking/booking_reminder.html', {'booking': booking})

@login_required
def booking_reschedule(request, pk): 
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking rescheduled successfully!')
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking/booking_reschedule.html', {'form': form})

@login_required
def booking_user_list(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-date')
    return render(request, 'booking/booking_user_list.html', {'bookings': bookings})

@login_required
def booking_user_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    return render(request, 'booking/booking_user_detail.html', {'booking': booking})

@login_required
def booking_user_edit(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking has been updated.')
            return redirect('booking_user_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking/booking_user_edit.html', {'form': form})

@login_required
def booking_user_cancel(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.status = 'Cancelled'
        booking.save()
        messages.info(request, 'Your booking has been cancelled.')
        return redirect('booking_user_list')
    return render(request, 'booking/booking_user_cancel.html', {'booking': booking})

@login_required
def booking_user_complete(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.status = 'Completed'
        booking.save()
        messages.success(request, 'Your booking has been marked as completed.')
        return redirect('booking_user_list')
    return render(request, 'booking/booking_user_complete.html', {'booking': booking})

@login_required
def booking_user_reschedule(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking has been rescheduled.')
            return redirect('booking_user_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking/booking_user_reschedule.html', {'form': form})

@login_required
def booking_user_reminder(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    # Logic to send reminder (e.g., email) would go here
    messages.info(request, f'Reminder sent for your booking on {booking.date}.')
    return redirect('booking_user_list')
    return render(request, 'booking/booking_user_reminder.html', {'booking': booking})

@login_required
def booking_statistics(request):
    total_bookings = Booking.objects.filter(user=request.user).count()
    upcoming_count = Booking.objects.filter(user=request.user, date__gte=timezone.now()).count()
    past_count = Booking.objects.filter(user=request.user, date__lt=timezone.now()).count()
    cancelled_count = Booking.objects.filter(user=request.user, status='Cancelled').count()
    completed_count = Booking.objects.filter(user=request.user, status='Completed').count()

    stats = {
        'total_bookings': total_bookings,
        'upcoming_count': upcoming_count,
        'past_count': past_count,
        'cancelled_count': cancelled_count,
        'completed_count': completed_count,
    }
    return render(request, 'booking/booking_statistics.html', {'stats': stats})

@login_required
def booking_export(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-date')
    # Logic to export bookings (e.g., to CSV) would go here
    messages.success(request, 'Your bookings have been exported.')
    return redirect('booking_user_list')
    return render(request, 'booking/booking_export.html', {'bookings': bookings})