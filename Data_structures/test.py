def test_numbers():
    x = input("Enter numbers to know if odd or even seperated by commas eg (1,2,3):")
    number = [int(i) for i in x.split(",")]
    odd_numbers = []
    even_numbers = []
    for u in number:
        if u % 2 == 1:
           odd_numbers.append(u)
        else:
             even_numbers.append(u)
        """
        The code is simply testing if the user inputed numbers are even or odd.
        Lets break it down as google maps directs Genz in the busy kanairo town.
        >The user is asked to input the numbers with the input request.
        >Then a variable number is created with inbuilt function .split() to be able 
        ... seprate the numbers entered by the users are separeted by a comma
        >Then there are control flow syntaxs 
        >Print outs
        """
    print(f"This are your odd numbers:{odd_numbers}")
    print(f"This are your odd numbers:{even_numbers}")
test_numbers()
test_numbers.__doc__



    