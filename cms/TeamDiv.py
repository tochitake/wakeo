from cms.models import Member, Team
from itertools import chain
import random


class makeTeamDiv:

    def __init__(self, team_count, member_count, serialCd, case):
        #request
        self.team_count = team_count
        self.member_count = member_count
        self.serialCd = serialCd
        self.case = case

        #objects
        self.all_members = Member.objects.filter(serialcd=serialCd).order_by('?')
        self.members_mens = Member.objects.filter(serialcd=serialCd, sex='男').order_by('?')
        self.members_womens = Member.objects.filter(serialcd=serialCd, sex='女').order_by('?')
        self.teams = Team.objects.filter(serialcd=serialCd).order_by('team')

        #人数
        self.member_all_count = self.all_members.count()
        self.m_cnt = self.members_mens.count()
        self.w_cnt = self.members_womens.count()

    def doTeamSet(self):
        self.teams.delete()

        wk_team_count = 1
        # メンバー数を決める場合
        if self.case == "3":
            wk_team_count, self.mod = divmod(self.member_all_count, self.member_count)
            if self.mod != 0:
                self.team_count = wk_team_count + 1
            else:
                self.team_count = wk_team_count

        # ペアの場合
        elif self.case == "1":
            wk_team_count, self.mod = divmod(self.member_all_count, 2)
            if self.mod != 0:
                self.team_count = wk_team_count + 1
            else:
                self.team_count = wk_team_count

        # チームを設定
        i = 0
        j = 1
        while j <= self.team_count:
            team = Team()
            team.team = j
            team.serialcd = self.serialCd
            team.name = j
            team.save()
            j += 1

        self.teams = Team.objects.filter(serialcd=self.serialCd).order_by('team')

        return self.teams, self.team_count

    def doTeamDiv(self):
        i = 0

        #★最も単純なチーム分けロジック★
        #チーム数が決まっている
        #メンバーの総数が決まっている
        #１チーム当たりの人数が決まっている
        #
        self.setMtoT(self.all_members, self.team_count)

        return self.all_members

    def doTeamDivOnCondition01(self):

        #男女別などの属性で均等条件がつくチーム分けロジック
        #チーム数は決まっている
        #（男女別均等の場合）男女ごとにメンバーの総数は決まっている
        #１チームあたりの人数は決まっている
        #
        #cnt_diff = self.m_cnt - self.w_cnt

        #if cnt_diff == 0:
        j = self.setMtoT(self.members_mens, self.team_count)
        if j == self.team_count:
            j = 0

        self.setMtoT(self.members_womens, self.team_count, j)


#        else:
#            if self.m_cnt % self.team_count == 0:
#                self.setMtoT(self.members_mens, self.team_count)
#
#            else:
#                j = self.setMtoT(self.members_mens, self.team_count)
#                self.setMtoT(self.members_womens, self.team_count, j+1)

        return Member.objects.filter(serialcd=self.serialCd)

    def setMtoT(self, mem, tc, start_cnt=0):
        i = start_cnt
        for member in mem:
            if i == tc:
                i = 1
            else:
                i += 1

            member.team = i
            member.save()

        return i
