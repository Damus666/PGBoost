from noinit import _NoInit
import math
from typing import SupportsIndex

class Math(_NoInit):
    """Groups python 'math' and 'builtins' module math related functions with some additional ones"""
    
    PI = math.pi
    E = math.e
    NaN = math.nan
    Infinity = math.inf
    NegativeInfinity = -math.inf
    
    Cos = math.cos
    Sin = math.sin
    Tan = math.tan
    ACos = math.acos
    ASin = math.asin
    ATan = math.atan
    ATan2 = math.atan2
    ACosH = math.acosh
    ASinH = math.asinh
    ATanH = math.atanh
    
    Degrees = math.degrees
    Radians = math.radians
    
    Log = math.log
    Log2 = math.log2
    Log1P = math.log1p
    Log10 = math.log10
    
    Pow = math.pow
    Sqrt = math.sqrt
    Sign = math.copysign
    Factorial = math.factorial
    Dist = math.dist
    
    Floor = math.floor
    Ceil = math.ceil
    
    Fabs = math.fabs
    FMod = math.fmod
    FSum = math.fsum
    Hypot = math.hypot
    Frexp = math.frexp
    Erf = math.erf
    Erfc = math.erfc
    Comb = math.comb
    ExpM1 = math.expm1
    
    IsNan = math.isnan
    IsInf = math.isinf
    IsFinite = math.isfinite
    
    Sum = sum
    Min = min
    Max = max
    ToInt = int
    ToFloat = float
    ToComplex = complex
    Eval = eval
    Round = round
    
    @staticmethod
    def InsideRange(number:float|int,rangeStart:float|int,rangeEnd:float|int)->bool:
        """Returns wether a number is inside a range. Start and end points are NOT included"""
        return number > min(rangeStart,rangeEnd) and number < max(rangeStart,rangeEnd)
    
    @staticmethod
    def InsideEqualRange(number:float|int,rangeStart:float|int,rangeEnd:float|int)->bool:
        """Returns wether a number is inside a range. Start and end points are included"""
        return number >= min(rangeStart,rangeEnd) and number <= max(rangeStart,rangeEnd)
    
    @staticmethod
    def Det(a:SupportsIndex,b:SupportsIndex)->float:
        """
        Return det of vector2 a and vector2 b
        """
        return a[0]*b[1]-a[1]*b[0]

    def TupleSlope(tuplee:tuple[tuple[float,float],tuple[float,float]])->float:
        """
        Find the slope of a line that is made of tuples.
        """
        if (tuplee[1][0]-tuplee[0][0]) == 0:
            return None
        return (tuplee[1][1]-tuplee[0][1])/(tuplee[1][0]-tuplee[0][0])