from flask import Flask
from flask_restful  import Api,Resource,reqparse
from pycricbuzz import Cricbuzz
import json
import re

app=Flask(__name__)
api = Api(app)

class getCommentary(Resource):
    def get(self,mid):
        c = Cricbuzz()
        dict_1 = {}
        list_1 = []
        
        commentary_recent = c.commentary(mid)
        # print commentary_recent
        comment_1 = commentary_recent['commentary']
        for comm in comment_1:

            over = comm['over']
            
            if over is not None:
                    try:

                            dict_1['over']=over
                            print over
                            commentaryyy = comm['comm']
                            details = commentaryyy.split(',')[0]
                            print("bowler/batsman", details)
                            dict_1['details']=details
                            runs = re.sub("<.*?>","",commentaryyy.split(',')[1])
                            runs = runs.split(' ')[1]

                            if (runs == 'FOUR'):
                                runs = 4
                            elif(runs == 'no'):
                                runs = 0
                            elif(runs == 'wide'):
                                runs = 1
                            elif(runs == 'leg'):
                                runs = 1
                            elif(runs == 'SIX'):
                                runs = 6
                            elif(over is None):
                                runs = 0

                            print(runs)

                            dict_1['runs'] = runs
                            commentaryyy = re.sub("<.*?>","",commentaryyy)

                            print("Commentary", commentaryyy)
                            dict_1['commentary'] = commentaryyy
                            list_1.append(dict_1)
                            dict_1 = {}

                    except:

                            pass

        print list_1
        return list_1[0],200

   
class ListOfLive(Resource):

     def get(self):
         c = Cricbuzz()
         dict = {}
         list1 = []
         
         matches = c.matches()
         for match in matches:
             if (match['mchstate'] != 'nextlive' and match[
                 'mchstate'].startswith("inprogress") == True):
                 match_details = match['team1']['name'] + " vs " + match['team2']['name']
                 dict['matchId'] = match['id']
                 dict['matchDetails'] = match_details
                 list1.append(dict)
                 dict = {}
         
         print list1
         return list1,200


class ScoreCard(Resource):

    def get(self,mid):
        c = Cricbuzz()
        dict = {}
        scorecard_required = c.scorecard(mid)
        dict['runs'] =scorecard_required['scorecard'][0]['runs']
        dict['bowlteam'] =scorecard_required['scorecard'][0]['bowlteam']
        dict['batteam'] =scorecard_required['scorecard'][0]['batteam']
        dict['overs'] =scorecard_required['scorecard'][0]['overs']
        dict['wickets'] = scorecard_required['scorecard'][0]['wickets']
        return dict, 200


api.add_resource(getCommentary,"/getCommentary/<string:mid>")
api.add_resource(ListOfLive,"/getLiveMatches")
api.add_resource(ScoreCard,"/getScoreCard/<string:mid>")

app.run(debug = True, host = '0.0.0.0')


