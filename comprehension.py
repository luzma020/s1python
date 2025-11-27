
given_list = [-5, 10, -3, 8, 2, -1, 0, 9]
positive_numbers = [num for num in given_list if num > 0]
print(f"Positive numbers: {positive_numbers}")


n = 5
squared_numbers = [i**2 for i in range(1, n + 1)]
print(f"Squares of the first {n} numbers: {squared_numbers}")


word = "programming"
vowels = [char for char in word if char.lower() in 'aeiou']
print(f"Vowels in '{word}': {vowels}")


given_word = "python"
ordinal_values = [ord(char) for char in given_word]
print(f"Ordinal values of '{given_word}': {ordinal_values}")