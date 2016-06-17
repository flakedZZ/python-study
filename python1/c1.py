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

if __name__ == '__main__':
    # print 'hello world'
    demo_controlflow()
    # demo_string()
