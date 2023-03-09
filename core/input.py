import pygame
from pygame.math import Vector2
from noinit import _NoInit

_pygame_key_codes = [
    pygame.K_BACKSPACE,
    pygame.K_RETURN,
    pygame.K_TAB,
    pygame.K_ESCAPE,
    pygame.K_SPACE,
    pygame.K_COMMA,
    pygame.K_MINUS,
    pygame.K_PERIOD,
    pygame.K_SLASH,
    pygame.K_0,
    pygame.K_1,
    pygame.K_2,
    pygame.K_3,
    pygame.K_4,
    pygame.K_5,
    pygame.K_6,
    pygame.K_7,
    pygame.K_8,
    pygame.K_9,
    pygame.K_SEMICOLON,
    pygame.K_EQUALS,
    pygame.K_LEFTBRACKET,
    pygame.K_RIGHTBRACKET,
    pygame.K_BACKSLASH,
    pygame.K_BACKQUOTE,
    pygame.K_a,
    pygame.K_b,
    pygame.K_c,
    pygame.K_d,
    pygame.K_e,
    pygame.K_f,
    pygame.K_g,
    pygame.K_h,
    pygame.K_i,
    pygame.K_j,
    pygame.K_k,
    pygame.K_l,
    pygame.K_m,
    pygame.K_n,
    pygame.K_o,
    pygame.K_p,
    pygame.K_q,
    pygame.K_r,
    pygame.K_s,
    pygame.K_t,
    pygame.K_u,
    pygame.K_v,
    pygame.K_w,
    pygame.K_x,
    pygame.K_y,
    pygame.K_z,
    pygame.K_DELETE,
    pygame.K_KP0,
    pygame.K_KP1,
    pygame.K_KP2,
    pygame.K_KP3,
    pygame.K_KP4,
    pygame.K_KP5,
    pygame.K_KP6,
    pygame.K_KP7,
    pygame.K_KP8,
    pygame.K_KP9,
    pygame.K_KP_PERIOD,
    pygame.K_KP_DIVIDE,
    pygame.K_KP_MULTIPLY,
    pygame.K_KP_MINUS,
    pygame.K_KP_PLUS,
    pygame.K_KP_ENTER,
    pygame.K_KP_EQUALS,
    pygame.K_UP,
    pygame.K_DOWN,
    pygame.K_RIGHT,
    pygame.K_LEFT,
    pygame.K_INSERT,
    pygame.K_HOME,
    pygame.K_END,
    pygame.K_PAGEUP,
    pygame.K_PAGEDOWN,
    pygame.K_F1,
    pygame.K_F2,
    pygame.K_F3,
    pygame.K_F4,
    pygame.K_F5,
    pygame.K_F6,
    pygame.K_F7,
    pygame.K_F8,
    pygame.K_F9,
    pygame.K_F10,
    pygame.K_F11,
    pygame.K_F12,
    pygame.K_NUMLOCK,
    pygame.K_CAPSLOCK,
    pygame.K_RSHIFT,
    pygame.K_LSHIFT,
    pygame.K_RCTRL,
    pygame.K_LCTRL,
    pygame.K_RALT,
    pygame.K_LALT
]

class KeyCode(_NoInit):
    """Pygame key codes grouped in a class. Regular pygame constants are valid too"""
    Backspace =  pygame.K_BACKSPACE
    Return =  pygame.K_RETURN
    Tab =  pygame.K_TAB
    Escape =  pygame.K_ESCAPE
    Space =  pygame.K_SPACE
    Comma =  pygame.K_COMMA
    Minus =  pygame.K_MINUS
    Period =  pygame.K_PERIOD
    Slash =  pygame.K_SLASH
    Alpha0 =  pygame.K_0
    Alpha1 =  pygame.K_1
    Alpha2 =  pygame.K_2
    Alpha3 =  pygame.K_3
    Alpha4 =  pygame.K_4
    Alpha5 =  pygame.K_5
    Alpha6 =  pygame.K_6
    Alpha7 =  pygame.K_7
    Alpha8 =  pygame.K_8
    Alpha9 =  pygame.K_9
    Semicolon =  pygame.K_SEMICOLON
    Equals =  pygame.K_EQUALS
    Leftbracket =  pygame.K_LEFTBRACKET
    Rightbracket =  pygame.K_RIGHTBRACKET
    Backslash =  pygame.K_BACKSLASH
    Backquote =  pygame.K_BACKQUOTE
    A =  pygame.K_a
    B =  pygame.K_b
    C =  pygame.K_c
    D =  pygame.K_d
    E =  pygame.K_e
    F =  pygame.K_f
    G =  pygame.K_g
    H =  pygame.K_h
    I =  pygame.K_i
    J =  pygame.K_j
    K =  pygame.K_k
    L =  pygame.K_l
    M =  pygame.K_m
    N =  pygame.K_n
    O =  pygame.K_o
    P =  pygame.K_p
    Q =  pygame.K_q
    R =  pygame.K_r
    S =  pygame.K_s
    T =  pygame.K_t
    U =  pygame.K_u
    V =  pygame.K_v
    W =  pygame.K_w
    X =  pygame.K_x
    Y =  pygame.K_y
    Z =  pygame.K_z
    Delete =  pygame.K_DELETE
    KP0 =  pygame.K_KP0
    KP1 =  pygame.K_KP1
    KP2 =  pygame.K_KP2
    KP3 =  pygame.K_KP3
    KP4 =  pygame.K_KP4
    KP5 =  pygame.K_KP5
    KP6 =  pygame.K_KP6
    KP7 =  pygame.K_KP7
    KP8 =  pygame.K_KP8
    KP9 =  pygame.K_KP9
    KPPeriod =  pygame.K_KP_PERIOD
    KPDivide =  pygame.K_KP_DIVIDE
    KPMultiply =  pygame.K_KP_MULTIPLY
    KPMinus =  pygame.K_KP_MINUS
    KPPlus =  pygame.K_KP_PLUS
    KPEnter =  pygame.K_KP_ENTER
    KPEquals =  pygame.K_KP_EQUALS
    Up =  pygame.K_UP
    Down =  pygame.K_DOWN
    Right =  pygame.K_RIGHT
    Left =  pygame.K_LEFT
    Insert =  pygame.K_INSERT
    Home =  pygame.K_HOME
    End =  pygame.K_END
    Pageup =  pygame.K_PAGEUP
    Pagedown =  pygame.K_PAGEDOWN
    F1 =  pygame.K_F1
    F2 =  pygame.K_F2
    F3 =  pygame.K_F3
    F4 =  pygame.K_F4
    F5 =  pygame.K_F5
    F6 =  pygame.K_F6
    F7 =  pygame.K_F7
    F8 =  pygame.K_F8
    F9 =  pygame.K_F9
    F10 =  pygame.K_F10
    F11 =  pygame.K_F11
    F12 =  pygame.K_F12
    Numlock =  pygame.K_NUMLOCK
    Capslock =  pygame.K_CAPSLOCK
    RShift =  pygame.K_RSHIFT
    LShift =  pygame.K_LSHIFT
    RCtrl =  pygame.K_RCTRL
    LCtrl =  pygame.K_LCTRL
    RAlt =  pygame.K_RALT
    LAlt =  pygame.K_LALT

_sign = lambda x: 1 if x > 0 else -1 if x < 0 else 0

class Input(_NoInit):
    """Contains nput data and functions"""
    pressedKeys:list[bool] = list()
    frameEvents:pygame.event.Event = None
    pressedMouse:list[bool] = list()
    mousePosition:Vector2 = Vector2()
    mouseRelative:Vector2= Vector2()
    mouseVisible:bool = True
    mouseWheelRel:Vector2 = Vector2()
    movementElasticity:float = 0.05
    horizontalMovement:float = 0
    verticalMovement:float = 0
    _keyData:dict[int,int] = dict()
    _mouseData:dict[int,int] = dict()
    
    @classmethod
    def _update(cls):
        cls.pressedKeys = pygame.key.get_pressed()
        cls.pressedMouse = pygame.mouse.get_pressed()
        cls.mousePosition = Vector2(pygame.mouse.get_pos())
        cls.mouseRelative = Vector2(pygame.mouse.get_rel())
        cls.mouseWheelRel.update(0,0)
        cls._keyData = dict.fromkeys(cls._keyData,0)
        cls._mouseData = dict.fromkeys(cls._mouseData,0)
        anyh = False
        anyv = False
        if cls.pressedKeys[pygame.K_a] or cls.pressedKeys[pygame.K_LEFT]:
            cls.horizontalMovement -= cls.movementElasticity
            if cls.horizontalMovement < -1:
                cls.horizontalMovement = -1
            anyh = True
        if cls.pressedKeys[pygame.K_d] or cls.pressedKeys[pygame.K_RIGHT]:
            cls.horizontalMovement += cls.movementElasticity
            if cls.horizontalMovement > 1:
                cls.horizontalMovement = 1
            anyh = True
        if not anyh:
            if cls.horizontalMovement != 0:
                old = _sign(cls.horizontalMovement)
                cls.horizontalMovement -= cls.movementElasticity*old
                if old != _sign(cls.horizontalMovement):
                    cls.horizontalMovement = 0
        if cls.pressedKeys[pygame.K_w] or cls.pressedKeys[pygame.K_UP]:
            cls.verticalMovement -= cls.movementElasticity
            if cls.verticalMovement < -1:
                cls.verticalMovement = -1
            anyv = True
        if cls.pressedKeys[pygame.K_s] or cls.pressedKeys[pygame.K_DOWN]:
            cls.verticalMovement += cls.movementElasticity
            if cls.verticalMovement > 1:
                cls.verticalMovement = 1
            anyv = True
        if not anyv:
            if cls.verticalMovement != 0:
                old = _sign(cls.verticalMovement)
                cls.verticalMovement -= cls.movementElasticity*old
                if old != _sign(cls.verticalMovement):
                    cls.verticalMovement = 0
    
    @classmethod
    def _event(cls,event):
        if event.type == pygame.KEYDOWN:
            cls._keyData[event.key] = 1
        elif event.type == pygame.KEYUP:
            cls._keyData[event.key] = 2
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cls._mouseData[event.button] = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            cls._mouseData[event.button] = 2
        elif event.type == pygame.MOUSEWHEEL:
            cls.mouseWheelRel.y = event.y
            cls.mouseWheelRel.x = event.x
        
    @classmethod
    def _init(cls,elasticity):
        cls.movementElasticity = elasticity
        for kc in _pygame_key_codes:
            cls._keyData[kc] = 0
        for i in range(30):
            cls._mouseData[i] = 0
        cls._update()
        
    @classmethod
    def MouseVisibility(cls,visible:bool):
        """Changes the mouse visibility"""
        pygame.mouse.set_visible(visible)
        cls.mouseVisible = pygame.mouse.get_visible()
    
    @staticmethod
    def KeyFromName(name:str)->int:
        """Convert a name into a keycode"""
        return pygame.key.key_code(name)
    
    @staticmethod
    def NameFromKey(key_code:int)->str:
        """Convert a keycode into a name"""
        return pygame.key.name(key_code)
    
    @classmethod
    def GetKey(cls,key_code:int)->bool:
        """Is the key held?"""
        return cls.pressedKeys[key_code]
    
    @classmethod
    def GetKeyDown(cls,key_code:int)->bool:
        """Return true the frame the key is pressed"""
        return cls._keyData[key_code] == 1
    
    @classmethod
    def GetKeyUp(cls,key_code:int)->bool:
        """Return true the frame the key is released"""
        return cls._keyData[key_code] == 2
    
    @classmethod
    def AnyKey(cls)->bool:
        """Is any key held?"""
        return any(cls.pressedKeys)
    
    @classmethod
    def GetMouse(cls,button:int)->bool:
        """Is the mouse button held?"""
        return cls.pressedMouse[button]
    
    @classmethod
    def GetMouseDown(cls,button:int)->bool:
        """Return true the frame the button is pressed"""
        return cls._mouseData[button+1] == 1
    
    @classmethod
    def GetMouseUp(cls,button:int)->bool:
        """Return true the frame the key is released"""
        return cls._mouseData[button+1] == 2
    
    @classmethod
    def AnyButton(cls)->bool:
        """Is any button held?"""
        return any(cls.pressedMouse)