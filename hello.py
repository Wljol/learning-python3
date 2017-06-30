def hello(greeting,*args):
    if len(args)==0:
        print('%s!'% greeting)
    else:
        print('%s, %s!'%(greeting,','.join(args)))
