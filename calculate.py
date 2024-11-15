import circle
import square
import triangle

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']

def calc(fig, func, size):
    assert fig in figs
    assert func in funcs

    if fig == 'circle':
        if func == 'area':
            return circle.circle_area(*size)
        elif func == 'perimeter':
            return circle.circle_perimeter(*size)
    elif fig == 'square':
        if func == 'area':
            return square.square_area(*size)
        elif func == 'perimeter':
            return square.square_perimeter(*size)
    elif fig == 'triangle':
        if func == 'area':
            return triangle.triangle_area(*size)
        elif func == 'perimeter':
            return triangle.triangle_perimeter(*size)
