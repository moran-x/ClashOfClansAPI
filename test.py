from CoC import CoC

CoC = CoC('APY_KEY')
#print (CoC.search_clan('-=KVB=-'))
#print (CoC.get_clan_info('#RCCG8VQV'))
#print (CoC.get_clan_members('#RCCG8VQV'))
#print (CoC.get_clan_warlog('#RCCG8VQV'))  # 403 in case of private war log

def get_clan_rushers(clan_tag):
    clan_members = CoC.get_clan_members(clan_tag)
    for line in clan_members['items']: 
        print(line['name'],  line['tag'])
        get_rusher(line['tag'])

#Узнать рашер игрок или нет.
def get_rusher(member_tag):
    member = CoC.get_clan_member(member_tag)
    m=CoC.is_rusher(member)
    print('Войска: ' + m['troops'])
    print('Заклинания: ' +m['spell'])
    print('---------------------')

#get_rusher('#9JPVVJURR') #TEST

get_clan_rushers('#9R2PYUJ8') #TEST
