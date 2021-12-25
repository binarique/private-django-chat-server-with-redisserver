from django.shortcuts import render, redirect
from .models import User, Chat, Message
from django.db.models import Q
from .helper import Helper
# Create your views here.


def index(request):
    if request.method == "POST":
        phone_no = request.POST.get("phone_no")
        user = User.objects.get(phoneno=phone_no)
        return redirect(
            '/chats/%s/'
            % user.pk)
    return render(request, "chat/index.html")


def Messages(request, my_id, other_user_id, chat_no):
    messages = Message.objects.filter(
        (Q(sender=my_id) & Q(reciever=other_user_id)) | (Q(sender=other_user_id) & Q(reciever=my_id)))
    me = User.objects.get(pk=my_id)
    # print(me.username);
    results = []
    for m in messages:
        user = User.objects.get(pk=m.sender)
        results.append({
            "message": m.message,
            "username": user.username
        })
    return render(request, 'chat/messages.html', {
        'my_id': my_id,
        'other_user_id': other_user_id,
        "user": me,
        'chat_no': chat_no,
        'messages': results
    })


def Chats(request, user_id):
    helper = Helper()
    results = []
    me = User.objects.get(pk=user_id)
    chats = Chat.objects.filter(Q(owner=user_id) | Q(other_user=user_id))
    for chat in chats:
        owner = chat.owner
        other = chat.other_user
        otheruserid = other if str(owner) == user_id else owner
        # if str(owner) == user_id:
        #     userid = other
        # elif str(other) == user_id:
        #     userid = owner
        chat_group_no = helper.passwordEncrypt(chat.chat_no)
        chat_url = f"/chats/messages/{user_id}/{otheruserid}/{chat_group_no}/"
        user = User.objects.get(pk=otheruserid)
        results.append({
            "user": user,
            "chat_url": chat_url
            })
    return render(request, 'chat/chats.html', {
        'chats': results,
        "user": me
    })
