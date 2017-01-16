import requests

class CoC(object):
    BASE_URL = 'https://api.clashofclans.com/v1/'
    TROPS = ['Barbarian', 'Archer', 'Goblin', 'Giant', 'Wall Breaker', 'Balloon', 'Wizard', 'Healer', 'Dragon', 'P.E.K.K.A', 'Baby Dragon', 'Miner', 'Minion', 'Hog Rider', 'Valkyrie', 'Golem', 'Witch', 'Lava Hound', 'Bowler']
    SPEELS = ['Lightning Spell', 'Healing Spell', 'Rage Spell', 'Jump Spell', 'Freeze Spell', 'Clone Spell', 'Poison Spell', 'Earthquake Spell', 'Haste Spell', 'Skeleton Spell']
    TH_TROOPS = {2: [1, 1, 1, 1],
    3:[2,2,2,1,1], 
    4:[2,2,2,2,2,2], 
    5:[3,3,3,2,2,2,2], 
    6:[3,3,3,3,3,3,3,1], 
    7:[4,4,4,4,4,4,4,2,2,2,2], 
    8:[5,5,5,5,5,5,5,3,3,3,4,4,2,2], 
    9:[6,6,6,6,5,6,5,4,4,3,2,5,5,4,4,2,2], 
    10:[7,7,7,7,6,6,6,4,5,5,4,2,6,6,5,5,2,3,2], 
    11:[7,7,7,8,6,7,7,4,6,5,5,4,7,7,5,6,3,4,3]}
    TH_SPELL = {5:[4], 
    6:[4, 3], 
    7: [4,4,4],
    8: [5,5,5, 2,2],
    9: [6,6,5,2,1,3,3,2,2],
    10: [7,6,5,3,5,2,4,4,4,3],
    11: [7,6,5,3,5,4,5,4,4,4]}
    
    def __init__(self, token):
        """ Api instance Constructor
        """

        self.token = token
        self.headers = {'authorization': 'Bearer %s' % self.token, 'Accept': 'application/json'}

    def fetch(self, url, params=None):
        #print ("requesting endpoint : " + self.BASE_URL + url)
        #print ("---------------")
        result = requests.get(self.BASE_URL + url, headers=self.headers, params=params)
        """if result.status_code == 403:
        pass"""

        if result.status_code != 200:
            return [result.status_code, result.json()]
        return result.json()

    def search_clan(self, clanname=None, warfrequency=None, locationid=None, minmembers=None, maxmembers=None,
                    minclanpoints=None, minclanlevel=None, limit=10, after=None, before=None):
        params = dict(name=clanname,
                      warfrequency=warfrequency,
                      minmembers=minmembers,
                      maxmembers=maxmembers,
                      minclanpoints=minclanpoints,
                      minclanlevel=minclanlevel,
                      limit=limit,
                      after=after,
                      before=before)
        return self.fetch('clans', params=params)

    def get_clan_info(self, tag):
        return self.fetch('clans/' + tag.replace('#', '%23'))

    def get_clan_members(self, tag):
        return self.fetch('clans/' + tag.replace('#', '%23') + '/members')

    def get_clan_warlog(self, tag):
        return self.fetch('clans/' + tag.replace('#', '%23') + '/warlog')

    def get_clan_member(self, tagmember):
        return self.fetch('players/' + tagmember.replace('#', '%23'))
        
    def is_rusher(self,  member_data):
        trops_level = []
        spell_level = []
        member_th = member_data['townHallLevel'] 
        for line in member_data['troops']: 
            if line['name'] in self.TROPS:
                trops_level.append(line['level'])
        
        for line in member_data['spells']:  
            if line['name'] in self.SPEELS:
                spell_level.append(line['level'])
        
        if trops_level < self.TH_TROOPS[int(member_th)-1]:
            member_is_rusher = {'troops': "rusher"}
        else:
            member_is_rusher = {'troops': "ok"}
        
        if int(member_th) > 5:
            if spell_level < self.TH_SPELL[int(member_th)-1]:
                member_is_rusher['spell'] = "rusher"
            else:
                member_is_rusher['spell'] = "ok"
        else:
            member_is_rusher['spell'] = "NONE"
        return member_is_rusher
