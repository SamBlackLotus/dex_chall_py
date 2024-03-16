# Questions and Answers

Q. A pergunta/função que conta quantos stages diferentes de digimon existem no arquivo, e em seguida lista eles, porém ela simplesmente lista na ordem em que eles aparecem no arquivo, e em seguida lista eles sem colocar uma vírgula entre elas. Eu queria saber se seria possível que na hora de imprimir na resposta, fazer com que os stages saíssem ordenados.

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

>
    A. You can sort the list (ref: https://docs.python.org/3/howto/sorting.html), there are many ways to do that, but 2 common ways are:

    - Using sort: This will change the data in place.
    ```
    >>> stages = ["Mega", "Ultimate", "Baby", "Champion"]
    >>> stages.sort()
    >>> print(stages)
    ['Baby', 'Champion', 'Mega', 'Ultimate']
    ```

    - Using sorted:
    ```
    >>> stages = ["Mega", "Ultimate", "Baby", "Champion"]
    >>> sorted_stages = sorted(stages)
    >>> print(stages)
    ["Mega", "Ultimate", "Baby", "Champion"]
    >>> print(sorted_stages)
    ['Baby', 'Champion', 'Mega', 'Ultimate']
    ```

    To make them separate by comma you can do the following:

    ```
    >>> ", ".join(sorted(stages))
    ```

Q. Como eu documento lambda e comprehension no mypy? Pq ele ta misturando os comandos com a documentação.(eu acho que é isso)

>
    A. A lambda is an anonymous function, therefore you can add typing in a similar way as we would do to a function reference, using Callable (https://docs.python.org/3/library/typing.html#typing.Callable): 

    ```
    lbd: Callable[[int], int] = lambda x: x*x
    ```

    The list comprehension generates a list in the end, so just add typing similar to how you would create for a list, using List[arg_type].

Q. Como definir o que é hardcode e o que deve ser fixo, pois por exemplo, no example do challenge_1, foi definido o tamanho do maior pokemon usando a key height, mas se eu tiver um arquivo de pokemon, com o nome Height, ou Hght, ou qualquer outra forma de se ler altura, no código já precisaria de tratamento e o mesmo ocorreria se eu tentasse puxar de modo genérico por número da chave, já que um arquivo com os campos em ordenação diferente, acabaria com a lógica, então a minha dúvida é, até onde eu devo deixar o código genérico, onde que eu traço a linha do que é hardcode dentro do meu código?

> A. It depends what the scope of the hardcode problem is, in your example you can do a data pipeline to change the column name so that your app only receives an unique name for the headers.  

Q. A alteração que foi feita essa semana foi, foi retirada a validação pelo comando --pokemon --digimon, e inserida a validação pelo nome do arquivo carregado, porém isso ainda deixa aberta a possibilidade de dar entrada num arquivo com nome pokemon e informações de digimon, por isso a ideia é adicionar uma camada de validação pós processamento que verifique os campos Stage e Legendary.

> A. Yes, it's a good pattern to validate the data you receive.

Q. As perguntas vão ser transformadas em funções, mas onde/em que arquivo essas funções vão? E como eu chamo elas?

> A. Here goes an example of how you could map the questions and the functions.

questions_config.csv
```
question_id,question_detail,function
1,"How many pokemons there is in this list",func_count_monsters
```
