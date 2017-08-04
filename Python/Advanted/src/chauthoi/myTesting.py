#!/usr/bin/env python 2.7
#Fail-Erro
import unittest
class TestSuper(unittest.TestCase):
    def setUp(self):
        print 'Setting up case'
    def tearDown(self):
        print 'Cleaning up case'
class Test(TestSuper):
    def runTest(self):
        """Test add"""
        print 'Running Test 1'
        self.failUnless(1+1==2,'one and one plus')
        self.failIf(1+1!=2,'one and one plus agian')
        self.failUnlessEqual(1+1,2,'more trouble')
class TestFail(TestSuper):
    def runTest(self):
        """Test add"""
        print 'Running Test 2!'
        self.failUnless(1+1==2,'one and one plus')
        self.failIf(1+1!=2,'one and one plus agian')
        self.failUnlessEqual(1+1,2,'more trouble')
        self.failIfEqual(1+1,2,'Expected here')
        self.failIfEqual(1+1,2,'second fails')
class Test2(unittest.TestCase):
    def setUp(self):
        print 'Setting Test 2'
    def tearDown(self):
        print 'Cleaning Test 2'
    def runTest2(self):
        """run Test add"""
        print 'Running Test 2 *'
        self.failUnless(1+1==2,'one and one plus')
        self.failIf(1+1!=2,'one and one plus agian')
        self.failUnlessEqual(1+1,2,'more trouble')
    def runTestFail(self):
        """run Test add """
        print 'Running Test Fail *'
        self.failUnless(1+1==2,'one and one plus')
        self.failIf(1+1!=2,'one and one plus agian')
        self.failUnlessEqual(1+1,2,'more trouble')
        self.failIfEqual(1+1,2,'Expected here')
        self.failIfEqual(1+1,2,'second fails')
    def suite():
        suite=unittest.TestSuite()
        #Frist
        suite.addTest(Test)
        suite.addTest(TestFail)
        #Second
        suite.addTest(Test2('runTest'))
        suite.addTest(Test2('runTestFail'))
        return suite
    if __name__ == '__main__':
        runner=unittest.TextTestRunner()
        test_suite=suite()
        runner.run(test_suite)