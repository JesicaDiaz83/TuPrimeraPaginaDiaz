from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Message
from .forms import MessageForm

@login_required
def send_message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, user=request.user)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            messages.success(request, 'Mensaje enviado exitosamente!')
            return redirect('messenger:inbox')
    else:
        form = MessageForm(user=request.user)
    
    return render(request, 'messenger/send.html', {'form': form})

@login_required
def inbox_view(request):
    messages_received = Message.objects.filter(receiver=request.user)
    return render(request, 'messenger/inbox.html', {
        'messages': messages_received
    })