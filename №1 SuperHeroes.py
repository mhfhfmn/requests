name = ['Hulk', 'Captain America', 'Thanos', 'Batman', 'Antman', 'Spider-man']

def get_all_intelligence(heroes_name):
    import requests
    url = 'https://www.superheroapi.com/api.php/2619421814940190/search/'
    all_intelligence = {}
    for hero in heroes_name:
        response = requests.get(f'''{url}{hero}''')
        intelligence = int(response.json()['results'][0]['powerstats']['intelligence'])
        all_intelligence.update({hero : intelligence})

    return all_intelligence



def max_intelligence():
    heroes_intelligence = get_all_intelligence(name)
    max_intelligence = name[0]
    for hero in name:
        if heroes_intelligence[hero] > heroes_intelligence[max_intelligence]:
            max_intelligence = hero

    return max_intelligence, heroes_intelligence[max_intelligence]



def main():
    hero_name, hero_intelligence = max_intelligence()
    print(f'''Самый умный супергерой - {hero_name} с показателем {hero_intelligence}''')



if __name__ == '__main__':
    main()
