"""
Unity test per fs
"""

from fs import fs_do


class TestFS:
    def test_get_competitions(self):
        resp = fs_do('competitions')
        assert 147 == resp['count']

    def test_get_serieA(self):
        resp = fs_do('competitions/SA')
        assert 'Serie A' == resp['name']

    def test_get_single_matchday(self):
        resp = fs_do('competitions/SA/matches', filter='matchday=12')
        assert 247903 == resp['matches'][0]['id']

    def test_get_all_matches_of_a_player(self):
        resp = fs_do('players/2019/matches', filter='status=FINISHED')
        assert 'Gianluigi Buffon' == resp['player']['name']

# resp = fs_do('competitions')
# resp = fs_do('competitions/SA')
# resp = fs_do('competitions/SA/matches')
# resp = fs_do('competitions/SA/matches', filter='matchday=12')

# print(resp['count'])
# print(resp['filters'])
# print(resp['competitions'])
# print(resp['matches'])

# resp = fs_do('players/2019/matches', filter='status=FINISHED')
