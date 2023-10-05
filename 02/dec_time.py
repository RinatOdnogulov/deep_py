import time


def mean(k):

    def inner_mean(func):
        lst = []

        def inner(*args, **kwargs):
            start_time = time.time()
            res = func(*args, **kwargs)
            end_time = time.time()
            lst.append(end_time - start_time)
            if k <= 0 or not isinstance(k, int):
                print("Значение k введено некорректно")
            elif len(lst) < k:
                print(sum(lst)/len(lst))
            else:
                print(sum(lst[len(lst) - k:])/k)
            return res
        return inner
    return inner_mean
