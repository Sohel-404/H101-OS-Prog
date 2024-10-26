import random
#
# #1. Write a function to find the sum and average of numbers in a list, L.
# def sum_a(a):
#     total_a = 0
#     for i in range(0,len(a)):
#         total_a += a[i]
#     return total_a
#
#
# def avg_a(a):
#     avg = sum_a(a) / len(a)
#     return avg
#
#
# def main():
#     a = [random.randint(0,100) for _ in range(random.randint(1,20))]
#     print(a)
#     print('Sum of list A: ',sum_a(a))
#     print('Average of list A: %0.2f'%avg_a(a))
# if __name__ == '__main__':
#     main()
#
# #2 Write a function to find the minimum and maximum number in a list, L.
# def min_a(a):
#     minimum = 0
#     for i in a:
#         if i < minimum:
#             minimum = i
#     return minimum
#
# def max_a(a):
#     maximum = 0
#     for i in a:
#         if i > maximum:
#             maximum = i
#     return maximum
#
# def main():
#     a = [random.randint(0,100) for _ in range(random.randint(1,20))]
#     print('List: ',a)
#     print('Minimum: ',min_a(a))
#     print('Maximum: ',max_a(a))
#
# if __name__ == '__main__':
#     main()
#
# #3 Write a program to find the even numbers in a list, L.
# def even(a):
#     even_list = [i for i in a if i % 2 == 0]
#     return even_list
#
# def main():
#     a = [random.randint(0, 100) for _ in range(random.randint(1, 20))]
#     print('List a : ',a)
#     print('Even numbers in a: ',even(a))
# if __name__ == '__main__':
#     main()
#
# #4 Write a program to print the duplicate elements in a list, L.
# def duplicate(a):
#     dup_list  = { i for i in a if a.count(i)>1 }
#     return list(dup_list)
#
# def main():
#     a = [random.randint(0, 10) for _ in range(random.randint(1, 20))]
#     print('List a: ',a)
#     print('Duplicate elements: ',duplicate(a))
#
# if __name__ == '__main__':
#     main()
#
# #5 Write a program to subtract two matrices, m1 and m2, using a list of lists.
# def matrix_sub(m1,m2):
#     m = [[0,0,0],[0,0,0],[0,0,0]]
#     l_m1 = len(m1)
#     l_m2 = len(m2)
#     for i in range(l_m1):
#         for j in range(l_m2):
#             m[i][j] = m1[i][j] - m2[i][j]
#     return m
#
# def main():
#     m1 = [[10, 20, 21],[21, 25, 64],[32, 14, 54 ]]
#     m2 = [[1, 2, 2],[2, 5, 6],[3, 1, 5 ]]
#
#     print(matrix_sub(m1,m2))
# if __name__ == '__main__':
#     main()
#
# #6 Write a program to extract elements of a list, if it occurs more than k times.
# def extract(a,k):
#     k_list = { i for i in a if a.count(i) > k }
#     return list(k_list)
#
# def main():
#     a = [random.randint(0, 10) for _ in range(random.randint(10, 20))]
#     k = int(input('Number of occurrences: '))
#     print('List a: ',a)
#     print('Extracted list: ',extract(a,k))
#
# if __name__ == '__main__':
#     main()
#
# #7 Write a program to remove all occurrences of an element from a list, L.
# def remove_l(a,l):
#      l_list=[ i for i in a if i!=l ]
#      return l_list
#
# def main():
#     a = [random.randint(1,10) for _ in range(random.randint(1,20))]
#     print(a)
#     l = int(input('Enter element to remove: '))
#     print(remove_l(a,l))
# if __name__ == '__main__':
#     main()
#
# #8 Write a program to extract words from a string list, L whose first character is k.
# def remove_k(a,k):
#     for i in a:
#         if i[0]== k:
#             print(i)
#
# def main():
#     a = ['koenigsegg','ferrari','porsche','mclaren','pagani','maserati']
#     k = input('Remove word starting with: ')
#     remove_k(a,k)
#
# if __name__ == '__main__':
#     main()
#
# #9 Write a program to iterate over a dictionary and print key and values.
# def dict_x(a):
#     for keys,values in a.items():
#         print(f'Key:{keys} Value:{values}')
#
# def main():
#     a = { 'a':1,'b':2,'c':3,'d':4,'e':5 }
#     dict_x(a)
# if __name__ == '__main__':
#     main()
#
# #10 Write a program to sum all values of a dictionary.
# def val_sum(a):
#     s = 0
#     for keys,values in a.items():
#         s += values
#     return s
#
# def main():
#     a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#     print(val_sum(a))
#
# if __name__ == '__main__':
#     main()
#
# #11 Write a program to find the maximum and minimum value of a dictionary
# def dict_mm(a):
#     d_min(a)
#     d_max(a)
#
# def d_min(a):
#     mi = 0
#     for keys, values in a.items():
#         if values < mi:
#             mi = values
#     print(f'Minimum: ',mi)
#
# def d_max(a):
#     ma = 0
#     for keys, values in a.items():
#         if values > ma:
#             ma = values
#     print(f'Maximum: ',ma)
#
# def main():
#     a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#     dict_mm(a)
#
# if __name__ == '__main__':
#     main()
#
# #12 Write a program to implement an insertion sort algorithm.
# def insertion_sort(a):
#     l = len(a)
#     for j in range(0,l):
#         key = a[j]
#         i = j-1
#         while i >=0 and a[i]>key:
#             a[i+1] = a[i]
#             i -= 1
#         a[i+1] = key
#     return a
#
# def main():
#     a = [ random.randint(0,100) for _ in range(random.randint(0,20))]
#     print('List a:',a)
#     print('Sorted list:',insertion_sort(a))
#
# if __name__ == '__main__':
#     main()
#
# #13 Given a dictionary with a values list, extract the key whose value has the most unique values.
# def dict_u(a):
#     v_list = [values for keys, values in a.items()]
#     print('Value lists:', v_list)
#     max_key = uniq(a)
#     print("Key with max unique values:", max_key)
#
# def uniq(a):
#     u_list = {}
#     for key, values in a.items():
#         uniq_val = set(values)
#         u_list[key] = len(uniq_val)
#         print(f"Unique values '{key}': {uniq_val}, Count: {len(uniq_val)}")
#     max_key = max(u_list, key=u_list.get)
#     return max_key
#
# def main():
#     a = {'Good': [5, 7, 7, 7, 7], 'Better': [6, 7, 7, 7], 'Best': [9, 9, 6, 5, 5]}
#     dict_u(a)
#
# if __name__ == '__main__':
#     main()