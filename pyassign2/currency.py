#currency exchange
#Wuchenhao
#2018/11/30
"""Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service.It
also provides a set of test functions.
The primary function in this module is exchange."""

def get_to(jstr):
    '''Returns: The TO value in the response to a currency query.
    
    This function returns the currency to convert to and the amount of
    it according to the result from the webpage.
    
    The value returned has type string.
    
    Parameter jstr:the processed string we get from webpage
    Precondition: jstr is a string'''
    
    str_to=jstr.split(',')[1].split(':')[1].replace('"','').strip()
    return str_to

def before_space(str_with_space):
    '''Returns: The amount of the currency.
    
    This function returns the amount of the currency given in parameter
    str_with_space.
    
    The value returned has type string.
    
    Parameter str_with_space:the FROM or TO value from the result from
    webpage
    Precondition: str_with_space is a string for a num and a currency 
    name with a space between them'''
        
    value=str_with_space.split()[0]
    return value

def test_get_to():
    """test the function get_to()"""
    from urllib.request import urlopen

    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5')
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    
    doc_wrong_input = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=XXX&to=XXX&amt=X')
    docstr_wrong_input = doc_wrong_input.read()
    doc_wrong_input.close()
    jstr_wrong_input = docstr_wrong_input.decode('ascii')
    assert('2.1589225 Euros' == get_to(jstr))
    assert('' == get_to(jstr_wrong_input))

def test_before_space():
    """test the function before_space()"""
    test_str = '2.5 United States Dollars'
    assert('2.5' == before_space(test_str))

def test_exchange():
    """test the function exchange()"""
    assert(3.673162 == exchange('USD','AED',1))
    assert('The code of the currency on hand is invalid' == exchange('XXX','AED',1))
    assert('The code of the currency to convert to is invalid.' == exchange('USD','XXX',1))
    assert('The currency amount you input is invalid.' == exchange('USD','AED','X'))

def testAll():
    """test all cases"""
    test_get_to()
    test_before_space()
    test_exchange()
    print("All tests passed")
    
def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    
    url='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' + currency_from + '&to=' + currency_to + '&amt=' + str(amount_from)
    
    from urllib.request import urlopen
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    
    if get_to(jstr) == '':
        error_name=jstr.split(':')[-1].split()[0].replace('"','')
        if error_name=='Source':
            return 'The code of the currency on hand is invalid'
        elif error_name == 'Exchange':
            return 'The code of the currency to convert to is invalid.'
        elif error_name == 'Currency':
            return 'The currency amount you input is invalid.'
    else:
        amount_to = float(before_space(get_to(jstr)))
        return amount_to
if __name__ == '__main__':
    testAll()
