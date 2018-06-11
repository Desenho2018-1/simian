"""
Keyboard classes used to manage
user keyboard input.
"""
import pygame
from simian.utils.singleton import Singleton


class Keyboard(metaclass=Singleton):
    """
    Class that represent a computer keyboard
    with representation of 92 keys.
    """
    BACKSPACE = pygame.K_BACKSPACE
    TAB = pygame.K_TAB
    CLEAR = pygame.K_CLEAR
    RETURN = pygame.K_RETURN
    PAUSE = pygame.K_PAUSE
    ESCAPE = pygame.K_ESCAPE
    SPACE = pygame.K_SPACE
    COMMA = pygame.K_COMMA
    MINUS = pygame.K_MINUS
    K_0 = pygame.K_0
    K_1 = pygame.K_1
    K_2 = pygame.K_2
    K_3 = pygame.K_3
    K_4 = pygame.K_4
    K_5 = pygame.K_5
    K_6 = pygame.K_6
    K_7 = pygame.K_7
    K_8 = pygame.K_8
    K_9 = pygame.K_9
    K_a = pygame.K_a
    K_b = pygame.K_b
    K_c = pygame.K_c
    K_d = pygame.K_d
    K_e = pygame.K_e
    K_f = pygame.K_f
    K_g = pygame.K_g
    K_h = pygame.K_h
    K_i = pygame.K_i
    K_j = pygame.K_j
    K_k = pygame.K_k
    K_l = pygame.K_l
    K_m = pygame.K_m
    K_n = pygame.K_n
    K_o = pygame.K_o
    K_p = pygame.K_p
    K_q = pygame.K_q
    K_r = pygame.K_r
    K_s = pygame.K_s
    K_t = pygame.K_t
    K_u = pygame.K_u
    K_v = pygame.K_v
    K_w = pygame.K_w
    K_x = pygame.K_x
    K_y = pygame.K_y
    K_z = pygame.K_z
    DELETE = pygame.K_DELETE
    NUMPAD_0 = pygame.K_KP0
    NUMPAD_1 = pygame.K_KP1
    NUMPAD_2 = pygame.K_KP2
    NUMPAD_3 = pygame.K_KP3
    NUMPAD_4 = pygame.K_KP4
    NUMPAD_5 = pygame.K_KP5
    NUMPAD_6 = pygame.K_KP6
    NUMPAD_7 = pygame.K_KP7
    NUMPAD_8 = pygame.K_KP8
    NUMPAD_9 = pygame.K_KP9
    NUMPAD_PERIOD = pygame.K_KP_PERIOD
    NUMPAD_SLASH = pygame.K_KP_DIVIDE
    NUMPAD_ASTERISC = pygame.K_KP_MULTIPLY
    NUMPAD_MINUS = pygame.K_KP_MINUS
    NUMPAD_PLUS = pygame.K_KP_PLUS
    NUMPAD_ENTER = pygame.K_KP_ENTER
    NUMPAD_EQUALS = pygame.K_KP_EQUALS
    UP = pygame.K_UP
    DOWN = pygame.K_DOWN
    RIGHT = pygame.K_RIGHT
    LEFT = pygame.K_LEFT
    INSERT = pygame.K_INSERT
    HOME = pygame.K_HOME
    END = pygame.K_END
    PAGEUP = pygame.K_PAGEUP
    PAGEDOWN = pygame.K_PAGEDOWN
    F1 = pygame.K_F1
    F2 = pygame.K_F2
    F3 = pygame.K_F3
    F4 = pygame.K_F4
    F5 = pygame.K_F5
    F6 = pygame.K_F6
    F7 = pygame.K_F7
    F8 = pygame.K_F8
    F9 = pygame.K_F9
    F10 = pygame.K_F10
    F11 = pygame.K_F11
    F12 = pygame.K_F12
    F13 = pygame.K_F13
    F14 = pygame.K_F14
    F15 = pygame.K_F15
    SHIFT_RIGHT = pygame.K_RSHIFT
    SHIFT_LEFT = pygame.K_LSHIFT
    CTRL_RIGHT = pygame.K_RCTRL
    CTRL_LEFT = pygame.K_LCTRL
    ALT_RIGHT = pygame.K_RALT
    ALT_LEFT = pygame.K_LALT

    def is_key_pressed(self, key):
        """
        Return if the given key was pressed.
        """
        return pygame.key.get_pressed()[key]
