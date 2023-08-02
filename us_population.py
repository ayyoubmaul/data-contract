from plugins.validation.data_contract import DataContract
from plugins.table_schema.us_population import Population
import requests

@DataContract(Population)
def main():
    response = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
    response.raise_for_status()

    data = response.json()['data']

    data[0]['ID Nation'] = 1234

    data_clean = [{key.lower().replace(' ', '_'): val for key, val in item.items()} for item in data]

    return data_clean

if __name__ == '__main__':
    main()
