# fileSearch.py
# kt 10/14/22
#
#  In this code challenge you will search an email file and list all the senders of all email messages.
#  You will call the prefix@domain the sender. Your Python program will use split() to parse the
#  prefix and domain

# ** Dictionary section **
print("\n******** Python List All the Senders of All Email Messages Section ************\n")


# Create a file handle and Open the file.
file_name = "mbox-short.txt"
my_file_handle = open(file_name)

# create a counter and set to 0
# TODO: What is an accumulator and how are they used?
# Used to count the number of senders
count = 0

# Read the file line by line.
# TODO: Where did my_file_handle come from? How was it created? What is it? What is my_line?
# It came from opening the file on line 10
# It was created by declaring it and opening a file
# my_line contains the characters in a line from the file
for my_line in my_file_handle:

    # TODO: What does [0:5] mean? What is this decision control structure checking?
    # Read the first 5 characters of the line including the space
    # Decision control is checking if it contains the word "From " it will process the line
    if (my_line[0:5] == "From "):
        # TODO: What are the elements of a list? What does split() do?
        # the elements of a list are the separate words in each line
        # split() will parse the line into separate words
        sender_info = my_line.split()
        print("dir(list):")

        # TODO: What is x[1] here?
        # Displays the second word from the line
        # which contains the prefix@domain information
        print(sender_info[1])

        # TODO: What is happening here?
        # the split() will Look for @ to parse the prefix and domain
        # Part 1 is prefix - Part 2 is domain
        two_parts = sender_info[1].split('@')
        print(two_parts)

        # Create variables for prefix and domain and display it
        prefix = two_parts[0]
        domain = two_parts[1]
        print(prefix)
        print(domain)

        # TODO: Why don't we use count++?
        # Because we are not incrementing a loop just counting instances
        # count instances of sender
        count = count + 1

print("\nThere were", count, "lines in the file with 'From ' as the first word!\n\n")

# Closing the file
my_file_handle.close()

# ** Dictionary section **
print("\n******** Python Dictionary Section ************\n\n")

# Open the file.
file_name = "mbox-short.txt"
my_file_handle = open(file_name)

# TODO: Use a Python dictionary to tabulate the number of messages from each sender
num_of_sender_msgs = dict()

# Using the loop I created for prefix/domain parsing.
for my_line in my_file_handle:
    if (my_line[0:5] == "From "):
        sender_info = my_line.split()
        two_parts = sender_info[1].split('@')
        prefix = two_parts[0]
        domain = two_parts[1]
        print(prefix)
        print(domain)

        # add prefix to dictionary check if prefix already exists in dictionary
        # prefix is used as key in dictionary
        if (prefix in num_of_sender_msgs):
            print(num_of_sender_msgs[prefix], " ", prefix, " exists as key in dictionary")
            # add 1 to value representing the number of messages
            num_of_sender_msgs[prefix] = num_of_sender_msgs[prefix] + 1
        else:
            # create new key in dictionary
            num_of_sender_msgs[prefix] = 1

# Loop through dictionary to find sender with most messages
largest_count = None
largest_word = None

# TODO: What other programming language can use two variables as loop control variables?
# other languages would be C++ and Java
for my_key,my_value in num_of_sender_msgs.items():
    if largest_count is None or my_value > largest_count:
        largest_word = my_key
        largest_count = my_value

# Display the sender with the most messages
print("\nMost messages is by sender..." + largest_word + " with " + str(largest_count) + " messages")

# Display the dictionary of sender messages
print("\nThe dictionary of num_of_sender_msgs looks like:")
print(num_of_sender_msgs)

# Sort dictionary and display
print("\nDictionary sorted by keys")
print(sorted(num_of_sender_msgs.keys()))

# Sort dictionary by values and display
print("\nDictionary sorted by values")
print(sorted(num_of_sender_msgs.values()))

# Sort by key
print("\nDictionary sorted by items")
print(dict(sorted(num_of_sender_msgs.items())))


# Sort dictionary by values in descending order
print("\nDictionary sorted by values in descending order")
sort_desc = sorted(num_of_sender_msgs.items(),key=lambda x:x[1],reverse=True)
for i in sort_desc:
    print(i[0],i[1])

# Sort dictionary by values in ascending order
print("\nDictionary sorted by values in ascending order")
sort_desc = sorted(num_of_sender_msgs.items(),key=lambda x:x[1])
for i in sort_desc:
    print(i[0],i[1])

print("\nDisplaying Tuples in a dictionary:")
print("Key-Value Pairs are:")
for (myKey, myVal) in num_of_sender_msgs.items():
    print(myKey,myVal)
print("\n...and printed as tuples...sorted...ascending")
my_tuples = sorted(num_of_sender_msgs.items(),key=lambda x:x[1])
print(my_tuples)

print("\n...and printed as tuples...sorted...descending")
my_tuples = sorted(num_of_sender_msgs.items(),key=lambda x:x[1],reverse=True)
print(my_tuples)

# Closing the file
my_file_handle.close()
print("\nFile closed")


# Advanced: Use prefix@domain as the sender and the get() method in dictionary
print("\n\n******* Advanced Using the prefix@domain as the Sender and using get() ********\n")

# Open the file.
file_name = "mbox-short.txt"
my_file_handle = open(file_name)

# Counter to tabulate the number of messages from each sender
num_of_sender_msgs = dict()

# Use the loop you created for prefix/domain parsing.
for my_line in my_file_handle:
   if (my_line[0:5] == "From "):
        my_list_of_words = my_line.split()
        sender = my_list_of_words[1]

        # add item to dictionary
        # TODO: Explain how this line of code works and how it replaces the code on lines 88-95.
        # This line of code contains the prefix@domain, it is the key in the dictionary and adds 1
        # it replaces the previous code by not having to determine if it exists or not
        num_of_sender_msgs[sender] = num_of_sender_msgs.get(sender, 0) + 1

# Loop through dictionary to find sender with most messages
largest_count = None
largest_word = None

# TODO: What other programming language can use two variables as loop control variables?
# other languages would be C++ and Java
for my_key,my_value in num_of_sender_msgs.items():
    if largest_count is None or my_value > largest_count:
        largest_word = my_key
        largest_count = my_value

# Display the sender with the most messages
print("Most messages is by sender..." + largest_word + " with " + str(largest_count) + " messages")

# Display the dictionary of sender messages
print("\nThe dictionary of num_of_sender_msgs looks like:")
print(num_of_sender_msgs)

# Sort dictionary and display
print("\nDictionary sorted by keys")
print(sorted(num_of_sender_msgs.keys()))

# Sort dictionary by values and display
print("\nDictionary sorted by values")
print(sorted(num_of_sender_msgs.values()))

# Sort by key
print("\nDictionary sorted by items")
print(dict(sorted(num_of_sender_msgs.items())))

# Sort dictionary by values in descending order
print("\nDictionary sorted by values in descending order")
sort_desc = sorted(num_of_sender_msgs.items(),key=lambda x:x[1],reverse=True)
for i in sort_desc:
    print(i[0],i[1])

# Sort dictionary by values in ascending order
print("\nDictionary sorted by values in ascending order")
sort_desc = sorted(num_of_sender_msgs.items(),key=lambda x:x[1])
for i in sort_desc:
    print(i[0],i[1])


print("\nDisplaying Tuples in a dictionary:")
print("Key-Value Pairs are:")
for (myKey, myVal) in num_of_sender_msgs.items():
    print(myKey,myVal)
print("\n...and printed as tuples...sorted...ascending")
my_tuples = sorted(num_of_sender_msgs.items(),key=lambda x:x[1])
print(my_tuples)

print("\n...and printed as tuples...sorted...descending")
my_tuples = sorted(num_of_sender_msgs.items(),key=lambda x:x[1],reverse=True)
print(my_tuples)


# Closing the file
my_file_handle.close()
print("\nFile closed")

