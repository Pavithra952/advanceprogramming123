import multiprocessing

def cal_sqare(numbers,res):

    for i,n in enumerate(numbers):
        res[i]=n*n
    print(multiprocessing.current_process())
if __name__=='__main__':
    num=[1,2,3,7,8]
    res=multiprocessing.Array('i',5)
    v=multiprocessing.Value('d',0.0)
    p1=multiprocessing.Process(target=cal_sqare,args=(num,res))
    print(p1.name)
    print(multiprocessing.current_process())
    p1.start()
    p1.join()
    print(res[:])