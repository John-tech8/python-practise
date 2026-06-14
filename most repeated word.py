file=open("sample.txt","r")
data=file.read()
input=data.split()
freq={}
for word in input:
    if word  in freq:
        freq[word]+=1
    else:
        freq[word]=1
max_word=max(freq,key=freq.get)
print(f"Most Frequent word:{max_word}")
print(f"frequency is {freq[max-word]}")
