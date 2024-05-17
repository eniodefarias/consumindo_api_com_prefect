import unittest
from unittest.mock import patch
from app import get_pokemon_info, get_pokemon_encounters


class TestPokemonAPI(unittest.TestCase):

    @patch('app.requests.get')
    def test_get_pokemon_info(self, mock_get):
        # Configura o mock para retornar um response com status_code 200
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'name': 'pikachu'}

        # Chama a função com o nome do Pokémon
        response = get_pokemon_info('pikachu')

        # Verifica se a resposta é a esperada
        self.assertEqual(response['name'], 'pikachu')

    @patch('app.requests.get')
    def test_get_pokemon_encounters(self, mock_get):
        # Configura o mock para retornar um response com status_code 200
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'location_area': 'viridian-forest-area'}

        # Chama a função com o nome do Pokémon e um timeout
        response = get_pokemon_encounters('pikachu', 10)

        # Verifica se a resposta é a esperada
        self.assertEqual(response['location_area'], 'viridian-forest-area')


if __name__ == '__main__':
    unittest.main()
