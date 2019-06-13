import random
## code determines where indecisive people should go to eat dinner

def the_big_question():
    
    '''
    Asks you where should you eat tonight
    
    '''
    
    print('Where should we eat tonight?')

##amount of money available to spend on food per person; to determine budget is passed into function

def am_i_ballin(inp_1):
    
    """
    Determine what tier of restaurant user should go to depending on their budget
    
    Parameters
    ----------
    inp_1 = float; The number input here should be your budget for the night per person
    output = str
    
    """
    if inp_1 <= 20 and inp_1 > 10:
        print('pick a cheap place')
        output = 'pick a cheap place'
    elif inp_1 > 20 and inp_1 <= 40:
        print('you should be fine; go somewhere mid-tier')
        output = 'you should be fine; go somewhere mid-tier'
    elif inp_1 > 40:
        print('you are ballin! Go treat yo\'self!')
        output = 'you are ballin! Go treat yo\'self!'
    elif inp_1 <= 10:
        print('consider staying in tonight')
        output = 'consider staying in tonight'
    else:
        print('Try typing an integer or float my dude')
        output = 'Try typing an integer or float my dude'
    
    return output
        
def test_am_i_ballin():
    '''
    Tests function am_i_ballin
    
    '''
    
    assert am_i_ballin(5) == 'consider staying in tonight'
    assert am_i_ballin(100) == 'you are ballin! Go treat yo\'self!'
    
    
    
food_types = ['italian', 'mexican', 'chinese', 'american', 'indian', 'seafood', 'thai', 'mediterranean', 'japanese', 'have a home cooked meal!']

def type_of_cuisine():
    
    '''
    Determines type of food you'll eat tonight
    
    Parameters
    ----------
    output = random choice from food types
 
    '''
    output = random.choice(food_types)
    return output

        ## lists of different kinds of food at different price points
        
cheap_italian_eaterys = ['buca_di_beppo', 'dominos lol', 'little caesars']

mid_tier_italian = ['Villa Capri', 'Trattoria Ponte Vecchio', 'Vittorios']

high_tier_italian = ['Baci', 'Osteria Panevino', 'Catania']

cheap_mex_eaterys = ['tacos el gordo', 'rubios', 'Kotija jr.']

mid_tier_mex = ['casa sol y mar', 'la Puerta', 'Puesto']

high_tier_mex = ['Red O Taste of Mexico', 'Curadero', 'Javiers']

cheap_chinese_eaterys = ['Panda Express', 'Pick up Stix', ]

mid_tier_chinese = ['P.F. Changs', 'Noble Chef', 'Mandarin House']

high_tier_chinese = ['Mr Chow', 'WP24', 'CHANs Cuisine']

cheap_indian_eaterys = ['Bombay Coast', 'Punjabi Tandoor', 'Sher-e-Punjab']

mid_tier_indian = ['Royal India', 'Sitar', 'Virsa']

high_tier_indian = ['Clay Oven']

cheap_seafood_eaterys = ['Rubios', 'Subarashi', 'Ralphs']

mid_tier_seafood = ['Trulucks', 'Zip fusion', 'The Boiling Crab' ]

high_tier_seafood = ['Eddie Vs', 'Roys', 'Crab Catcher']

cheap_thai_eaterys = ['lemongrass', 'ruby thai', 'blue pepper']

mid_tier_thai = ['Taste of Thai', 'Star Anise', 'Aaharn Thai']

high_tier_thai = ['Spices Thai', 'Tumeric', 'Siam Nara']

cheap_med_eaterys = ['Santorini Grill', 'Daphnes', 'Mister Falafel']

mid_tier_med = ['Sultan Baklava', 'Kabob Lounge', 'Kebab Grill']

high_tier_med = ['Marketplace Grill', 'Sufi Mediterranean', 'Apollonia']

cheap_japanese_eaterys = ['Sushiya', 'Vons sushi', 'village market california roll']

mid_tier_japanese = ['Tajima','Robataya Oton', 'Sushi Kuchi']

high_tier_japanese = ['Nobu', 'Sushi Ota', 'Izakaya Masa']


   
              
def italian_place(inp_budget):
    
    """
    picks a specific restaurant for type of food and matches choice with your budget
    
    Parameters
    ----------
    inp_budget: Enter 'im broke rn' for a low-tier restaurant. Enter 'im able to spend a bit of money' for mid-tier restaraunt. Enter 'lets spend some money' for high-tier restaurant
    output: 
    """
    
    if inp_budget == 'im broke rn':
        output = random.choice(cheap_italian_eaterys)
    elif inp_budget == 'im able to spend a bit of money':
        output = random.choice(mid_tier_italian)
    elif inp_budget == 'lets spend some money':
        output = random.choice(high_tier_italian)
    return output

def mex_place(inp_budget):
    if inp_budget == 'im broke rn':
        output = random.choice(cheap_mex_eaterys)
    elif inp_budget == 'im able to spend a bit of money':
        output = random.choice(mid_tier_mex)
    elif inp_budget == 'lets spend some money':
        output = random.choice(high_tier_mex)
    return output

def american_place(inp_budget):
    if inp_budget == 'im broke rn':
        output = random.choice(cheap_american_eaterys)
    elif inp_budget == 'im able to spend a bit of money':
        output = random.choice(mid_tier_american)
    elif inp_budget == 'lets spend some money':
        output = random.choice(high_tier_american)
    return output

def indian_place(inp_budget):
    if inp_budget == 'im broke rn':
        output = random.choice(cheap_indian_eaterys)
    elif inp_budget == 'im able to spend a bit of money':
        output = random.choice(mid_tier_indian)
    elif inp_budget == 'lets spend some money':
        output = random.choice(high_tier_indian)
    return output
        

def chinese_place(inp_budget):
    if inp_budget == 'im broke rn':
        output = random.choice(cheap_chinese_eaterys)
    elif inp_budget == 'im able to spend a bit of money':
        output = random.choice(mid_tier_chinese)
    elif inp_budget == 'lets spend some money':
        output = random.choice(high_tier_chinese)
    return output

def seafood_place(inp_budget):
    if inp_budget == 'im broke rn':
        output = random.choice(cheap_seafood_eaterys)
    elif inp_budget == 'im able to spend a bit of money':
        output = random.choice(mid_tier_seafood)
    elif inp_budget == 'lets spend some money':
        output = random.choice(high_tier_seafood)
    return output

def thai_place(inp_budget):
    if inp_budget == 'im broke rn':
        output = random.choice(cheap_thai_eaterys)
    elif inp_budget == 'im able to spend a bit of money':
        output = random.choice(mid_tier_thai)
    elif inp_budget == 'lets spend some money':
        output = random.choice(high_tier_thai)
    return output

def mediterranean_place(inp_budget):
    if inp_budget == 'im broke rn':
        output = random.choice(cheap_med_eaterys)
    elif inp_budget == 'im able to spend a bit of money':
        output = random.choice(mid_tier_med)
    elif inp_budget == 'lets spend some money':
        output = random.choice(high_tier_med)
    return output

def japanese_place(inp_budget):
    if inp_budget == 'im broke rn':
        output = random.choice(cheap_japanese_eaterys)
    elif inp_budget == 'im able to spend a bit of money':
        output = random.choice(mid_tier_japanese)
    elif inp_budget == 'lets spend some money':
        output = random.choice(high_tier_japanese)
    return output








