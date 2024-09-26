import time
from tqdm import tqdm
# from ..box.box import Display


def selection_sort(lst):
    for f in range(len(lst)):
        currmin = lst[f]
        idx = f
        for e in range(f, len(lst)):
            if lst[e] < currmin:
                currmin = lst[e]
                idx = e
        lst[idx], lst[f]  = lst[f], lst[idx]



if __name__ == "__main__":
    l = [7, 4, 8, 6, 2 ,1 ,9, 10, 5, 3, 15]
    # dispOne = Display(max(l),len(l))
    print(f"Before: {l}".format(l))
    selection_sort(l)
    print(f"After: {l}".format(l))