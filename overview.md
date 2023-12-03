# Hello Samara

Welcome to the first of many challenges that will unlock new opportunities for your carrer!
The full challenge will consist of many incremental steps that increases the level of difficulty as you go. The requirements for the amount of data, technologies used, code practices, documentation, will be incremental as well.

**Important:** Each step of the challenge needs to be in github so that I can review it, so please, as a "zero" step, create a public repository in your github and share the link with me. You are free to commit directly on main branch, and please use relevant comments on each modification in english. All your code should be in english as well.

## Roadmap

There is no hard deadline for the steps below, but it would be nice if we could advance each step every week.

- CLIs, interactive terminal menu, data aggregation and files:
1. Create a CLI that will receive the name of the pokedex file and provide answers for some questions.
2. The CLI that reads the file now will have an interactive terminal menu that will provide answers for some questions as the users selects the options.
3. The interactive terminal menu will log into files each action that the user selects and generate a final report of the information that the user request.

- Web:
1. Now you need to gather the pokemon information from the API https://pokeapi.co/docs/v2/pokemon and print some relevant info about the data in the terminal.
2. You need to gather the data from the inner urls that comes in each pokemon information, aggregate those information and show some relevant info about the data in the terminal.
3. After capture these data, store it in a database, and aggreagate the data from the database to show relevant information in the terminal.
4. Add a fastapi web framework to show the relevant aggregate data from the db in the browser.
5. Choose any client side language / framework to build a frontend for these data in the browser.

- To be continued...

## Data

During the whole challenge you will be using one data source, a pokedex.
All the data will come from this service: https://pokeapi.co/docs/v2.
The very first challenge won't include all the data to not overflow you with lots of information in the beginning, but as you step in new challenges I will provide more information to be processed.

## Techs requeriments

Basics:
- Linux, ubuntu
- Python 3.9
- git, github

Advanced:
- Poetry
- Fastapi
- Postgresql
