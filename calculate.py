import circle
import square
import triangle

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']

def calc(fig, func, size):
    if fig not in figs:
        raise ValueError("Unsupported figure")
    if func not in funcs:
        raise ValueError("Unsupported function")
    
    result = eval(f'{fig}.{func}(*{size})')
    return result
