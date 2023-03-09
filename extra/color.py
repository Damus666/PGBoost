import random
from noinit import _NoInit

class ColorRGB(_NoInit):
    """Contains color attributes as RGB and some methods related to them. 'ColorRGB.colors' contains the same attributes inside a dictionary"""
    
    colors = {"maroon":(128,0,0),
            "dark red":(139,0,0),
            "brown":(165,42,42),
            "firebrick":(178,34,34),
            "crimson":(220,20,60),
            "red":(255,0,0),
            "tomato":(255,99,71),
            "coral":(255,127,80),
            "indian red":(205,92,92),
            "light coral":(240,128,128),
            "dark salmon":(233,150,122),
            "salmon":(250,128,114),
            "light salmon":(255,160,122),
            "orange red":(255,69,0),
            "dark orange":(255,140,0),
            "orange":(255,165,0),
            "gold":(255,215,0),
            "dark golden rod":(184,134,11),
            "golden rod":(218,165,32),
            "pale golden rod":(238,232,170),
            "dark khaki":(189,183,107),
            "khaki":(240,230,140),
            "olive":(128,128,0),
            "yellow":(255,255,0),
            "yellow green":(154,205,50),
            "dark olive green":(85,107,47),
            "olive drab":(107,142,35),
            "lawn green":(124,252,0),
            "chartreuse":(127,255,0),
            "green yellow":(173,255,47),
            "dark green":(0,100,0),
            "green":(0,128,0),
            "forest green":(34,139,34),
            "lime":(0,255,0),
            "lime green":(50,205,50),
            "light green":(144,238,144),
            "pale green":(152,251,152),
            "dark sea green":(143,188,143),
            "medium spring green":(0,250,154),
            "spring green":(0,255,127),
            "sea green":(46,139,87),
            "medium aqua marine":(102,205,170),
            "medium sea green":(60,179,113),
            "light sea green":(32,178,170),
            "dark slate gray":(47,79,79),
            "teal":(0,128,128),
            "dark cyan":(0,139,139),
            "aqua":(0,255,255),
            "cyan":(0,255,255),
            "light cyan":(224,255,255),
            "dark turquoise":(0,206,209),
            "turquoise":(64,224,208),
            "medium turquoise":(72,209,204),
            "pale turquoise":(175,238,238),
            "aqua marine":(127,255,212),
            "powder blue":(176,224,230),
            "cadet blue":(95,158,160),
            "steel blue":(70,130,180),
            "corn flower blue":(100,149,237),
            "deep sky blue":(0,191,255),
            "dodger blue":(30,144,255),
            "light blue":(173,216,230),
            "sky blue":(135,206,235),
            "light sky blue":(135,206,250),
            "midnight blue":(25,25,112),
            "navy":(0,0,128),
            "dark blue":(0,0,139),
            "medium blue":(0,0,205),
            "blue":(0,0,255),
            "royal blue":(65,105,225),
            "blue violet":(138,43,226),
            "indigo":(75,0,130),
            "dark slate blue":(72,61,139),
            "slate blue":(106,90,205),
            "medium slate blue":(123,104,238),
            "medium purple":(147,112,219),
            "dark magenta":(139,0,139),
            "dark violet":(148,0,211),
            "dark orchid":(153,50,204),
            "medium orchid":(186,85,211),
            "purple":(128,0,128),
            "thistle":(216,191,216),
            "plum":(221,160,221),
            "violet":(238,130,238),
            "magenta / fuchsia":(255,0,255),
            "orchid":(218,112,214),
            "medium violet red":(199,21,133),
            "pale violet red":(219,112,147),
            "deep pink":(255,20,147),
            "hot pink":(255,105,180),
            "light pink":(255,182,193),
            "pink":(255,192,203),
            "antique white":(250,235,215),
            "beige":(245,245,220),
            "bisque":(255,228,196),
            "blanched almond":(255,235,205),
            "wheat":(245,222,179),
            "corn silk":(255,248,220),
            "lemon chiffon":(255,250,205),
            "light golden rod yellow":(250,250,210),
            "light yellow":(255,255,224),
            "saddle brown":(139,69,19),
            "sienna":(160,82,45),
            "chocolate":(210,105,30),
            "peru":(205,133,63),
            "sandy brown":(244,164,96),
            "burly wood":(222,184,135),
            "tan":(210,180,140),
            "rosy brown":(188,143,143),
            "moccasin":(255,228,181),
            "navajo white":(255,222,173),
            "peach puff":(255,218,185),
            "misty rose":(255,228,225),
            "lavender blush":(255,240,245),
            "linen":(250,240,230),
            "old lace":(253,245,230),
            "papaya whip":(255,239,213),
            "sea shell":(255,245,238),
            "mint cream":(245,255,250),
            "slate gray":(112,128,144),
            "light slate gray":(119,136,153),
            "light steel blue":(176,196,222),
            "lavender":(230,230,250),
            "floral white":(255,250,240),
            "alice blue":(240,248,255),
            "ghost white":(248,248,255),
            "honeydew":(240,255,240),
            "ivory":(255,255,240),
            "azure":(240,255,255),
            "snow":(255,250,250),
            "black":(0,0,0),
            "dim gray":(105,105,105),
            "dim grey":(105,105,105),
            "grey":(128,128,128),
            "gray":(128,128,128),
            "dark gray":(169,169,169),
            "dark grey":(169,169,169),
            "silver":(192,192,192),
            "light gray":(211,211,211),
            "light grey":(211,211,211),
            "gainsboro":(220,220,220),
            "white smoke":(245,245,245),
            "white":(255,255,255),
            }
    Maroon = (128,0,0)
    DarkRed = (139,0,0)
    Brown = (165,42,42)
    Firebrick = (178,34,34)
    Crimson = (220,20,60)
    Red = (255,0,0)
    Tomato = (255,99,71)
    Coral = (255,127,80)
    IndianRed = (205,92,92)
    LightCoral = (240,128,128)
    DarkSalmon = (233,150,122)
    Salmon = (250,128,114)
    LightSalmon = (255,160,122)
    OrangeRed = (255,69,0)
    DarkOrange = (255,140,0)
    Orange = (255,165,0)
    Gold = (255,215,0)
    DarkGoldenRod = (184,134,11)
    GoldenRod = (218,165,32)
    PaleGoldenRod = (238,232,170)
    DarkKhaki = (189,183,107)
    Khaki = (240,230,140)
    Olive = (128,128,0)
    Yellow = (255,255,0)
    YellowGreen = (154,205,50)
    DarkOliveGreen = (85,107,47)
    OliveDrab = (107,142,35)
    LawnGreen = (124,252,0)
    Chartreuse = (127,255,0)
    GreenYellow = (173,255,47)
    DarkGreen = (0,100,0)
    Green = (0,128,0)
    ForestGreen = (34,139,34)
    Lime = (0,255,0)
    LimeGreen = (50,205,50)
    LightGreen = (144,238,144)
    PaleGreen = (152,251,152)
    DarkSeaGreen = (143,188,143)
    MediumSpringGreen = (0,250,154)
    SpringGreen = (0,255,127)
    SeaGreen = (46,139,87)
    MediumAquaMarine = (102,205,170)
    MediumSeaGreen = (60,179,113)
    LightSeaGreen = (32,178,170)
    DarkSlateGray = (47,79,79)
    Teal = (0,128,128)
    DarkCyan = (0,139,139)
    Aqua = (0,255,255)
    Cyan = (0,255,255)
    LightCyan = (224,255,255)
    DarkTurquoise = (0,206,209)
    Turquoise = (64,224,208)
    MediumTurquoise = (72,209,204)
    PaleTurquoise = (175,238,238)
    AquaMarine = (127,255,212)
    PowderBlue = (176,224,230)
    CadetBlue = (95,158,160)
    SteelBlue = (70,130,180)
    CornFlowerBlue = (100,149,237)
    DeepSkyBlue = (0,191,255)
    DodgerBlue = (30,144,255)
    LightBlue = (173,216,230)
    SkyBlue = (135,206,235)
    LightSkyBlue = (135,206,250)
    MidnightBlue = (25,25,112)
    Navy = (0,0,128)
    DarkBlue = (0,0,139)
    MediumBlue = (0,0,205)
    Blue = (0,0,255)
    RoyalBlue = (65,105,225)
    BlueViolet = (138,43,226)
    Indigo = (75,0,130)
    DarkSlateBlue = (72,61,139)
    SlateBlue = (106,90,205)
    MediumSlateBlue = (123,104,238)
    MediumPurple = (147,112,219)
    DarkMagenta = (139,0,139)
    DarkViolet = (148,0,211)
    DarkOrchid = (153,50,204)
    MediumOrchid = (186,85,211)
    Purple = (128,0,128)
    Thistle = (216,191,216)
    Plum = (221,160,221)
    Violet = (238,130,238)
    Magenta = (255,0,255)
    Fuchsia = (255,0,255)
    Orchid = (218,112,214)
    MediumVioletRed = (199,21,133)
    PaleVioletRed = (219,112,147)
    DeepPink = (255,20,147)
    HotPink = (255,105,180)
    LightPink = (255,182,193)
    Pink = (255,192,203)
    AntiqueWhite = (250,235,215)
    Beige = (245,245,220)
    Bisque = (255,228,196)
    BlanchedAlmond = (255,235,205)
    Wheat = (245,222,179)
    CornSilk = (255,248,220)
    LemonChiffon = (255,250,205)
    LightGoldenRodYellow = (250,250,210)
    LightYellow = (255,255,224)
    SaddleBrown = (139,69,19)
    Sienna = (160,82,45)
    Chocolate = (210,105,30)
    Peru = (205,133,63)
    SandyBrown = (244,164,96)
    BurlyWood = (222,184,135)
    Tan = (210,180,140)
    RosyBrown = (188,143,143)
    Moccasin = (255,228,181)
    NavajoWhite = (255,222,173)
    PeachPuff = (255,218,185)
    MistyRose = (255,228,225)
    LavenderBlush = (255,240,245)
    Linen = (250,240,230)
    OldLace = (253,245,230)
    PapayaWhip = (255,239,213)
    SeaShell = (255,245,238)
    MintCream = (245,255,250)
    SlateGray = (112,128,144)
    LightSlateGray = (119,136,153)
    LightSteelBlue = (176,196,222)
    Lavender = (230,230,250)
    FloralWhite = (255,250,240)
    AliceBlue = (240,248,255)
    GhostWhite = (248,248,255)
    Honeydew = (240,255,240)
    Ivory = (255,255,240)
    Azure = (240,255,255)
    Snow = (255,250,250)
    Black = (0,0,0)
    DimGray = (105,105,105)
    DimGrey = (105,105,105)
    Grey = (128,128,128)
    Gray = (128,128,128)
    DarkGray = (169,169,169)
    DarkGrey = (169,169,169)
    Silver = (192,192,192)
    LightGray = (211,211,211)
    LightGrey = (211,211,211)
    Gainsboro = (220,220,220)
    WhiteSmoke = (245,245,245)
    White = (255,255,255)
    
    @classmethod
    def Random(cls):
        """Return a random color from the available ones"""
        return random.choice(cls.colors.values())
    
    @classmethod
    def RandomName(cls):
        """Return a random color name"""
        return random.choice(cls.colors.keys())
    
    @classmethod
    def Names(cls):
        """Return the available color names"""
        return list(cls.colors.keys())
    
    @staticmethod
    def RandomRGB():
        """Return a random RGB color of the range 0-255"""
        return (
            random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255)
        )
        
    @staticmethod
    def ToRange01(range0255color:tuple[int,int,int]):
        """Returns the same color constrained in a range 0-1"""
        return (
            range0255color[0]/255,
            range0255color[1]/255,
            range0255color[2]/255
        )
        
    @staticmethod
    def ToRange0255(range01color:tuple[float,float,float]):
        """Returns the same color in a range 0-255"""
        return (
            int(range01color[0]*255),
            int(range01color[1]*255),
            int(range01color[2]*255)
        )
    
    @staticmethod
    def ToHEX(RGBColor):
        """Converts a RGB color to a HEX one"""
        return '%02x%02x%02x' % RGBColor

class ColorHEX:
    """Contains color attributes as HEX and some methods related to them. 'ColorHEX.colors' contains the same attributes inside a dictionary"""
    colors = {
        "maroon":"#800000",
        "dark red":"#8B0000",
        "brown":"#A52A2A",
        "firebrick":"#B22222",
        "crimson":"#DC143C",
        "red":"#FF0000",
        "tomato":"#FF6347",
        "coral":"#FF7F50",
        "indian red":"#CD5C5C",
        "light coral":"#F08080",
        "dark salmon":"#E9967A",
        "salmon":"#FA8072",
        "light salmon":"#FFA07A",
        "orange red":"#FF4500",
        "dark orange":"#FF8C00",
        "orange":"#FFA500",
        "gold":"#FFD700",
        "dark golden rod":"#B8860B",
        "golden rod":"#DAA520",
        "pale golden rod":"#EEE8AA",
        "dark khaki":"#BDB76B",
        "khaki":"#F0E68C",
        "olive":"#808000",
        "yellow":"#FFFF00",
        "yellow green":"#9ACD32",
        "dark olive green":"#556B2F",
        "olive drab":"#6B8E23",
        "lawn green":"#7CFC00",
        "chartreuse":"#7FFF00",
        "green yellow":"#ADFF2F",
        "dark green":"#006400",
        "green":"#008000",
        "forest green":"#228B22",
        "lime":"#00FF00",
        "lime green":"#32CD32",
        "light green":"#90EE90",
        "pale green":"#98FB98",
        "dark sea green":"#8FBC8F",
        "medium spring green":"#00FA9A",
        "spring green":"#00FF7F",
        "sea green":"#2E8B57",
        "medium aqua marine":"#66CDAA",
        "medium sea green":"#3CB371",
        "light sea green":"#20B2AA",
        "dark slate gray":"#2F4F4F",
        "teal":"#008080",
        "dark cyan":"#008B8B",
        "aqua":"#00FFFF",
        "cyan":"#00FFFF",
        "light cyan":"#E0FFFF",
        "dark turquoise":"#00CED1",
        "turquoise":"#40E0D0",
        "medium turquoise":"#48D1CC",
        "pale turquoise":"#AFEEEE",
        "aqua marine":"#7FFFD4",
        "powder blue":"#B0E0E6",
        "cadet blue":"#5F9EA0",
        "steel blue":"#4682B4",
        "corn flower blue":"#6495ED",
        "deep sky blue":"#00BFFF",
        "dodger blue":"#1E90FF",
        "light blue":"#ADD8E6",
        "sky blue":"#87CEEB",
        "light sky blue":"#87CEFA",
        "midnight blue":"#191970",
        "navy":"#000080",
        "dark blue":"#00008B",
        "medium blue":"#0000CD",
        "blue":"#0000FF",
        "royal blue":"#4169E1",
        "blue violet":"#8A2BE2",
        "indigo":"#4B0082",
        "dark slate blue":"#483D8B",
        "slate blue":"#6A5ACD",
        "medium slate blue":"#7B68EE",
        "medium purple":"#9370DB",
        "dark magenta":"#8B008B",
        "dark violet":"#9400D3",
        "dark orchid":"#9932CC",
        "medium orchid":"#BA55D3",
        "purple":"#800080",
        "thistle":"#D8BFD8",
        "plum":"#DDA0DD",
        "violet":"#EE82EE",
        "magenta / fuchsia":"#FF00FF",
        "orchid":"#DA70D6",
        "medium violet red":"#C71585",
        "pale violet red":"#DB7093",
        "deep pink":"#FF1493",
        "hot pink":"#FF69B4",
        "light pink":"#FFB6C1",
        "pink":"#FFC0CB",
        "antique white":"#FAEBD7",
        "beige":"#F5F5DC",
        "bisque":"#FFE4C4",
        "blanched almond":"#FFEBCD",
        "wheat":"#F5DEB3",
        "corn silk":"#FFF8DC",
        "lemon chiffon":"#FFFACD",
        "light golden rod yellow":"#FAFAD2",
        "light yellow":"#FFFFE0",
        "saddle brown":"#8B4513",
        "sienna":"#A0522D",
        "chocolate":"#D2691E",
        "peru":"#CD853F",
        "sandy brown":"#F4A460",
        "burly wood":"#DEB887",
        "tan":"#D2B48C",
        "rosy brown":"#BC8F8F",
        "moccasin":"#FFE4B5",
        "navajo white":"#FFDEAD",
        "peach puff":"#FFDAB9",
        "misty rose":"#FFE4E1",
        "lavender blush":"#FFF0F5",
        "linen":"#FAF0E6",
        "old lace":"#FDF5E6",
        "papaya whip":"#FFEFD5",
        "sea shell":"#FFF5EE",
        "mint cream":"#F5FFFA",
        "slate gray":"#708090",
        "light slate gray":"#778899",
        "light steel blue":"#B0C4DE",
        "lavender":"#E6E6FA",
        "floral white":"#FFFAF0",
        "alice blue":"#F0F8FF",
        "ghost white":"#F8F8FF",
        "honeydew":"#F0FFF0",
        "ivory":"#FFFFF0",
        "azure":"#F0FFFF",
        "snow":"#FFFAFA",
        "black":"#000000",
        "dim gray":"#696969",
        "dim grey":"#696969",
        "gray":"#808080",
        "grey":"#808080",
        "dark gray":"#A9A9A9",
        "dark grey":"#A9A9A9",
        "silver":"#C0C0C0",
        "light gray":"#D3D3D3",
        "light grey":"#D3D3D3",
        "gainsboro":"#DCDCDC",
        "white smoke":"#F5F5F5",
        "white":"#FFFFFF",
        }
    
    Maroon = "#800000"
    DarkRed = "#8B0000"
    Brown = "#A52A2A"
    Firebrick = "#B22222"
    Crimson = "#DC143C"
    Red = "#FF0000"
    Tomato = "#FF6347"
    Coral = "#FF7F50"
    IndianRed = "#CD5C5C"
    LightCoral = "#F08080"
    DarkSalmon = "#E9967A"
    Salmon = "#FA8072"
    LightSalmon = "#FFA07A"
    OrangeRed = "#FF4500"
    DarkOrange = "#FF8C00"
    Orange = "#FFA500"
    Gold = "#FFD700"
    DarkGoldenRod = "#B8860B"
    GoldenRod = "#DAA520"
    PaleGoldenRod = "#EEE8AA"
    DarkKhaki = "#BDB76B"
    Khaki = "#F0E68C"
    Olive = "#808000"
    Yellow = "#FFFF00"
    YellowGreen = "#9ACD32"
    DarkOliveGreen = "#556B2F"
    OliveDrab = "#6B8E23"
    LawnGreen = "#7CFC00"
    Chartreuse = "#7FFF00"
    GreenYellow = "#ADFF2F"
    DarkGreen = "#006400"
    Green = "#008000"
    ForestGreen = "#228B22"
    Lime = "#00FF00"
    LimeGreen = "#32CD32"
    LightGreen = "#90EE90"
    PaleGreen = "#98FB98"
    DarkSeaGreen = "#8FBC8F"
    MediumSpringGreen = "#00FA9A"
    SpringGreen = "#00FF7F"
    SeaGreen = "#2E8B57"
    MediumAquaMarine = "#66CDAA"
    MediumSeaGreen = "#3CB371"
    LightSeaGreen = "#20B2AA"
    DarkSlateGray = "#2F4F4F"
    Teal = "#008080"
    DarkCyan = "#008B8B"
    Aqua = "#00FFFF"
    Cyan = "#00FFFF"
    LightCyan = "#E0FFFF"
    DarkTurquoise = "#00CED1"
    Turquoise = "#40E0D0"
    MediumTurquoise = "#48D1CC"
    PaleTurquoise = "#AFEEEE"
    AquaMarine = "#7FFFD4"
    PowderBlue = "#B0E0E6"
    CadetBlue = "#5F9EA0"
    SteelBlue = "#4682B4"
    CornFlowerBlue = "#6495ED"
    DeepSkyBlue = "#00BFFF"
    DodgerBlue = "#1E90FF"
    LightBlue = "#ADD8E6"
    SkyBlue = "#87CEEB"
    LightSkyBlue = "#87CEFA"
    MidnightBlue = "#191970"
    Navy = "#000080"
    DarkBlue = "#00008B"
    MediumBlue = "#0000CD"
    Blue = "#0000FF"
    RoyalBlue = "#4169E1"
    BlueViolet = "#8A2BE2"
    Indigo = "#4B0082"
    DarkSlateBlue = "#483D8B"
    SlateBlue = "#6A5ACD"
    MediumSlateBlue = "#7B68EE"
    MediumPurple = "#9370DB"
    DarkMagenta = "#8B008B"
    DarkViolet = "#9400D3"
    DarkOrchid = "#9932CC"
    MediumOrchid = "#BA55D3"
    Purple = "#800080"
    Thistle = "#D8BFD8"
    Plum = "#DDA0DD"
    Violet = "#EE82EE"
    Magenta = "#FF00FF"
    Fuchsia = "#FF00FF"
    Orchid = "#DA70D6"
    MediumVioletRed = "#C71585"
    PaleVioletRed = "#DB7093"
    DeepPink = "#FF1493"
    HotPink = "#FF69B4"
    LightPink = "#FFB6C1"
    Pink = "#FFC0CB"
    AntiqueWhite = "#FAEBD7"
    Beige = "#F5F5DC"
    Bisque = "#FFE4C4"
    BlanchedAlmond = "#FFEBCD"
    Wheat = "#F5DEB3"
    CornSilk = "#FFF8DC"
    LemonChiffon = "#FFFACD"
    LightGoldenRodYellow = "#FAFAD2"
    LightYellow = "#FFFFE0"
    SaddleBrown = "#8B4513"
    Sienna = "#A0522D"
    Chocolate = "#D2691E"
    Peru = "#CD853F"
    SandyBrown = "#F4A460"
    BurlyWood = "#DEB887"
    Tan = "#D2B48C"
    RosyBrown = "#BC8F8F"
    Moccasin = "#FFE4B5"
    NavajoWhite = "#FFDEAD"
    PeachPuff = "#FFDAB9"
    MistyRose = "#FFE4E1"
    LavenderBlush = "#FFF0F5"
    Linen = "#FAF0E6"
    OldLace = "#FDF5E6"
    PapayaWhip = "#FFEFD5"
    SeaShell = "#FFF5EE"
    MintCream = "#F5FFFA"
    SlateGray = "#708090"
    LightSlateGray = "#778899"
    LightSteelBlue = "#B0C4DE"
    Lavender = "#E6E6FA"
    FloralWhite = "#FFFAF0"
    AliceBlue = "#F0F8FF"
    GhostWhite = "#F8F8FF"
    Honeydew = "#F0FFF0"
    Ivory = "#FFFFF0"
    Azure = "#F0FFFF"
    Snow = "#FFFAFA"
    Black = "#000000"
    DimGray = "#696969"
    DimGrey = "#696969"
    Gray = "#808080"
    Grey = "#808080"
    DarkGray = "#A9A9A9"
    DarkGrey = "#A9A9A9"
    Silver = "#C0C0C0"
    LightGray = "#D3D3D3"
    LightGrey = "#D3D3D3"
    Gainsboro = "#DCDCDC"
    WhiteSmoke = "#F5F5F5"
    White = "#FFFFFF"
    
    @classmethod
    def Random(cls):
        """Return a random color from the available ones"""
        return random.choice(cls.colors.values())
    
    @classmethod
    def RandomName(cls):
        """Return a random color name"""
        return random.choice(cls.colors.keys())
    
    @classmethod
    def Names(cls):
        """Return the available color names"""
        return list(cls.colors.keys())
    
    @staticmethod
    def RandomHEX():
        """Returns a random color with the HEX format (the color is from a RGB 0-255 value)"""
        randrgb = ColorRGB.RandomRGB()
        return ColorRGB.ToHEX(randrgb)
    
    @staticmethod
    def ToRGB(HEXColor:str):
        """Convers a HEX color into a RGB one"""
        value = HEXColor.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))