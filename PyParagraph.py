filename = 'The Picture Of Dorian Gray - Oscar Wilde.rtf'
lines = ''
#open the file in read mode ('r') and store the contents in the variable text
with open(filename, 'r') as file:
        #stores all of the text inside a variable called "lines"
        lines = file.read()

#print the contents of the text file
print(lines)

#Approximate word count 
wc = len(lines.split(' ')) 

#Approximate sentance count 
sc = len(lines.split('.'))

#Approximate letter count per word
lc = len(lines)
lc_wc = lc / wc

#Approximate sentance length (in words) 
sl = wc / sc

#Print("Paragraph analysis") 
print("Paragraph Analysis")
print("--------------------------")
print("Approximate Word Count: " + str(wc))
print("Approximate Sentence Count: " + str(sc))
print("Average Letter Count: " + str(lc_wc))
print("Average Sentence Length: " + str(sl))