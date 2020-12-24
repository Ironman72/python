text = 'This is a global varaible'

def testing_vars():
    x = 'This is a local variable'
    print('Local variable: ' + x)

testing_vars()
print('global: ' + text)