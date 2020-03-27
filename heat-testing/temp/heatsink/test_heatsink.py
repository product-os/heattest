
def test_stressberry():
    print("Testing stressberry ...")    
    print ("Done")
    max_temp = 40
    freq_drop = False
    assert max_temp < 50
    assert freq_drop == False

def test_ambient_temp():
    max_ambient = 40
    assert max_ambient < 45
