'''
CISC106 Module that includes some basic helper functions such as assertEqual().

Versions:
0.152 - 2015-NOV-19, Modified by Jon Leighton
 + Corrected typo - args spelled as agrs when checking for invalid precision
   argument.
0.151 - 2015-AUG-29, Modified by Jon Leighton
 + Modified names of __isEqual() and __isseqtype() to _isEqual() and _isseqtype().
 + Edited documentation for assertEqual() function for clarity.
0.15 - 2015-MAY-01, Modified by Jon Leighton
 + Comparison now based on significant figures rather than on a fixed number of
   decimal places. Default precision is 15 significant figures.
0.142 - 2014-APR-23, Modified by Jon Leighton
 + Modified success and failure messages to print "SUCCESS" and "FAILURE" at the
   beginning of each result. This makes it much easier to quickly discern the
   outcome visually.
0.141 - 2014-MAR-26, Modified by Jon Leighton
 + Removed unused function print_verbose().
 + Appended text to FAILURE message for incompatible types to indicate that types
   involved can't be compared.
0.14 - 2014-MAR-26, Modified by Andrew Roosen
 + Modified assertEqual() to return False on failure and True on success.
 + Introduced QUITE option to supress output on SUCCESS.
 + Modified FAILURE message for incompatible data types to be consistent with
 + FAILURE message for unequal values.
0.13 - 2014-MAR-25, Modified by Jon Leighton
 + added elif clause to __isEqual(), to avoid comparing ints and floats to anything
   that is not an int or a float, and to return None in this case. The previous
   comparison tried to subtract these quantities from each other, causing a
   runtime error.
 + Modified assertEqual() to check for __isEqual() returning None, which now
   indicates an attempt to compare unrelated data types. Failure message is
   modified in this case to report the attempt to compare unrelated types.
 + Removed unused global variables fail and success.
 + Added version numbers to Paul Amer's modifications, and bumped version number to
   reflect my modifications.
 + Changed version number to string, to match recommended practice.
 + Modified names of internal functions isEqual() and isseqtype() to __isEqual()
   and __isseqtype(), respectively
0.122 - 2012-APR-17, Modified by Paul Amer
 + removed graphics stuff; just kept AssertEqual
0.121 - 2011-SEP-08, Modified by Paul Amer
 +improved success-failure messages
0.12
 + display can be called multiple times
 + assertEqual supports PIL.Image.Image
0.1
 + Initial assertEqual, display, animate, bind
'''
__version__ = '0.151'

import sys, traceback, types, os

# Don't print message from assertEqual on success
QUIET=False

def assertEqual(x, y, *args):
    '''
    Test for equality of x and y
    Prints a SUCCESS msg if x and y are equal, otherwise a FAILURE msg.
    If x and y are numeric, they are tested for equality to 15 significant
    figures by default. Optional 3rd argument can be used to specify a different
    number of significant figures. Optional argument ignored for non-numeric
    values. If no comparison relationship exists between x and y, the FAILURE
    message states that the values are unrelated.
    Parameters:
        x, y (any type)
        args (int) - number of digits of precicion to use when x and y are
                     numeric.
    Outputs:
        Message indication success or failure
    Returns:
        None
    '''
    
    trace = traceback.extract_stack()
    frame = trace[len(trace)-2]

    result = _isEqual(x, y, *args)
    if result == None:
        print('FAILURE - [line', frame[1], '] ', frame[3], ', predicted answer was ',
              y, ' ', type(y), ', computed answer was ', x, ' ', type(x),
              ' (Attempting to compare unrelated data types.)', sep = '')
        return False
    elif not result:
        print("FAILURE - [line %d] %s, predicted answer was %s, computed answer was %s " \
            % (frame[1], frame[3], y, x))
        return False
    elif not QUIET:
        print("SUCCESS - [line %d] %s" % (frame[1], frame[3]))
    return True

def _isEqual(x, y, *args):
    """
    _isEqual : thing thing -> boolean
    _isEqual : number number number -> boolean
    Determines whether the two arguments are equal, or in the case of
    floating point numbers, within a specified number of decimal points
    precision (by default, checks to with 4 decimal points for floating
    point numbers). Returns None when attempting to compare ints and floats
    to anything other than ints and floats.
    
    Examples:
    >>> _isEqual('ab', 'a'+'b')
     True
     
    >>> _isEqual(12.34, 12.35)
     False
     
    >>> _isEqual(12.3456, 12.34568, 4)
     True
         
    >>> _isEqual(12.3456, 12.34568w5)
     False
    """
    if (x is None and y is not None) or (y is None and x is not None):
        return False
    elif x is None and y is None:
        return True
    elif (type(x) == int or type(x) == float) and \
             (type(y) != int and type(y) != float) or \
         (type(y) == int or type(y) == float) and \
             (type(x) != int and type(x) != float):
        return None
    elif type(x) == int and type(y) == int:
        return x == y
    elif type(x) == float or type(y) == float:
        # set default precision to 15 significant figures.
        exp = 15
        if len(args) == 1:
            if type(args[0]) != int and type(args[0]) != float:
                print('Invalid precision: must be non-negative and numeric.',
                      'Using default precision of 15 significant figures.')
            else:
                exp = args[0]
        if y != 0:
            return abs(y - x) < abs(y) * 10 ** (-exp)
        else:
            return abs(x) < 10 ** (-exp)
    elif _isseqtype(x) and _isseqtype(y) and len(x)==len(y):
        res = True
        for (x1,y1) in zip(x, y):
            res = res and _isEqual(x1, y1, *args)
        return res
    else:
        return x == y

def _isseqtype(x):
    return type(x) == list or type(x) == tuple
