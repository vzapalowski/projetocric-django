from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView

from django.contrib import messages
from django.utils.text import format_lazy

from django.shortcuts import render, redirect

from event.models import Event
from event.models import EnrollmentForm
from event.models.enrollment import Bond
from event.models.how_knew import HowKnew
from event.models.route_path import RoutePath
from users.models import User


class EventView(DetailView):
    model = Event
    template_name = 'events/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = Event.objects.get(pk=self.kwargs['pk'])
        
        context['event'] = event
        context['form'] = lambda: EnrollmentForm(self.request.POST) if self.request.method == 'POST' else EnrollmentForm()
        context['bond'] = Bond.objects.all()
        context['howKnew'] = HowKnew.objects.all()
        context['routePath'] = RoutePath.objects.all()
        context['events'] = Event.objects.all()

        return context

def enrollment(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == 'POST':
        if not request.session.get('user_id'):
            return redirect('users:login')

        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro feito com Sucesso!')
        else:
            error_message = "\n".join(
                f"{str(form.fields[field_name].label)}: {error}"
                for field_name, error_list in form.errors.items()
                for error in error_list
            )
            messages.error(request, error_message)
    else:
        form = EnrollmentForm()
    
    context = {
        'event': event,
        'form': form,
        'bond': Bond.objects.all(),
        'howKnew': HowKnew.objects.all(),
        'routePath': RoutePath.objects.all(),
        'user': User.objects.get(id=request.session.get('user_id'))  
    }
    
    return render(request, 'events/index.html', context)
