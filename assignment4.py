#TASK 1


try:
    with open('sample.txt', 'r') as file:
        for line in file:
            print(line, end='') # Use end='' to avoid double newlines
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


#TASK

file1= open('output.txt','w')
writing_file=file1.write("Hello, python!!\n")
file1.close()

file1=open('output.txt','r')
file1.close()

file1=open('output.txt','a')
appending_file=file1.write("Learning file handling in Python.")
file1.close()

file1=open('output.txt','r')
print(file1.read())
file1.close()