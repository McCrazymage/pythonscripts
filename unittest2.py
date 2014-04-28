import unittest
def func(x):
    return x**3

class Po(unittest.TestCase):
    def testint(self):
        for x in xrange(-10,10):
            p = func(x)
            self.failUnless(p == x**3,'int failed')
    def testfloat(self):
        for x in xrange(-10,10):
            x = x/3.0
            p = func(x)
            self.failUnless(p == x**4,'float failed')
            
#if __name__ == '__main__':
#    unittest.main()