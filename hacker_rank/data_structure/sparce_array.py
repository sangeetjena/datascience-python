"""There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings.

For example, given input  and , we find  instances of ',  of '' and  of ''. For each query, we add an element to our return array, ."""


strings = ['abc','ab','bcf','ght','ab']
queries = ['ab','bcf','xcg']
dic = {}
len_array=[]
for i in strings:
    if i in dic.keys():
        dic[i] = dic[i]+1
    else:
        dic[i] = 1
for i in queries:
    if i in dic.keys():
        len_array.append(dic[i])
    else:
        len_array.append(0)
print(len_array)