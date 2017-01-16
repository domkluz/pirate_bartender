
def piratebartender (questions,ingredients):
    print("So do what do you fancy tonight. I have some suggestions")
    print(questions['strong'] + ". Press yes or just press enter...")
    response['strong']=bool(input())
    print(questions['salty'] + ". Press yes or just press enter...")
    response['salty']=bool(input())
    print(questions['bitter'] + ". Press yes or just press enter...")
    response['bitter']=bool(input())
    print(questions['sweet'] + ". Press yes or just press enter...")
    response['sweet']=bool(input())
    print(questions['fruity'] + ". Press yes or just press enter...")
    response['fruity']=bool(input())
    
    import random
    
    drink=[]
    
    if response['strong']==True:
        drink.append(random.choice(ingredients['strong']))
    if response['salty']==True:
        drink.append(random.choice(ingredients['salty']))
    if response['bitter']==True:
        drink.append(random.choice(ingredients['bitter']))
    if response['sweet']==True:
        drink.append(random.choice(ingredients['sweet']))
    if response['fruity']==True:
        drink.append(random.choice(ingredients['fruity']))
    if drink == []:
        print("Maybe you aint that thirsty")
    else:
        print("I recommend the following...")
        print(drink)



questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

response = {
    "strong": "",
    "salty": "",
    "bitter": "",
    "sweet": "",
    "fruity": "",
}


if __name__ == '__main__':
    piratebartender(questions,ingredients)    





