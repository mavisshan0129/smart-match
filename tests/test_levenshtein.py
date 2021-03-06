import unittest
import smart_match

class TestLevenshtein(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('LE')

    def test_similarity(self):
        self.assertEqual(smart_match.similarity('hello', 'hero'), 0.6)
        self.assertEqual(smart_match.similarity('Subsitute', 'Subsytute'), 0.8888888888888888)
        self.assertEqual(smart_match.similarity('Subsitute', 'Sybsytyte'), 0.6666666666666667)
        self.assertEqual(smart_match.similarity('abc', 'abcdef'), 0.5)
        self.assertEqual(smart_match.similarity('def', 'abcdef'), 0.5)
        self.assertEqual(smart_match.similarity('test string1','test string2'),0.9166666666666666)
        self.assertEqual(smart_match.similarity('test','test string2'),0.33333333333333337)
        self.assertEqual(smart_match.similarity('','test string2'),0.0)
        self.assertEqual(smart_match.similarity('aaa bbb ccc ddd','aaa bbb ccc eee'),0.8)
        self.assertEqual(smart_match.similarity('aaa bbb','aaa aaa'),0.5714285714285714)
        self.assertEqual(smart_match.similarity('aaa','aaa aaa'),0.4285714285714286)
        self.assertEqual(smart_match.similarity('a b c d','a b c e'), 0.8571428571428572)
        self.assertEqual(smart_match.similarity('Healed','Sealed'),0.8333333333333334)
        self.assertEqual(smart_match.similarity('Healed','Healthy'),0.5714285714285714)
        self.assertEqual(smart_match.similarity('Healed','Heard'),0.6666666666666667)
        self.assertEqual(smart_match.similarity('Healed','Herded'),0.6666666666666667)
        self.assertEqual(smart_match.similarity('Healed','Help'),0.5)
        self.assertEqual(smart_match.similarity('Healed','Sold'),0.33333333333333337)
        self.assertEqual(smart_match.similarity('Healed','Help'),0.5)
        self.assertEqual(smart_match.similarity('Sam J Chapman','Samuel John Chapman'),0.6842105263157895)
        self.assertEqual(smart_match.similarity('Sam Chapman','S Chapman'),0.8181818181818181)
        self.assertEqual(smart_match.similarity('John Smith','Samuel John Chapman'),0.26315789473684215)
        self.assertEqual(smart_match.similarity('John Smith','Sam Chapman'),0.0)
        self.assertEqual(smart_match.similarity('John Smith','Sam J Chapman'),0.07692307692307687)
        self.assertEqual(smart_match.similarity('John Smith','S Chapman'),0.09999999999999998)
        self.assertEqual(smart_match.similarity('Web Database Applications','Web Database Applications with PHP & MySQL'),0.5952380952380952)
        self.assertEqual(smart_match.similarity('Web Database Applications','Creating Database Web Applications with PHP and ASP'),0.4509803921568627)
        self.assertEqual(smart_match.similarity('Web Database Applications','Building Database Applications on the Web Using PHP3'),0.42307692307692313)
        self.assertEqual(smart_match.similarity('Web Database Applications','Building Web Database Applications with Visual Studio 6'),0.4545454545454546)
        self.assertEqual(smart_match.similarity('Web Database Applications','Web Application Development With PHP'),0.25)
        self.assertEqual(smart_match.similarity('Web Database Applications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),0.28735632183908044)
        self.assertEqual(smart_match.similarity('Web Database Applications','Structural Assessment: The Role of Large and Full-Scale Testing'),0.15873015873015872)
        self.assertEqual(smart_match.similarity('Web Database Applications','How to Find a Scholarship Online'),0.15625)
        self.assertEqual(smart_match.similarity('Web Aplications','Web Database Applications with PHP & MySQL'),0.3571428571428571)
        self.assertEqual(smart_match.similarity('Web Aplications','Creating Database Web Applications with PHP and ASP'),0.2941176470588235)
        self.assertEqual(smart_match.similarity('Web Aplications','Building Database Applications on the Web Using PHP3'),0.25)
        self.assertEqual(smart_match.similarity('Web Aplications','Building Web Database Applications with Visual Studio 6'),0.2727272727272727)
        self.assertEqual(smart_match.similarity('Web Aplications','Web Application Development With PHP'),0.38888888888888884)
        self.assertEqual(smart_match.similarity('Web Aplications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),0.1724137931034483)
        self.assertEqual(smart_match.similarity('Web Aplications','Structural Assessment: The Role of Large and Full-Scale Testing'),0.11111111111111116)
        self.assertEqual(smart_match.similarity('Web Aplications','How to Find a Scholarship Online'),0.1875)
        

    def test_dissimilarity(self):
        self.assertEqual(smart_match.dissimilarity('hello', 'hero'), 0.4)
        self.assertEqual(smart_match.dissimilarity('Subsitute', 'Subsytute'), 0.1111111111111111)
        self.assertEqual(smart_match.dissimilarity('Subsitute', 'Sybsytyte'), 0.3333333333333333)
        self.assertEqual(smart_match.dissimilarity('abc', 'abcdef'), 0.5)
        self.assertEqual(smart_match.dissimilarity('def', 'abcdef'), 0.5)
        self.assertEqual(smart_match.dissimilarity('test string1','test string2'),0.08333333333333333)
        self.assertEqual(smart_match.dissimilarity('test','test string2'),0.6666666666666666)
        self.assertEqual(smart_match.dissimilarity('','test string2'),1.0)
        self.assertEqual(smart_match.dissimilarity('aaa bbb ccc ddd','aaa bbb ccc eee'),0.2)
        self.assertEqual(smart_match.dissimilarity('aaa bbb','aaa aaa'),0.42857142857142855)
        self.assertEqual(smart_match.dissimilarity('aaa','aaa aaa'),0.5714285714285714)
        self.assertEqual(smart_match.dissimilarity('a b c d','a b c e'),0.14285714285714285)
        self.assertEqual(smart_match.dissimilarity('Healed','Sealed'),0.16666666666666666)
        self.assertEqual(smart_match.dissimilarity('Healed','Healthy'),0.42857142857142855)
        self.assertEqual(smart_match.dissimilarity('Healed','Heard'),0.33333333333333333)
        self.assertEqual(smart_match.dissimilarity('Healed','Herded'),0.33333333333333333)
        self.assertEqual(smart_match.dissimilarity('Healed','Help'),0.5)
        self.assertEqual(smart_match.dissimilarity('Healed','Sold'),0.6666666666666666)
        self.assertEqual(smart_match.dissimilarity('Healed','Help'),0.5)
        self.assertEqual(smart_match.dissimilarity('Sam J Chapman','Samuel John Chapman'),0.3157894736842105)
        self.assertEqual(smart_match.dissimilarity('Sam Chapman','S Chapman'),0.18181818181818182)
        self.assertEqual(smart_match.dissimilarity('John Smith','Samuel John Chapman'),0.7368421052631579)
        self.assertEqual(smart_match.dissimilarity('John Smith','Sam Chapman'),1.0)
        self.assertEqual(smart_match.dissimilarity('John Smith','Sam J Chapman'),0.9230769230769231)
        self.assertEqual(smart_match.dissimilarity('John Smith','S Chapman'),0.9)
        self.assertEqual(smart_match.dissimilarity('Web Database Applications','Web Database Applications with PHP & MySQL'),0.40476190476190477)
        self.assertEqual(smart_match.dissimilarity('Web Database Applications','Creating Database Web Applications with PHP and ASP'),0.5490196078431373)
        self.assertEqual(smart_match.dissimilarity('Web Database Applications','Building Database Applications on the Web Using PHP3'),0.5769230769230769)
        self.assertEqual(smart_match.dissimilarity('Web Database Applications','Building Web Database Applications with Visual Studio 6'),0.5454545454545454)
        self.assertEqual(smart_match.dissimilarity('Web Database Applications','Web Application Development With PHP'),0.75)
        self.assertEqual(smart_match.dissimilarity('Web Database Applications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),0.7126436781609196)
        self.assertEqual(smart_match.dissimilarity('Web Database Applications','Structural Assessment: The Role of Large and Full-Scale Testing'),0.8412698412698413)
        self.assertEqual(smart_match.dissimilarity('Web Database Applications','How to Find a Scholarship Online'),0.84375)
        self.assertEqual(smart_match.dissimilarity('Web Aplications','Web Database Applications with PHP & MySQL'),0.6428571428571429)
        self.assertEqual(smart_match.dissimilarity('Web Aplications','Creating Database Web Applications with PHP and ASP'),0.7058823529411765)
        self.assertEqual(smart_match.dissimilarity('Web Aplications','Building Database Applications on the Web Using PHP3'),0.75)
        self.assertEqual(smart_match.dissimilarity('Web Aplications','Building Web Database Applications with Visual Studio 6'),0.7272727272727273)
        self.assertEqual(smart_match.dissimilarity('Web Aplications','Web Application Development With PHP'),0.6111111111111112)
        self.assertEqual(smart_match.dissimilarity('Web Aplications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),0.8275862068965517)
        self.assertEqual(smart_match.dissimilarity('Web Aplications','Structural Assessment: The Role of Large and Full-Scale Testing'),0.8888888888888888)
        self.assertEqual(smart_match.dissimilarity('Web Aplications','How to Find a Scholarship Online'),0.8125)


    def test_distance(self):
        self.assertEqual(smart_match.distance('hello', 'hero'), 2)
        self.assertEqual(smart_match.distance('Subsitute', 'Subsytute'), 1)
        self.assertEqual(smart_match.distance('Subsitute', 'Sybsytyte'), 3)
        self.assertEqual(smart_match.distance('abc', 'abcdef'), 3)
        self.assertEqual(smart_match.distance('def', 'abcdef'), 3)
        self.assertEqual(smart_match.distance('hello', 'ehllo'), 2)
        self.assertEqual(smart_match.distance('test string1','test string2'),1)
        self.assertEqual(smart_match.distance('test','test string2'),8)
        self.assertEqual(smart_match.distance('','test string2'),12)
        self.assertEqual(smart_match.distance('aaa bbb ccc ddd','aaa bbb ccc eee'),3)
        self.assertEqual(smart_match.distance('aaa bbb','aaa aaa'),3)
        self.assertEqual(smart_match.distance('aaa','aaa aaa'),4)
        self.assertEqual(smart_match.distance('a b c d','a b c e'),1)
        self.assertEqual(smart_match.distance('Healed','Sealed'),1)
        self.assertEqual(smart_match.distance('Healed','Healthy'),3)
        self.assertEqual(smart_match.distance('Healed','Heard'),2)
        self.assertEqual(smart_match.distance('Healed','Herded'),2)
        self.assertEqual(smart_match.distance('Healed','Help'),3)
        self.assertEqual(smart_match.distance('Healed','Sold'),4)
        self.assertEqual(smart_match.distance('Healed','Help'),3)
        self.assertEqual(smart_match.distance('Sam J Chapman','Samuel John Chapman'),6)
        self.assertEqual(smart_match.distance('Sam Chapman','S Chapman'),2)
        self.assertEqual(smart_match.distance('John Smith','Samuel John Chapman'),14)
        self.assertEqual(smart_match.distance('John Smith','Sam Chapman'),11)
        self.assertEqual(smart_match.distance('John Smith','Sam J Chapman'),12)
        self.assertEqual(smart_match.distance('John Smith','S Chapman'),9)
        self.assertEqual(smart_match.distance('Web Database Applications','Web Database Applications with PHP & MySQL'),17)
        self.assertEqual(smart_match.distance('Web Database Applications','Creating Database Web Applications with PHP and ASP'),28)
        self.assertEqual(smart_match.distance('Web Database Applications','Building Database Applications on the Web Using PHP3'),30)
        self.assertEqual(smart_match.distance('Web Database Applications','Building Web Database Applications with Visual Studio 6'),30)
        self.assertEqual(smart_match.distance('Web Database Applications','Web Application Development With PHP'),27)
        self.assertEqual(smart_match.distance('Web Database Applications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),62)
        self.assertEqual(smart_match.distance('Web Database Applications','Structural Assessment: The Role of Large and Full-Scale Testing'),53)
        self.assertEqual(smart_match.distance('Web Database Applications','How to Find a Scholarship Online'),27)
        self.assertEqual(smart_match.distance('Web Aplications','Web Database Applications with PHP & MySQL'),27)
        self.assertEqual(smart_match.distance('Web Aplications','Creating Database Web Applications with PHP and ASP'),36)
        self.assertEqual(smart_match.distance('Web Aplications','Building Database Applications on the Web Using PHP3'),39)
        self.assertEqual(smart_match.distance('Web Aplications','Building Web Database Applications with Visual Studio 6'),40)
        self.assertEqual(smart_match.distance('Web Aplications','Web Application Development With PHP'),22)
        self.assertEqual(smart_match.distance('Web Aplications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),72)
        self.assertEqual(smart_match.distance('Web Aplications','Structural Assessment: The Role of Large and Full-Scale Testing'),56)
        self.assertEqual(smart_match.distance('Web Aplications','How to Find a Scholarship Online'),26)


if __name__ == '__main__':
    unittest.main()
