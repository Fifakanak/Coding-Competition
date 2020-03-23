# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:08:20 2020

@author: Kanak
"""
#3
#4 3
#3 1 9 100
#6 2
#5 5 1 2 3 4
#5 5
#7 7 1 7 7

t=int(input())
ans=[]
for tc in range(t):
     N,P = [int(i) for i in input().split(" ")]
     S = [int(i) for i in input().split(" ")]
     S.sort()
     S.reverse()
     HR=[]
     for i in range(P):
         Pi=i+P
         H=(S[i:Pi])
         hrs=0
         for j in range(len(H)-1):
             hrs+=H[0]-H[j+1]
         HR.append(hrs)
         if(Pi>P):
             break
     ans.append(min(HR))
for i in range(len(ans)):
    print("Case #" +  str(i+1) + ": " + str(ans[i]))
     
     
         
             
     