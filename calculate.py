import circle  # noqa: F401
import square  # noqa: F401

figs = ["circle", "square"]
funcs = ["perimeter", "area"]


def calc(fig, func, size):
    assert fig in figs
    assert func in funcs
    result = eval(f"{fig}.{func}(*{size})")
    return result


if __name__ == "__main__":
    fig = input(f"Enter figure name (available: {figs}):\n").strip()
    func = input(f"Enter function name (available: {funcs}):\n").strip()
    size_inp_msg = "Enter size(s), separated by spaces:\n"
    size = list(map(float, input(size_inp_msg).split()))
    try:
        result = calc(fig, func, size)
        print(f"The {func} of {fig} is {result}")
    except ValueError as e:
        print(e)
