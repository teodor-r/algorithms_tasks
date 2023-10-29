
def func( *args, **kargs):
    print(list(args))
    print(kargs)


func(1,23,4, name = "na,e")