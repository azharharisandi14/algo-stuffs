def create_array(size=10, max=50):
    from random import randint
    return [randint(0, max) for _ in range(size)]


def merge(a, b, count_inv):
    a_idx, b_idx = 0, 0
    c = []
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1
            count_inv += (len(a) - a_idx)
            
    if a_idx == len(a): c.extend(b[b_idx:])
    else: c.extend(a[a_idx:])

    return c, count_inv


def merge_sort(a):
    # a list of zero or one elements is sorted
    if len(a) <= 1:
        return a, 0

    # split the list
    left, count_left = merge_sort(a[:len(a)//2])
    right, count_right = merge_sort(a[len(a)//2:])
    count = (count_left + count_right)

    # merge the now-sorted sublists
    return merge(left, right, count)


if __name__ == '__main__':

    # a = [3, 4, 6, 1, 2, 5]
    a = create_array(size=100, max=50) 
    print(f"Original Array : {a}")
    s, inversions = merge_sort(a)
    print(f"Sorted Array : {s}\nnumber of inversion(s) in array : {inversions}")
