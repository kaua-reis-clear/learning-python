questions = [
    {
        'Question': 'How much is 2+2?',
        'Options': ['1', '3', '4', '5'],
        'Answer': '4',
    },
    {
        'Question': 'How much is 5*5?',
        'Options': ['25', '55', '10', '51'],
        'Answer': '25',
    },
    {
        'Question': 'How much is 10/2?',
        'Options': ['4', '5', '2', '1'],
        'Answer': '5',
    },
]

hit_amount = 0
for question in questions:
    print('Question:', question['Question'])
    print()

    options = question['Options']
    for i, option in enumerate(options):
        print(f'{i})', option)
    print()

    escolha = input('Choose an option: ')

    hit = False
    choose_int = None
    option_amount = len(options)

    if escolha.isdigit():
        choose_int = int(escolha)

    if choose_int is not None:
        if choose_int >= 0 and choose_int < option_amount:
            if options[choose_int] == question['Answer']:
                hit = True

    print()
    if hit:
        hit_amount += 1
        print('Hit 👍')
    else:
        print('Miss ❌')

    print()


print('You hit', hit_amount)
print('out of', len(questions), 'questions.')