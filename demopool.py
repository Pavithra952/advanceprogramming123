import multiprocessing
def square(x):
    return x * x
if __name__=='__main__':
    with multiprocessing.Pool(processes=4) as pool:
        result=pool.map(square,[1,2,3,4,5])
    print(result)
