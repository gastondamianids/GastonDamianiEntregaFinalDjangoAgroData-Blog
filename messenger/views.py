from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Message


@login_required
def inbox(request):
    recibidos = request.user.received_messages.all().order_by("-created_at")
    enviados = request.user.sent_messages.all().order_by("-created_at")
    return render(request, "messenger/inbox.html", {
        "recibidos": recibidos,
        "enviados": enviados,
    })


@login_required
def send_message(request):
    error = ""
    if request.method == "POST":
        receiver_username = request.POST.get("receiver", "").strip()
        subject = request.POST.get("subject", "").strip()
        body = request.POST.get("body", "").strip()

        try:
            receiver = User.objects.get(username=receiver_username)
        except User.DoesNotExist:
            error = "Usuario no existe."
        else:
            Message.objects.create(
                sender=request.user,
                receiver=receiver,
                subject=subject,
                body=body
            )
            return redirect("inbox")

    return render(request, "messenger/send.html", {"error": error})


@login_required
def message_detail(request, pk):
    msg = get_object_or_404(Message, pk=pk)

    # Solo el receptor puede verlo y marcarlo como leído
    if msg.receiver != request.user:
        return redirect("inbox")

    if not msg.read:
        msg.read = True
        msg.save()

    return render(request, "messenger/detail.html", {"msg": msg})


@login_required
def message_delete(request, pk):
    msg = get_object_or_404(Message, pk=pk)

    # Solo dueño: emisor o receptor
    if msg.sender != request.user and msg.receiver != request.user:
        return redirect("inbox")

    if request.method == "POST":
        msg.delete()
        return redirect("inbox")

    return render(request, "messenger/confirm_delete.html", {"msg": msg})


# Create your views here.
