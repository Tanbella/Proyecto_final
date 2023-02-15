def get_game(dic):
    hours_games = {
        "watched":int(dic['Hours_watched']),
        "Streamed":int(dic['Hours_Streamed']),
        "Streamers":int(dic['Streamers']),
        }    
    labels = hours_games.keys() #para poder graficar se le asignan labels
    values = hours_games.values() #para poder graficar se le asignan values
    return labels, values
 

def name_by_game(data, game):
  result = list(filter(lambda item: item['Game'] == game, data))
  return result