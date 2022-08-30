# pylint: disable=locally-disabled, no-member
'''
Import the required packages
'''
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Testimononial
from .forms import TestimonialForm


# Create your views here.


class TestimonialList(generic.ListView):
    '''
    Gets testimonial objects from the testimonial models and renders them to
    the testimonials page.
    '''
    model = Testimononial

    def get(self, request, *args, **kwargs):
        '''
        Gets only approved objects from the testimonial models and
        renders the paginated lists to testimonials page.
        '''

        paginate = Paginator(Testimononial.objects.filter(
            approved=True).order_by("-created_on"), 6)
        page = request.GET.get('page')
        lists = paginate.get_page(page)

        return render(request, 'testimonials.html', {'lists': lists})


@login_required()
def write_testimonial(request):
    '''
    Posts data to testimonials. If the submit is successful
    then page redirects to testimonials page. Renders the
    write testimonials page.
    '''
    if request.method == "POST":
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial_form = form.save(commit=False)
            testimonial_form.name = request.user
            testimonial_form.save()
            messages.success(
                request, ('Your testimonial is awaiting approval'))
            return HttpResponseRedirect('/testimonials')
    else:
        form = TestimonialForm()

    return render(request, 'write_testimonial.html', {'form': form})


@login_required
def edit_testimonial(request, testimonial_id):
    '''
    Gets the stored data by id for a specific confirmed
    testimonial and allows for editing. Resubmission sets the
    approved back to false for it to be confirmed again by
    the admin. Renders edit testimonials page.
    '''
    testimonial = get_object_or_404(Testimononial, id=testimonial_id)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            testimonial_form = form.save(commit=False)
            testimonial_form.name = request.user
            testimonial_form.approved = False
            testimonial_form.save()
            messages.success(
                request, ('Your testimonial is awaiting approval'))
            return redirect('/testimonials')
    form = TestimonialForm(instance=testimonial)
    context = {
        'form': form
    }
    return render(request, 'edit_testimonial.html', context)


# pylint: disable=unused-argument
@login_required
def delete_testimonial(request, testimonial_id):
    '''
    Gets stored testimonial data by testing id and allows
    the user to delete the testimonial
    '''
    testimonial = get_object_or_404(Testimononial, id=testimonial_id)
    testimonial.delete()
    return redirect('/testimonials')
