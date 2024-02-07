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
