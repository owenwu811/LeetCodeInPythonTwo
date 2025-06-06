
#1114
#easy

#Suppose we have a class:

#public class Foo {
#  public void first() { print("first"); }
#  public void second() { print("second"); }
#  public void third() { print("third"); }
#}
#The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

#Note:

#We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.

 

#Example 1:

#Input: nums = [1,2,3]
#Output: "firstsecondthird"
#Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
#Example 2:

#Input: nums = [1,3,2]
#Output: "firstsecondthird"
#Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.




#correct python3 solution (could not solve):

#make sure no deadlocks 

class Foo:
    def __init__(self):
        self.a = threading.Lock()
        self.b = threading.Lock()
        self.a.acquire()
        self.b.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.a.release()

      
    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.a.acquire()
        printSecond()
        self.b.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.b.acquire()
        printThird()
        #self.b.release()



#2/16/25 review:

class Foo:
    def __init__(self):
        self.a = threading.Lock()
        self.b = threading.Lock()
        self.a.acquire()
        self.b.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.a.release()
 

    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.a.acquire()
        printSecond()
        self.b.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.b.acquire()
        printThird()

