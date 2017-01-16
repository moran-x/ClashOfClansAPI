from CoC import CoC

CoC = CoC('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjRkM2Y2NDBkLTUzMTEtNGZiZC1hM2NmLWM5NjNiZWQ2N2Y2NiIsImlhdCI6MTQ3MzEzNDg1OCwic3ViIjoiZGV2ZWxvcGVyL2JkY2ZiNDA3LWU2NmUtNzg2MC0wMGY5LWVmMWNhYTBjMGVjYSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjUuMTI4LjMxLjE1NiIsIjM3LjE5My4xNi4xMTciXSwidHlwZSI6ImNsaWVudCJ9XX0.Mg69SqS5XCMcQ_AKULHuSxDhBBcSIoRsiuG--84Vf2j-5xjXC-8Bo1kjh4r77qtDgoV3Wjf2kz6DOfmf1Atfhg')
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

#get_rusher('#9QCGGRY9Y') #YODA
#get_rusher('#9JPVVJURR') #DIMON
#get_rusher('#Q2Q2RLYG') #ArhanGel
#get_rusher('#G89PRJV2') #TVIN
#get_rusher('#9JPVVJURR') #TEST

get_clan_rushers('#RCCG8VQV') #-=KVB=-
#get_clan_rushers('#9R2PYUJ8') #TEST
