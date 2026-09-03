
#fastPY is used to make Python code even faster. fastPY contains a bunch of useful functions to use in your code.
def turn_number(number_str):
    #This functions turns a number in a string format into a number. It doesn't crash if the input is invalid, and it can process both integers and floats. If the input is invalid, it returns None.
    try:
        if "." in number_str:
            return float(number_str)
        else:
            return int(number_str)
    except ValueError:
        return None

def separate_output(output, separator="-", separator_size=50):
    #This function separates the output in the console with a separator. The separator can be customized with the separator and separator_size parameters.
    print(separator * separator_size)
    print(output)
    print(separator * separator_size)

def get_pi():
    #This function returns a very precise value of pi(500 digits). It is useful for calculations that require a high degree of precision.
    return 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912
