from django.shortcuts import render
from django.views.generic.detail import DetailView

from event.models import Event

from django.shortcuts import render, redirect
from event.models import EnrollmentForm
from event.models.enrollment import Bond
from event.models.how_knew import HowKnew
from event.models.route_path import RoutePath

class EventView(DetailView):
    model = Event
    template_name = 'events/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = Event.objects.get(pk=self.kwargs['pk'])
        
        context['event'] = event
        context['form'] = lambda: EnrollmentForm(self.request.POST) if self.request.method == 'POST' else EnrollmentForm()
        context['bond'] = lambda: Bond.objects.all()
        context['howKnew'] = lambda: HowKnew.objects.all()
        context['routePath'] = lambda: RoutePath.objects.all()
        
        return context

def enrollment(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = None
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events:event', pk=event.pk)
    else:
        form = EnrollmentForm()
    
    context = {
        'event': event,
        'form': form,
        'bond': Bond.objects.all(),
        'howKnew': HowKnew.objects.all(),
        'routePath': RoutePath.objects.all(),
    }
    
    return render(request, 'events/index.html', context)
