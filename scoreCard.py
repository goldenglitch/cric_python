from pycricbuzz import Cricbuzz
c = Cricbuzz()
matches = c.matches()
match=matches[0]

scorecard_required=c.scorecard('21534')
print scorecard_required['scorecard'][0]['runs']
print scorecard_required['scorecard'][0]['bowlteam']
print scorecard_required['scorecard'][0]['batteam']
print scorecard_required['scorecard'][0]['overs']
print scorecard_required['scorecard'][0]['wickets']
