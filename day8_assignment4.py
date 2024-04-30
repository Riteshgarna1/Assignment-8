# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# num = int(input("Enter a non-negative integer: "))
# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     print("Factorial of", num, "is", factorial(num))




# def count_words_in_file(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             for line_num, line in enumerate(file, start=1):
#                 words = line.split()
#                 num_words = len(words)
#                 print(f"Line {line_num}: {num_words} words")
#     except FileNotFoundError:
#         print("File not found!")

# # Change this to the path of your text file
# file_path = r"C:\Users\prana\Desktop\Data Science WIth AI & ML\jecrc\sample_text.txt"

# count_words_in_file(file_path)





# def find_max_min(numbers):
#     max_num = numbers[0]
#     min_num = numbers[0]
#     for num in numbers:
#         if num > max_num:
#             max_num = num
#         if num < min_num:
#             min_num = num
#     return max_num, min_num


# numbers = [3, 1, 8, 5, 2]
# max_num, min_num = find_max_min(numbers)
# print("Maximum number:", max_num)
# print("Minimum number:", min_num)





# def find_longest_word(words):
#     longest_word = ""
#     for word in words:
#         if len(word) > len(longest_word):
#             longest_word = word
#     return longest_word


# word_list = ["apple", "banana", "orange", "kiwi", "strawberry"]
# longest_word = find_longest_word(word_list)
# print("Longest word:", longest_word)