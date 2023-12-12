def test_pass():
    assert True

def test_fails():
    assert True
    #assert False

def test_long_lists():
    result=['this','is','a','list']
    excepted=['this','is','a','list']
    #excepted=['this','is','A','list']
    assert result==excepted


result=['this','is','a','list','aA']
def test_long_lists():    
    excepted=['this','is','A','list']
    assert result==excepted    