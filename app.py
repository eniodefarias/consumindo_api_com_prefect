from prefect import task, Flow, Parameter
import requests
from datetime import timedelta


# task para puxar só 1 pkmn
@task
def get_pokemon_info(pokemon_name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    print(f'a1 - lendo response={response}')

    return response.json()

# task para puxar habilidades do mesmo pkmn, com retry e timeout
@task(max_retries=3, retry_delay=timedelta(seconds=5), timeout=10)
def get_pokemon_abilities(pokemon_name):

    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/abilities',
                            timeout=1)
    print(f'b1 - lendo response={response}')

    return response.json()

# fluxo para puxar as tasks
with Flow("Fluxo de Informações do Pokémon") as flow:
    pokemon_name = Parameter('pokemon_name', default='ditto')

    pokemon_info = get_pokemon_info(pokemon_name)
    pokemon_abilities = get_pokemon_abilities(pokemon_name)

# Let's rock
if __name__ == "__main__":
    flow.run(parameters={"pokemon_name": "jolteon"})