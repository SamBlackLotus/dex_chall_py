# Curiosidades 

1. A pergunta/função que conta quantos stages diferentes de digimon existem no arquivo, e em seguida lista eles, porém 
ela simplesmente lista na ordem em que eles aparecem no arquivo, e em seguida lista eles sem colocar uma vírgula entre 
elas. Eu queria saber se seria possível que na hora de imprimir na resposta, fazer com que os stages saíssem ordenados.

Ex:

    {
        "Id": 304,
        "Name": "Ravemon",
        "Stage": "Mega",
    },
    {
        "Id": 144,
        "Name": "Andromon",
        "Stage": "Ultimate",
    },
    {
        "Id": 2,
        "Name": "Pabumon",
        "Stage": "Baby",
    },
    {
        "Id": 120,
        "Name": "Nanimon",
        "Stage": "Champion",
    },
    {
        "Id": 269,
        "Name": "HiAndromon",
        "Stage": "Mega",
    },

Hoje o programa imprime: In this list we have 4 stages of digimon, they're Mega Ultimate Baby Champion

Como eu queria que saísse: In this list we have 4 stages of digimon, they're Baby, Champion, Ultimate, Mega

É só uma questão de estética e organização mesmo.

# Dúvidas

1. Como eu documento lambda e comprehension no mypy? Pq ele ta misturando os comandos com a documentação.(eu acho que é isso)