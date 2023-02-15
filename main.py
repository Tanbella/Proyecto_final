import read_csv
import charts
import utils

def run():# obtener la data 
    data = read_csv.read_csv("data.csv")#modulo.funcion
    data = list(filter(lambda item: item['Year'] == '2018', data ))
    games = list(map(lambda x: x['Game'], data)) #selecciona solo la columna
    espectadores = list(map(lambda x: x['Avg_viewer_ratio'], data))
    charts.generate_pie_chart(games, espectadores)


"""     game = input("Ingrese el nombre del juego: ")

    resultado = utils.name_by_game(data, game)

    if len(resultado)>0: 
        game = resultado[0]
        labels, values = utils.get_game(dic)
        charts.generate_bar_chart(labels, values) """


if __name__ == '__main_':
    run()