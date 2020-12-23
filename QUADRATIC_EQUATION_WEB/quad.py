
#def search4vowels(phrase: str) -> set:
#    """Return any vowels found in a supplied phrase."""
#   vowels = set('aeiou')
#    return vowels.intersection(set(phrase))


#def search4letters(phrase: str, letters: str='aeiou') -> set:
#    """Return a set of the 'letters' found in 'phrase'."""
#    return set(letters).intersection(set(phrase))


def quadratic_equation1(a,b,c):
    x1 = (-b+(b**2 - 4*a*c)**0.5)/(2*a)

#    print("The roots are", x1, "and" , x2)
    return(x1)

def quadratic_equation2(a,b,c):

    x2 = (-b-(b**2 - 4*a*c)**0.5)/(2*a)
#    print("The roots are", x1, "and" , x2)
    return(x2)

#print("We are going to determine the roots of a quadratic equation based on the input given by you.")    
#a=int(input("Please insert the coefficient of x**2: "))
#b=int(input("Please insert the coefficient of x: "))  
#c=int(input("Please insert the coefficient of x**0: "))      
#quadratic_equation(a,b,c)  
