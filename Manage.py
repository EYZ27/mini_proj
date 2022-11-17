class Manage:
    def __init__(self):
        self.team_prefix =\
        {
            '나무팀': '파릇파릇한',
            '꽃팀': '향긋한',
            '열매팀': '달콤한',
        }

    def compare_age(self, standard_member, member_to_compare):
        if standard_member['나이'] < member_to_compare['나이']:
            return f"{standard_member['성']}{standard_member['이름']} 사원은 {member_to_compare['성']}{member_to_compare['이름']} 사원보다 나이가 적습니다."
        elif standard_member['나이'] > member_to_compare['나이']:
            return f"{standard_member['성']}{standard_member['이름']} 사원은 {member_to_compare['성']}{member_to_compare['이름']} 사원보다 나이가 많습니다."
        else:
            return f"{standard_member['성']}{standard_member['이름']} 사원은 {member_to_compare['성']}{member_to_compare['이름']} 사원과 나이가 같습니다."


    def generate_introduce(self, member):
        if member['국적'] == '대한민국':
            return "안녕하세요, 저는 {} {}의 {}{}입니다.".format(
                self.team_prefix[member['소속']],
                member['소속'],
                member['성'],
                member['이름'])
        else:
            return "안녕하세요, 저는 {} {}의 {} {}입니다.".format(
                self.team_prefix[member['소속']],
                member['소속'],
                member['이름'],
                member['성'])