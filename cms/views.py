from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView

from cms.models import Member, attribute
from cms.forms import MemberForm, attributeForm



def member_list(request):
    # return HttpResponse('メンバー名の一覧')
    members = Member.objects.all().order_by('id')
    return render(request, 'cms/member_list.html',
                  {'members': members})


def member_edit(request, member_id=None):
    # return HttpResponse('メンバーの編集')
    if member_id:
        member = get_object_or_404(Member, pk=member_id)
    else:
        member = Member()

    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            member = form.save(commit=False)
            member.save()
            return redirect('cms:member_list')
    else:
        form = MemberForm(instance=member)

    return render(request, 'cms/member_edit.html', dict(form=form, member_id=member_id))


def member_del(request, member_id):
    # return HttpResponse('メンバーの削除')
    member = get_object_or_404(Member, pk=member_id)
    member.delete()
    return redirect('cms:member_list')


def attribute_edit(request, member_id, attribute_id=None):
    member = get_object_or_404(Member, pk=member_id)
    if attribute_id:
        attributes = get_object_or_404(attribute, pk=attribute_id)
    else:
        attributes = attribute()

    if request.method == 'POST':
        form = attributeForm(request.POST, instance=attributes)
        if form.is_valid():
            attributes = form.save(commit=False)
            attributes.member = member
            attributes.save()
            return redirect('cms:attribute_list', member_id=member_id)
    else:
        form = attributeForm(instance=attributes)

    return render(request,
                  'cms/attribute_edit.html',
                  dict(form=form, member_id=member_id, attribute_id=attribute_id))


def attribute_del(request, member_id, attribute_id):
    attributes = get_object_or_404(attribute, pk=attribute_id)
    attributes.delete()
    return redirect('cms:attribute_list', member_id=member_id)



class attributeList(ListView):
    context_object_name = 'attributes'
    template_name = 'cms/attribute_list.html'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        member = get_object_or_404(Member, pk=kwargs['member_id'])
        attributes = member.attributes.all().order_by('id')
        self.object_list = attributes

        context = self.get_context_data(object_list=self.object_list, member=member)
        return self.render_to_response(context)
