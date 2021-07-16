def def most_frequent(str):
        for i in str:
            if i in dict:
               dict[i]=dict.get(i)+1
            else:
               dict[i]=1
        sortedbyval={k: v for k, v in sorted(dict.items(),key= lamda v: v[1],reverse=true)}
        print(sortedbyval)
    str=input("enter the string ")
    dict={}
    most_frequent(str)
