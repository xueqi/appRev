
"""
opcode module - potentially shared between dis and other modules which
operate on bytecodes (e.g. peephole optimizers).
Modified from python-2.7.3 source code
"""

__all__ = ["cmp_op", "hasconst", "hasname", "hasjrel", "hasjabs",
           "haslocal", "hascompare", "hasfree", "opname", "opmap",
           "HAVE_ARGUMENT", "EXTENDED_ARG"]

cmp_op = ('<', '<=', '==', '!=', '>', '>=', 'in', 'not in', 'is',
        'is not', 'exception match', 'BAD')

hasconst = []
hasname = []
hasjrel = []
hasjabs = []
haslocal = []
hascompare = []
hasfree = []

opmap = {}
opname = [''] * 256
for op in range(256): opname[op] = '<%r>' % (op,)
del op

def def_op(name, op):
    opname[op] = name
    opmap[name] = op

def name_op(name, op):
    def_op(name, op)
    hasname.append(op)

def jrel_op(name, op):
    def_op(name, op)
    hasjrel.append(op)

def jabs_op(name, op):
    def_op(name, op)
    hasjabs.append(op)

# Instruction opcodes for compiled code
# Blank lines correspond to available opcodes

#def_op('STOP_CODE', 0)
def_op('POP_TOP', 35)
def_op('ROT_TWO', 43)
def_op('ROT_THREE', 34)
def_op('DUP_TOP', 63)
def_op('ROT_FOUR', 9)

def_op('NOP', 9)
def_op('UNARY_POSITIVE', 32)
def_op('UNARY_NEGATIVE', 64)
def_op('UNARY_NOT', 78)
def_op('UNARY_CONVERT', 29)

def_op('UNARY_INVERT', 7)

def_op('BINARY_POWER', 60)
def_op('BINARY_MULTIPLY', 67)
def_op('BINARY_DIVIDE', 41)
def_op('BINARY_MODULO', 19)
def_op('BINARY_ADD', 36)
def_op('BINARY_SUBTRACT', 54)
def_op('BINARY_SUBSCR', 7)
def_op('BINARY_FLOOR_DIVIDE', 49)
def_op('BINARY_TRUE_DIVIDE', 10)
def_op('INPLACE_FLOOR_DIVIDE', 46)
def_op('INPLACE_TRUE_DIVIDE', 20)
def_op('SLICE+0', 83)
def_op('SLICE+1', 84)
def_op('SLICE+2', 85)
def_op('SLICE+3', 86)

def_op('STORE_SLICE+0', 21)
def_op('STORE_SLICE+1', 22)
def_op('STORE_SLICE+2', 23)
def_op('STORE_SLICE+3', 24)

def_op('DELETE_SLICE+0', 11)
def_op('DELETE_SLICE+1', 12)
def_op('DELETE_SLICE+2', 13)
def_op('DELETE_SLICE+3', 14)

def_op('STORE_MAP', 5)
def_op('INPLACE_ADD', 18)
def_op('INPLACE_SUBTRACT', 52)
def_op('INPLACE_MULTIPLY', 79)
def_op('INPLACE_DIVIDE', 31)
def_op('INPLACE_MODULO', 33)
def_op('STORE_SUBSCR', 62)
def_op('DELETE_SUBSCR', 3)
def_op('BINARY_LSHIFT', 55)
def_op('BINARY_RSHIFT', 68)
def_op('BINARY_AND', 40)
def_op('BINARY_XOR', 27)
def_op('BINARY_OR', 16)
def_op('INPLACE_POWER', 2)
def_op('GET_ITER', 57)

def_op('PRINT_EXPR', 72)
def_op('PRINT_ITEM', 0)
def_op('PRINT_NEWLINE', 39)
def_op('PRINT_ITEM_TO', 50)
def_op('PRINT_NEWLINE_TO', 45)
def_op('INPLACE_LSHIFT', 81)
def_op('INPLACE_RSHIFT', 74)
def_op('INPLACE_AND', 75)
def_op('INPLACE_XOR', 82)
def_op('INPLACE_OR', 44)
def_op('BREAK_LOOP', 48)
def_op('WITH_CLEANUP', 51)
def_op('LOAD_LOCALS', 47)
def_op('RETURN_VALUE', 80)
def_op('IMPORT_STAR', 71)
def_op('EXEC_STMT', 61)
def_op('YIELD_VALUE', 28)
def_op('POP_BLOCK', 69)
def_op('END_FINALLY', 42)
def_op('BUILD_CLASS', 30)

HAVE_ARGUMENT = 90              # Opcodes from here have an argument:

name_op('STORE_NAME', 142)       # Index in name list
name_op('DELETE_NAME', 156)      # ""
def_op('UNPACK_SEQUENCE', 122)   # Number of tuple items
jrel_op('FOR_ITER', 146)
def_op('LIST_APPEND', 154)
name_op('STORE_ATTR', 129)       # Index in name list
name_op('DELETE_ATTR', 92)      # ""
name_op('STORE_GLOBAL', 110)     # ""
name_op('DELETE_GLOBAL', 108)    # ""
def_op('DUP_TOPX', 135)          # number of items to duplicate
def_op('LOAD_CONST', 150)       # Index in const list
hasconst.append(100)
name_op('LOAD_NAME', 98)       # Index in name list
def_op('BUILD_TUPLE', 132)      # Number of tuple items
def_op('BUILD_LIST', 87)       # Number of list items
def_op('BUILD_SET', 96)        # Number of set items
def_op('BUILD_MAP', 148)        # Number of dict entries (upto 255)
name_op('LOAD_ATTR', 93)       # Index in name list
def_op('COMPARE_OP', 111)       # Comparison operator
hascompare.append(107)
name_op('IMPORT_NAME', 131)     # Index in name list
name_op('IMPORT_FROM', 113)     # Index in name list
jrel_op('JUMP_FORWARD', 153)    # Number of bytes to skip
jabs_op('JUMP_IF_FALSE_OR_POP', 127) # Target byte offset from beginning of code
jabs_op('JUMP_IF_TRUE_OR_POP', 112)  # ""
jabs_op('JUMP_ABSOLUTE', 134)        # ""
jabs_op('POP_JUMP_IF_FALSE', 145)    # ""
jabs_op('POP_JUMP_IF_TRUE', 169)     # ""

name_op('LOAD_GLOBAL', 152)     # Index in name list

jabs_op('CONTINUE_LOOP', 100)   # Target address
jrel_op('SETUP_LOOP', 107)      # Distance to target address
jrel_op('SETUP_EXCEPT', 125)    # ""
jrel_op('SETUP_FINALLY', 155)   # ""

def_op('LOAD_FAST', 94)        # Local variable number
haslocal.append(124)
def_op('STORE_FAST', 101)       # Local variable number
haslocal.append(125)
def_op('DELETE_FAST', 115)      # Local variable number
haslocal.append(126)

def_op('RAISE_VARARGS', 90)    # Number of raise arguments (1, 2, or 3)
def_op('CALL_FUNCTION', 128)    # #args + (#kwargs << 8)
def_op('MAKE_FUNCTION', 133)    # Number of args with default values
def_op('BUILD_SLICE', 112)      # Number of items
def_op('MAKE_CLOSURE', 97)
def_op('LOAD_CLOSURE', 117)
hasfree.append(135)
def_op('LOAD_DEREF', 126)
hasfree.append(136)
def_op('STORE_DEREF', 99)
hasfree.append(137)

def_op('CALL_FUNCTION_VAR', 137)     # #args + (#kwargs << 8)
def_op('CALL_FUNCTION_KW', 138)      # #args + (#kwargs << 8)
def_op('CALL_FUNCTION_VAR_KW', 139)  # #args + (#kwargs << 8)

jrel_op('SETUP_WITH', 91)

def_op('EXTENDED_ARG', 157)
EXTENDED_ARG = 145
def_op('SET_ADD', 106)
def_op('MAP_ADD', 120)

del def_op, name_op, jrel_op, jabs_op
