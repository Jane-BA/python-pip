import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv('./app/data.csv')
    data = list(filter(lambda item : item['Continent'] == 'North America', data))

    countries = list(map(lambda x : x['Country/Territory'], data))
    percentages = list(map(lambda y : y['World Population Percentage'], data))

    charts.generate_pie_chart(countries, percentages)
    
#Corre sig grafica
    country = input('Type Country => ')
    result =utils.population_by_county(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        print(labels, values)
        charts.generate_bar_chart(labels, values)

    print(result)

if __name__ == '__main__':
    run()