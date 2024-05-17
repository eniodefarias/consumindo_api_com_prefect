import time

from prefect import task, flow
import requests
import time

# task para puxar só 1 pkmn
@task
def get_pokemon_info(pokemon_name):
    print(f'a1 - get_pokemon_info pokemon_name={pokemon_name}')
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    #print(f'a2 - lendo response={response}')
    if response.status_code != 200:
        raise Exception('a3 - Falha na requisição da API')
    return response.json()


# task para puxar habilidades do mesmo pkmn, com retry e timeout
###  esse decorator só funciona no prefect 1.x
###     @task(max_retries=3, retry_delay=timedelta(seconds=5), timeout=10)
###  no prefct2 é diferente, é direto no flow
@task
def get_pokemon_encounters(pokemon_name, timeout):
    print(f'b1 - get_pokemon_encounters pokemon_name={pokemon_name}')
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/encounters', timeout=timeout)

    # print(f'b2 - response.status_code={response.status_code}')

    # print(f'b3 - lendo response={response}')
    if response.status_code != 200:
        raise Exception('b4 - Falha na requisição da API ou timeout')
    return response.json()


# fluxo para puxar as tasks
@flow(retries=3, retry_delay_seconds=5)
def poke_flow(pokemon_name: str = 'ditto', timeout: float = 10):

    print(f'c1 - pesquisando pokemon_name={pokemon_name}\n\n')
    pokemon_info = get_pokemon_info(pokemon_name)['stats']  #coloquei a chave só para não imprimir um caminhão de dados
    print(f'c2 - {pokemon_name} >>  pokemon_info={pokemon_info}\n\n')
    time.sleep(5)
    pokemon_encounters = get_pokemon_encounters(pokemon_name, timeout)
    print(f'c3 - {pokemon_name} >> pokemon_encounters={pokemon_encounters}\n\n')


# Let's rock
if __name__ == '__main__':
    print(f'Executando app sem timeout')
    time.sleep(5)
    poke_flow()
    print(f'\n\n---------\n\n')
    time.sleep(5)
    print(f'Executando app COM timeout e retry')
    time.sleep(5)
    poke_flow(pokemon_name='jolteon', timeout=0.001)
