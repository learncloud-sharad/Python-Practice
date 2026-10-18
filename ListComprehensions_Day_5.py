### Vowel Counter

sentence = "The quick brown fox jumps over the lazy dog"
vowel_counts = []
for char in sentence:
    if char in 'aeiou':
        vowel_counts.append(1)
print(vowel_counts)
print(f"Total number of vowels: {sum(vowel_counts)}")

print("\n Another Way :")
#

vowel_counter = [1 for  char in sentence if char in 'aeiou']
print(sum(vowel_counter))