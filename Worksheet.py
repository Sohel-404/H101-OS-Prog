# #1
# def sum_sq(n):
#     s=0
#     for i in range(1,n+1):
#         sqi=i**2
#         s=s+sqi
#         i=i+1
#     return s
#
# def main():
#     n=int(input('Enter n numbers: '))
#     out=sum_sq(n)
#     print(f'The sum of first {n} integers is {out}.')
#
# if __name__ == '__main__':
#     main()
#
# #2
# def dec_bin(d):
#     if d==0:
#         return 0
#     binary=''
#     while d>0:
#         remainder=d%2
#         binary=str(remainder) + binary
#         d=d//2
#     return binary
#
# #3
# def count_1(d):
#     bn=(dec_bin(d))
#     c=0
#     for i in bn:
#         if i=='1':
#             c=c+1
#     return c
# # 2 & 3 combine main
# def main():
#     d=int(input('Enter decimal number: '))
#     out=(dec_bin(d))
#     print(f'Binary number: {out}')
#     ones=count_1(d)
#     print(f'Numer of 1s :{ones}')
#
# if __name__ == '__main__':
#     main()
#
# #4
#
# def bin_dec(b):
#     b=b[::-1]
#     n=0
#     p=0
#     for i in b:
#         m=(2**p)*int(i)
#         int_m=int(m)
#         n+=int_m
#         p+=1
#     return n
#
# def main():
#     b=input('Enter binary number: ')
#     result=bin_dec(b)
#     print(f'Decimal number:{result}')
#
# if __name__ == '__main__':
#     main()
#
# #5
# def power(base,exp):
#     result=base**exp
#     return result
#
# def main():
#     base=int(input('Enter base number: '))
#     exp=int(input('Enter the power: '))
#     print(power(base,exp))
#
# if __name__ == '__main__':
#     main()
#
# #6
#
# def prime(p):
#     if p==0 or p==1:
#         return 'Neither prime nor composite'
#     elif p==2 or p==3:
#         return True
#     else:
#         for i in range(2,p-1):
#             if p%int(i)==0:
#                 return False
#             else:
#                 return True
#
#
# def main():
#     p=int(input('Enter number to check if it\'s prime: '))
#     print(prime(p))
# if __name__ == '__main__':
#     main()
#
# #7
#
# def individual_digits(n):
#     n=list(n)
#     for i in list(n):
#         print(int(i))
#
# def main():
#     n=input('Enter number: ')
#     individual_digits(n)
# if __name__ == '__main__':
#     main()
#
# #8. Write a function to print the first half of a string, S.
#
# def half_s(s):
#     l=len(s)
#     half_l=int(l)
#     print(f'Half of string:{s[0:l//2]}')
#
# def main():
#     s=str(input('Enter string: '))
#     (half_s(s))
# if __name__ == '__main__':
#     main()
#
#  9. Write print alternate characters of a string, S
# def alt_s(s):
#     alt_elements=s[0::2]
#     return alt_elements
#
# def main():
#     s=input('Enter string: ')
#     print(alt_s(s))
# if __name__ == '__main__':
#     main()
#
# #10. Write a program to concatenate two strings, S1 and S2.
# def con(s1,s2):
#     s_blank=' '
#     s3 = s1 + s_blank + s2
#     return s3
#
# def main():
#     s1=str(input('Enter string 1: '))
#     s2=str(input('Enter string 2: '))
#     print(con(s1,s2))
#
# if __name__ == '__main__':
#     main()
#
# 11. Write a function to find the first occurrence of a character, c, in a string S.
# def position_c(string_s):
#     c=string_s.find('c')
#     return c
#
# def main():
#     string_s=str(input('Enter string: '))
#     print('Position of first occurrence of character "c" is: ',position_c(string_s))
# if __name__ == '__main__':
#     main()
#
# #12. Write a function to find the highest frequency character in a string, S.
# def high_freq(s):
#     freq={}
#     for i in s:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     max_freq= max(freq,key=freq.get)
#     return max_freq
#
# def main():
#     s=str(input('Enter string: '))
#     print(high_freq(s))
# if __name__ == '__main__':
#     main()
#
# #13. Write a function to replace all occurrences of a character, c, with another character, d.
# def rep(sen):
#     r_sen=sen.replace('c','d')
#     return r_sen
#
# def main():
#     sen=str(input('Enter sentence/word: '))
#     print(rep(sen))
# if __name__ == '__main__':
#     main()
#
# #14. Write a function to trim leading whitespace characters from a string, S.
# def trim(st):
#     no_space=st.strip(' ')
#     return no_space
#
# def main():
#     st=str(input('Enter a string: '))
#     print(trim(st))
# if __name__ == '__main__':
#     main()
#
# #15. Write a function to count the number of occurrences of a word, W, in a sentence, S.
# def count_w(sen,wor):
#     word_c=sen.count(wor)
#     return word_c
#
# def main():
#     sen=str(input('Enter sentence: '))
#     wor=str(input('Enter word: '))
#     print(count_w(sen,wor))
# if __name__ == '__main__':
#     main()
#
#
# #16. Write a function to check if two strings are anagrams of each other . Eg. listen and silent
# # are anagrams, gram and arm are not anagrams
# def anagram(ana_1,ana_2):
#     ana_1=sorted(ana_1)
#     ana_2=sorted(ana_2)
#     l1=len(ana_1)
#     l2=len(ana_2)
#     if l1==l2:
#         for i in ana_1:
#             for j in ana_2:
#                 if i==j:
#                     return True
#     else:
#         return False
#
#
#
# def main():
#     ana_1 = str(input('Enter first word: '))
#     ana_2 = str(input('Enter second word: '))
#
#     print(f'Anagram check: {anagram(ana_1,ana_2)}')
# if __name__ == '__main__':
#     main()