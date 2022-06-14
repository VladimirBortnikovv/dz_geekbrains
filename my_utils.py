def gen_zip(a_iter, b_iter):
    len_b = len(b_iter)
    return ((a_elem, b_iter[i]) if i < len_b else (a_elem, None)
            for i, a_elem in enumerate(a_iter))
