from my_module import am_i_ballin, test_am_i_ballin

def test_am_i_ballin():
    '''
    Tests function am_i_ballin
    
    '''
    
    assert am_i_ballin(5) == 'consider staying in tonight'
    assert am_i_ballin(100) == 'you are ballin! Go treat yo\'self!'