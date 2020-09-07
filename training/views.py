from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from utils.decorators import first_register
from .models import Training, Entity, Instructor, Event


""" All views that references a Training models... """
@method_decorator(login_required, name='dispatch')
class TrainingListView(ListView):
    model = Training
    template_name = 'training/index.html'
    context_object_name = 'training'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(TrainingListView, self).get_context_data(**kwargs)
        training = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(training, self.paginate_by)
        try:
            training = paginator.page(page)
        except PageNotAnInteger:
            training = paginator.page(1)
        except EmptyPage:
            training = paginator.page(paginator.num_pages)
        context['training'] = training
        return context


@method_decorator(login_required, name='dispatch')
class TrainingCreateView(CreateView):
    model = Training
    template_name = 'training/training/training_create.html'
    fields = '__all__'
    success_url = reverse_lazy('training_list')


@method_decorator(login_required, name='dispatch')
class TrainingUpdateView(UpdateView):
    model = Training
    template_name = 'training/training/training_update.html'
    fields = '__all__'
    success_url = reverse_lazy('training_list')


@method_decorator(login_required, name='dispatch')
class TrainingDeleteView(DeleteView):
    model = Training
    template_name = 'training/training/training_delete.html'
    success_url = reverse_lazy('training-list')


""" All views that references a Entity models... """
@method_decorator(login_required, name='dispatch')
class EntityListView(ListView):
    model = Entity
    template_name = 'training/entity/index.html'
    context_object_name = 'entity'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(EntityListView, self).get_context_data(**kwargs)
        entity = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(entity, self.paginate_by)
        try:
            entity = paginator.page(page)
        except PageNotAnInteger:
            entity = paginator.page(1)
        except EmptyPage:
            entity = paginator.page(paginator.num_pages)
        context['entity'] = entity
        return context


@method_decorator(login_required, name='dispatch')
class EntityCreateView(CreateView):
    model = Entity
    template_name = 'training/entity/entity_create.html'
    fields = '__all__'
    success_url = reverse_lazy('entity_list')


@method_decorator(login_required, name='dispatch')
class EntityUpdateView(UpdateView):
    model = Entity
    template_name = 'entity/entity_update.html'
    fields = '__all__'
    success_url = reverse_lazy('entity_list')


@method_decorator(login_required, name='dispatch')
class EntityDeleteView(DeleteView):
    model = Entity
    template_name = 'training/entity/entity_delete.html'
    success_url = reverse_lazy('entity-list')


""" All views that references a Instructor models... """
@method_decorator(login_required, name='dispatch')
class InstructorListView(ListView):
    model = Instructor
    template_name = 'training/instructor/index.html'
    context_object_name = 'instructor'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(InstructorListView, self).get_context_data(**kwargs)
        instructor = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(instructor, self.paginate_by)
        try:
            instructor = paginator.page(page)
        except PageNotAnInteger:
            instructor = paginator.page(1)
        except EmptyPage:
            instructor = paginator.page(paginator.num_pages)
        context['instructor'] = instructor
        return context


@method_decorator(login_required, name='dispatch')
class InstructorCreateView(CreateView):
    model = Instructor
    template_name = 'training/instructor/instructor_create.html'
    fields = '__all__'
    success_url = reverse_lazy('instructor_list')


@method_decorator(login_required, name='dispatch')
class InstructorUpdateView(UpdateView):
    model = Instructor
    template_name = 'instructor/instructor_update.html'
    fields = '__all__'
    success_url = reverse_lazy('instructor_list')


@method_decorator(login_required, name='dispatch')
class InstructorDeleteView(DeleteView):
    model = Instructor
    template_name = 'training/instructor/entity_delete.html'
    success_url = reverse_lazy('instructor-list')


""" All views that references a Event models... """
@method_decorator(login_required, name='dispatch')
class EventListView(ListView):
    model = Event
    template_name = 'training/event/index.html'
    context_object_name = 'event'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        event = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(event, self.paginate_by)
        try:
            event = paginator.page(page)
        except PageNotAnInteger:
            event = paginator.page(1)
        except EmptyPage:
            event = paginator.page(paginator.num_pages)
        context['event'] = event
        return context


@method_decorator(login_required, name='dispatch')
class EventCreateView(CreateView):
    model = Event
    template_name = 'training/event/event_create.html'
    fields = '__all__'
    success_url = reverse_lazy('event_list')


@method_decorator(login_required, name='dispatch')
class EventUpdateView(UpdateView):
    model = Event
    template_name = 'training/event/event_update.html'
    fields = '__all__'
    success_url = reverse_lazy('event_list')


@method_decorator(login_required, name='dispatch')
class EventDeleteView(DeleteView):
    model = Event
    template_name = 'training/event/event_delete.html'
    success_url = reverse_lazy('event-list')