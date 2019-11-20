# test
import requests

def change_lv_people(x):
    url = 'http://188.188.1.202:20006/chess//league/manage/saveMatchReward'

    head = {
        "UserKey": "171141_1573271339451_1_58902dbc860a5343dfdb54365215c06a",
        "OfficeId": "10001",
    }

    form = {
        "leagueId":48,
        "maxRank":x,
        "minRank":x,
        "rewardInfo":'',
        "rewardType":'1'

    }

    data = requests.post(url=url,headers=head,data=form)

    print(data.json())

def run_change_lv_people():
    for i in range(41,200):
        try:
            change_lv_people(i)
        except:
            print("error")

def add_club_people(clubId,fId):
    url = 'http://188.188.1.202:20006/chess//club/clubjoinRequest/inviteFriendJoin'

    head = {
        "UserKey": "171141_1573528589599_1_7f3259b8449f816e3eb42d225268bc92",
        "OfficeId": "10001",
    }

    form = {
        "clubId":clubId,
        "friendsId":fId

    }

    data = requests.post(url=url,headers=head,data=form)

    print(data.json())

def four_year():
    url = "http://m.dabqg.com/html/6_6106/2417896.html"

    data = requests.post(url= url)

    str = data.content

    print(str.decode('unicode_escape'))


if __name__ == '__main__':
    # add_club_people(1378,171277)
    four_year()

