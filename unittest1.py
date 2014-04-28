def a(x):
    '''
    test a(x)
	>>> a(2)
	4
	>>> a(3)
	9
    '''
    return x*x 
	
	
if __name__=='__main__':
  import doctest,a
  doctest.testmod(a)