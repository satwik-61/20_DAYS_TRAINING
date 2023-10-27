s1 = input()
n = int(input())
n = n % len(s1)
Map = {}  # Index : Symbol
s = '[@_!#$%^&*()<>?/\|}{~:],'

# Initialize a dictionary to store special characters and spaces at their respective positions
for i in range(len(s1)):
    if s1[i] == " " or s1[i] in s:
        Map[i] = s1[i]

# Remove non-alphanumeric characters and spaces from the input string
s3 = ''.join(c for c in s1 if c.isalnum() or c.isspace())

# Reverse the words based on input word length
l1 = list(s3.split())
l1.sort(key=len, reverse=True)

s2 = ''.join(l1)
s2 = s2[n:] + s2[:n]

# Reconstruct the final string with special characters and spaces
output = ""
i = 0
for char in s1:
    if i in Map:
        output += Map[i]
    output += char
    i += 1

print(output)
