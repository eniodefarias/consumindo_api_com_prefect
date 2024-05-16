from prefect import task, flow
import requests


# task para puxar só 1 pkmn
@task
def get_pokemon_info(pokemon_name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    print(f'a1 - lendo response={response}')

    return response.json()


# task para puxar habilidades do mesmo pkmn, com retry e timeout
###  esse decorator só funciona no prefect 1.x
###     @task(max_retries=3, retry_delay=timedelta(seconds=5), timeout=10)
###  no prefct2 é diferente, é direto no flow
@task
def get_pokemon_abilities(pokemon_name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/abilities', timeout=1)
    print(f'b1 - lendo response={response}')

    return response.json()


# fluxo para puxar as tasks
@flow(retries=3, retry_delay_seconds=5)
def poke_flow(pokemon_name: str = 'ditto'):
    print(f'c1 - pesquisando pokemon_name={pokemon_name}')
    pokemon_info = get_pokemon_info(pokemon_name)
    print(f'c2 - pokemon_info={pokemon_info}')
    pokemon_abilities = get_pokemon_abilities(pokemon_name)
    print(f'c3 - pokemon_abilities={pokemon_abilities}')


# Let's rock
if __name__ == '__main__':
    print(f'Executando app:')
    poke_flow(pokemon_name='jolteon')
