# consumindo_api_com_prefect
Desafio para realizar o consumo de dois endpoints de APIS usando o modulo Prefect



# Desafio Técnico

 - dev: [Enio Farias](mailto:eniodefarias@gmail.com)
 - data: 15/05/2024
 - repo: [github/consumindo_api_com_prefect](https://github.com/eniodefarias/consumindo_api_com_prefect)
 


# Proposta:
 Crie um repositório publico utilizando GIT e, utilizando Python, use a biblioteca Prefect (https://docs.prefect.io/latest/) para criar um projeto que consuma uma API externa (de sua preferência), construindo tarefas (flow tasks) que consuma dados de pelo menos 2 endpoints relacionados, sumulando timeout em um deles e utilizando retry, continuar o fluxo.

 PS: Sugestões de API para serem usadas (não é obrigatório a utilização das API’s abaixo. Você pode construir uma se quiser):
 - [ImageReport Wrapper - Report Dashboards](https://developers.thecatapi.com/)
 - [Rick and Morty API](https://rickandmortyapi.com)
 - [Deck of cards](https://deckofcardsapi.com)
 - [Public APIS](https://publicapis.dev)


## Avaliação

 - Padrão de codificação, utilização das melhores práticas e PEPs python;
 - Padrão e boas práticas de commit (não suba tudo em um commit só);
 - Estruturação de código;
 - Conhecimento de consumo de API’s;
 - Construção de API’s;
 - Questionamentos sobre padrões usadas e questões técnicas de python.

# Desenvolvimento do projeto

## Estudo para o caso

### biblioteca Prefect

#### Definição:
   - A biblioteca Prefect é uma ferramenta de orquestração de fluxo de trabalho que capacita desenvolvedores a construir, observar e reagir a pipelines de dados. É a maneira mais fácil de transformar qualquer função Python em uma unidade de trabalho que pode ser observada e orquestrada. Com o Prefect, você ganha recursos como agendamento, tentativas de repetição (retries), registro de logs (logging), funcionalidades assíncronas convenientes, cache, notificações e orquestração baseada em eventos

#### Pontos-chave sobre o funcionamento
 - Orquestração de Fluxos de Trabalho: Prefect permite que você defina fluxos de trabalho complexos como código Python. Você pode orquestrar a execução de várias tarefas, definindo dependências e condições para sua execução.
 - Observabilidade: Com Prefect, cada atividade é rastreada e pode ser monitorada. Isso inclui visualizar o progresso das tarefas, inspecionar logs e gerenciar estados de falha.
 - Recursos Automáticos: Prefect supercarrega seu código com recursos como tentativas automáticas de repetição, execução distribuída, agendamento, cache e muito mais, apenas com a adição de alguns decoradores.
 - Interface de Usuário: Prefect oferece uma interface de usuário onde você pode visualizar e interagir com seus fluxos de trabalho. Você pode iniciar fluxos de trabalho manualmente ou agendá-los para execução automática.
 - Prefect Cloud: Para aqueles que preferem uma solução gerenciada, o Prefect Cloud oferece orquestração centralizada, automações e webhooks, tudo respaldado por segurança de nível empresarial. Isso permite que você construa e gerencie seus fluxos de trabalho de dados de forma confiável e rápida1.
 - Prefect Client: Se o seu caso de uso está voltado para a comunicação com o Prefect Cloud ou um servidor Prefect remoto, o prefect-client é uma opção mais leve para acessar a funcionalidade do lado do cliente no SDK do Prefect1.

 #### Como usar
  - instalar a lib
  - definir tarefas(task) e fluxos(flow) com os decorators
  - executar o fluxo


## criando projeto e consumindo uma API

 - escolha da API:
   - [PokeAPI](https://pokeapi.co/)
     - motivo: é gratuita e é legal

 - prefect:
   - tasks
   - flow

 - requests

### estrutura e fluxo do código

 - importar os modulos
 - definir 1ª task para uma chamada request de 1 pkmn
 - definir 2ª task para uma chamada das tecnicas do pkmn para ter uma lista maior e timeout para forçar um retry, conforme a proposta do desafio
 - definir o flow para usar as tasks
 - executar tudo



 - sugestões e frescurinhas para o futuro, se der tempo:
   - adicionar algumas sinalizações em cada etapa
   - ~~add logs~~
   - talvez uma opção interativa 
   - talvez uma interface visual pyqt
   - UI web com flask

# como executar o projeto
 -
 - para os processos abaixo, considere o uso em um ambiente linux

## preparação do ambiente

 - realize o download do projeto:
   - ```bash
      git clone https://github.com/eniodefarias/consumindo_api_com_prefect.git 
     ```
 - entre no diretorio do projeto:
   - ```bash 
     cd  consumindo_api_com_prefect
     ```
 - crie um ambiente virtual com o venv:
   - ```bash
     python3 -m venv ./venv
     ```

 - ative o venv o terminal:
   - ```bash
       source ./venv/bin/activate
       ```
   
 - instale as bibliotecas do requirements.txt
   - ```bash
     cat requirements.txt|sort|uniq | xargs -n 1 pip install 
     ```
 
 
## executando
 - para executar use o comando:
   - ```bash
     python3 app.py     
        ```

## desativando o ambiente virtual
 - após terminar, desative o venv no console
   - ```bash
        deactivate
     ```