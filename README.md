Этот модуль использует официалный API Clash of Clans


Получить API ключ https://developer.clashofclans.com


```sh
from CoC import CoC

CoC = CoC('<APIKEY>')
CoC.search_clan('ozaki league')
CoC.get_clan_info('#QU9R8P09')
CoC.get_clan_members('#QU9R8P09')
CoC.get_clan_warlog('#QU9R8P09')  # returns 403 in case of private war log
CoC.get_clan_member('#9JPVVJURR')
```