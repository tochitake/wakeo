from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.http import HttpResponse, HttpResponseRedirect

from cms.makeSerialCd import MakeRndCode
from cms.TeamDiv import makeTeamDiv
from cms.models import Member, attribute, Page, Team
from cms.forms import MemberForm, attributeForm, PageForm
import random


def page_create(request, page_id=None):

    if page_id:
        page = get_object_or_404(Page, pk=page_id)
    else:
        page = Page()

    if request.method == 'POST':
        form = PageForm(request.POST, instance=page)
        serial = MakeRndCode()
        serialCd = serial.mkrnd()
        if form.is_valid():
            page = form.save(commit=False)
            page.serialcd = serialCd

            #response = HttpResponse('test')
            response = redirect('cms:member_list')
            response['location'] += '?S=' + serialCd + '&case=1'

            #response.set_cookie('serial_cd', serialCd)

            page.save()
            #return redirect('cms:member_list')
            #return render(request, 'cms/member_list.html')
            return response
    else:
        form = PageForm(instance=page)


    #初回きた時はGetなので、そのままindexを渡す
    #POSTでリクエストがきたら、Saveして、メンバーリストに飛ばす
    #ここからはクッキーでIDを渡す
    #DBにはPageIDを持つ

    return render(request, 'cms/index.html', dict(form=form))


def page_list(request):
    pages = Page.objects.all().order_by('id')
    return render(request, 'cms/page_list.html',
                  {'pages': pages})


def member_list(request):
    # return HttpResponse('メンバー名の一覧')
    # members = Member.objects.all().order_by('id')
    #serialCd = request.COOKIES['serial_cd']
    serialCd = request.GET.get("S")
#    response = HttpResponse('Test')
#    response.set_cookie('serial_cd', serialCd)

    case = request.GET.get("case")
    team_count = request.GET.get("team_cnt")
    member_count = request.GET.get("member_cnt")
    if case:
        a = 1
    else:
        case = '1'

    #チーム数初期値
    if team_count:
        a = 1
    else:
        team_count = '2'

    #メンバー数初期値
    if member_count:
        a = 1
    else:
        member_count = '2'


    members = Member.objects.filter(serialcd = serialCd).order_by('id')
    mcnt = members.count()
    return render(request, 'cms/member_list.html',
                  dict(members=members, S=serialCd, mcnt=mcnt, case=case, team_cnt=team_count, member_cnt=member_count))


def member_edit(request, member_id=None):
    # return HttpResponse('メンバーの編集')
    if member_id:
        member = get_object_or_404(Member, pk=member_id)
    else:
        member = Member()

    serialCd = request.GET.get("S")

    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)

        if form.is_valid():
            member = form.save(commit=False)
            #serialCd = request.COOKIES['serial_cd']
            #serialCd = request.GET.get("S")
            member.serialcd = serialCd
            #response = HttpResponse('Test')
            #response.set_cookie('serial_cd', serialCd)
            response = redirect('cms:member_list')
            response['location'] += '?S=' + serialCd
            member.save()
            #return redirect('cms:member_list')
            #return render(request, 'cms/member_list.html')
            return response
    else:
        form = MemberForm(instance=member)

    return render(request, 'cms/member_edit.html', dict(form=form, member_id=member_id, S=serialCd))


def member_del(request, member_id):
    # return HttpResponse('メンバーの削除')
    member = get_object_or_404(Member, pk=member_id)
    member.delete()
    serialCd = request.GET.get("S")
    members = Member.objects.filter(serialcd = serialCd).order_by('id')
    return render(request, 'cms/member_list.html',
                  dict(members=members, S=serialCd))
                  #{'members': members})
    #return redirect('cms:member_list')


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



def team_member_list(request):
    #members = Member.objects.all().order_by('team')
    serialCd = request.GET.get("S")
    team_count = int(request.POST.get("team_count"))
    member_count = int(request.POST.get("member_count"))
    case = request.POST.get("case")
    check_Alter = request.POST.get("check_Alter")

#    members = Member.objects.filter(serialcd = serialCd)
#    teams = Team.objects.filter(serialcd=serialCd).order_by('team')
#    member_all_count = members.count()

#    if teams.first() is None:
        #team = Team()
#    teams.delete()

    mkModel = makeTeamDiv(team_count, member_count, serialCd, case)
    teams, team_count = mkModel.doTeamSet()

    # メンバー数を決める場合
#    if case == "3":
#        team_count,mod = divmod(member_all_count,member_count)
        #if team_count == 0:
    # ペアの場合
#    elif case == "1":
#        team_count, mod = divmod(member_all_count, 2)

    if check_Alter:
        members = mkModel.doTeamDivOnCondition01()
    else:
        members = mkModel.doTeamDiv()

#    for member in members:
#        #暫定ロジック
#        i = random.randint(1,team_count)
#        member.team = i
#        member.save()

#ペアではない場合、チーム数、メンバー数は記憶しておく

    return render(request, 'cms/team_member_list.html',
                  dict(members=members, teams=teams, S=serialCd, case=case, team_cnt=team_count, member_cnt=member_count))




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

