def str_to_int(string):
    """
    Parses a string number into an integer,optionally converting to a float
    and rounding down
    """

    error_msg="Unable to convert to integer :'%s'" % str(string)

    try:
        integer=float(string.replace(',','.'))
    except AttributeError:
        #this might be a integer already ,so try to use it ,oterwise raise

        if isinstance(string,(int,float)):
            integer = string
        else:
            raise RuntimeError(error_msg)
    except   (TypeError,ValueError):
        raise RuntimeError(error_msg)


    return int(integer)

class TestStrToInt:

    def setup(self):
        print('\nthis is setup')

    def teardown(self):
        print('\nthis is teardown')    

    def setup_class(cls):
        print('\nthis is setup class')     

    def teardown_class(cls):
        print('\nthis is teardown class')   

    def test_rounds_down(self):
        result=str_to_int('1.99')
        assert result == 2 

    def test_rounds_down_lesser_half(self):
        result=str_to_int('1.2')
        assert result == 2

"""
The setup_class method is executed once at the beginning of the test class.
The setup method is executed once at the beginning of each test function.
The teardown method is executed once at the end of each test function.
The setup method is executed again in preparation for the second test function.
The teardown method is executed once at the end of the second test function.
The teardown_class method is executed once at the end of the test class.
"""     