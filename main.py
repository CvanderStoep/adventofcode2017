from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(10) as p:
        print(p.map(f, list(range(10))))