def greet_pythons(items: list) -> None:
    greeting = 'Hello' # free variable
    print(f'The ID of `greeting` in `greet_pythons` is {id(greeting)}')
    print(f'Local namespace in `greet_pythons`(1): {locals()}')

    def make_greeting(item: str) -> str:
        print(f'Local namespace in `make_greeting`(1): {locals()}')
        greeting = 'Hi' # prioritized variable when defined twice
        print(f'The ID of `greeting` in `make_greeting` is {id(greeting)}')
        print(f'Local namespace in `make_greeting`(2): {locals()}')
        return f'{greeting} {item}'

    for item in items:
        print(make_greeting(item))
    print(f'Inside greet_pythons, `greeting` is {greeting}')
    print(f'The ID of `greeting` in `greet_pythons` is {id(greeting)}')
    print(f'Local namespace in `greet_pythons`(2): {locals()}')


names = ['John']#, 'Eric', 'Graham', 'Terry', 'Terry', 'Michael']

greet_pythons(names)