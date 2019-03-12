from pycricbuzz import Cricbuzz

c = Cricbuzz()
matches = c.matches()
match = matches[0]

# print c.livescore(match['id'])
commentary_recent = c.commentary(match['id'])
# print commentary_recent
comment_1 = commentary_recent['commentary']
for comm in comment_1:

    try:
        over = comm['over']
        print over
        commentaryyy = comm['comm']
        details = commentaryyy.split(',')[0]
        print("bowler/batsman", details)
        runs = commentaryyy.split(',')[1]
        print("RUNS", runs)
        print("Commentary", commentaryyy)
    except:
        pass