import random

def demo_string():
    stra = "hello neko"
    print 1, stra.upper()
    print 2, range(1, 20, 3)
    print 3, eval("3+3")
    print 4, chr(97 - 32), ord("a")
    print 5, divmod(11, 3)


def demo_controlflow():
    score = 65
    if score > 99:
        print 'A'
    elif score > 60:
        print 'B'
    else:
        print 'C'

    while score < 100:
        print score
        score += 10

    for i in range(0,20,1):
        print i

def demo_list():
    lista=[1,2,3,45,5]
    listb=['a','b','c',4]
    print lista
    print listb
    for i in listb:
        print i


def demo_dirt():
    dirta={1:1,2:4,3:9}
    print dirta.items()
    print dirta

def demo_set():
    setA=set([1,2,3,4,5])
    print setA

def demo_random():
    print random.random()
if __name__ == '__main__':
    # print 'hello world'
    #demo_controlflow()
    # demo_string()
    #demo_list()
    #emo_dirt()
    #demo_set()
    demo_random()