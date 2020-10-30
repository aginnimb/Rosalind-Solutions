#Rosalind TREE List

# 1ST
from collections import Counter
file = open("/Users/anu/Downloads/rosalind_dna.txt", "r")
st = (file.readline())
# print(st)
counter = Counter(st)
print(counter["A"],"",counter["C"],"",counter["G"],"",counter["T"])

#2ND
file = open("/Users/anu/Downloads/rosalind_rna.txt", "r")
st = (file.readline())
print(st)
print(st.replace("T","U"))

#3RD
import string
from Bio.Seq import Seq

def reverse(x):     #function to reverse the string
	return x[::-1] 

file = open("/Users/anu/Downloads/rosalind_revc.txt", "r") #open
org = file.readline() #reading file
seg = Seq(org) #calling Seq function to read the sequence
rev_comp = seg.reverse_complement() # generating reverse complimentary

print("1:" + org)
print("2:" + reverse(org))
print("3:" + rev_comp)
# print (seg.transcribe()) #transcribes the seq
# print (seg.translate()) #translates the seq
