def celcius_to_fahrenheit():
    while True:
        try:
            print('Welcome. Celcius to Fahrenheit or Fahrenheit to Celcius?')
            
            ans = input('1 for c to f and 2 for f to c\n')
            if ans != '1' and ans != '2':
                raise ValueError('you must enter 1 or 2 pls try again')
            
                            
            
            if ans == '1':
                 
                    cel = float(input('please enter a value: '))
                    fah = cel * 1.8+32
                    return f'your fahrenheit value is {round(fah,2)} *F'
                
            if ans == '2':
                fah = float(input('please enter a value: '))
                cel = (fah-32)/1.8
                return f'your celcius value is {round(cel,2)} *C'
        except ValueError as err:
            print(err)

a = celcius_to_fahrenheit()
print(a)
