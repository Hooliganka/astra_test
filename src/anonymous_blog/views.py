from django.shortcuts import redirect
from django.views.generic import TemplateView

from anonymous_blog.models import Message


class Blog(TemplateView):
    def post(self, request, *args, **kwargs):
        message = request.POST.get('text')
        if not message:
            kwargs.update({'error': 'Поле сообщения не может быть пустым'})
            return self.get(request, *args, **kwargs)

        Message.objects.create(text=message)
        return redirect('index')

    def get(self, request, *args, **kwargs):
        kwargs['messages'] = Message.objects.all()
        return super().get(request, *args, **kwargs)
