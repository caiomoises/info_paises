from countryinfo import CountryInfo

while True:
    country_name = input('Digite o nome do país (ou "sair" para sair): ')
    if country_name.lower() == 'sair':
        break
    
    country = CountryInfo(country_name)
    print(f'Pais: {country.name()}')
    print(f'Capital: {country.capital()}')
    print(f'Moeda: {country.currencies()}')
    print(f'Idiomas: {country.languages()}')
    print(f'Fazem fronteiras: {country.borders()}')
    print(f'Codigo de área: {country.calling_codes()}')
    print(f'População: {country.population()}')
    print('\n')