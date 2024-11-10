import random
# from itertools import count
from os.path import split
import time
from time import sleep


def main():
    #1
    # fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
    # print('fruits: ',fruits)
    # capitalized_fruits = [ x.title() for x in fruits ]
    # print('capitalized fruits: ',capitalized_fruits)
    #
    # #2
    # vowels = ['a','e','i','o','u']
    # fruits_with_only_two_vowels = [ fruits for fruits in fruits if
    #                                 fruits.count('a') +
    #                                 fruits.count('e') +
    #                                 fruits.count('i') +
    #                                 fruits.count('o') +
    #                                 fruits.count('u') == 2 ]
    # print(fruits_with_only_two_vowels)
    #
    #3
    # org1 = ["ACGTTTCA", "AGGCCTTA", "AAAACCTG"]
    # org2 = ["AGCTTTGA", "GCCGGAAT", "GCTACTGA"]
    # def similarity(seq1,seq2):
    #     match = sum(1 for a,b in zip(seq1,seq2) if a == b)
    #     return match
    #
    # threshold = 2
    # similar_pairs = [(seq1,seq2) for seq1,seq2 in zip(org1,org2) if similarity(seq1,seq2) > threshold ]
    # print(similar_pairs)
    #
    #4
    # key = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
    # val = [ i**2 for i in key ]
    # num_dict = { key:val for key,val in zip(key,val) if key%2!=0 }
    # print(num_dict)
    #
    #5
    # key = "Hello, how are you?"
    # key = key.split(' ')
    # val = [ i[::-1] for i in key ]
    # sen_dict = { key:val for key,val in zip(key,val) }
    # print(sen_dict)
    #
    # # 6
    # l = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
    # l_sort = sorted(l,key = lambda x:x[-1])
    # print(l_sort)
    # #
    # # 7
    # n = [random.randint(-10,10)for _ in range(10)]
    # n_sort = sorted(n, key = lambda x: x>=0)
    # print(n_sort)
    # # 8
    # def log_decorator(func):
    #     def wrapper(*args,**kwargs):
    #         print(f'Calling add with args:{args}, kwargs:{kwargs}')
    #         result = func(*args,**kwargs)
    #         print(f'add returned:{result}')
    #     return wrapper
    #
    # @log_decorator
    # def add(a,b):
    #     return a + b
    #
    # add(2,3)
    #
    # #9
    # def log_time(func):
    #     def wrapper(*args,**kwargs):
    #         begin = time.time()
    #
    #         func(*args,**kwargs)
    #
    #         end = time.time()
    #         print('Total time: ',func.__name__,end - begin)
    #
    #     return wrapper
    #
    # @log_time
    # def add(a,b):
    #     print('result:',a + b)
    #
    # add(2,3)
    #
    # #10
    # def division(a,b):
    #     try:
    #         print(a/b)
    #     except ZeroDivisionError as ze:
    #         print('Error:',ze)
    #     except ValueError as ve:
    #         print('Error',ve)
    #     except Exception as e:
    #         print('Unknown error',e)
    #     finally:
    #         print('Operation done')
    #
    # division(10,5)
    # division(10,0)
    # division(10,'5')
    #
    # #11
    n = input('Enter operation:')
    ns = n.split()
    def calculator():
            if n.lower()=='quit':
                print('Bye')
            

            try:
                a = float(ns[0])
                b = float(ns[2])
                if ns[1]=='+':
                    print('result:',a + b)
                if ns[1]=='-':
                    print('result',a -b)

            except ValueError :
                print('Formula Error: Use valid format( number <space> operator <space> number )')
            except Exception as e:
                if len(ns) != 3 :
                    print('Formula Error',e)
                if ns[1] not in ('+','-'):
                    print(e)
    calculator()





if __name__ == '__main__':
    main()