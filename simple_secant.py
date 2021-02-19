def simple_secant(f, init_1, init_2, maxiter, verbose):
    """
    """
    x_n1 = init_1
    x_n2 = init_2

    for i in range(0, maxiter):
        x_n = x_n1 - f(x_n1) * (x_n1 + x_n2) / (f(x_n1) - f(x_n2))
        x_n2 = x_n1
        x_n1 = x_n
    return x_n
