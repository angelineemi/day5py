def fn():
    a=5
    b=0
    try:
        c=a/b
        print(c)
    except(ZeroDivisionError):
        print(" Division by zero is not possible")
fn()
        
