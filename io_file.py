# Tutorial and exercises for file interaction with Python

try:
    file_var = open("course.txt")  # save content of file in local variable
    file_lines = file_var.readlines()  # read content of variable line by line
    # print(file_lines)  # print all lines
    for line in file_lines:
        print(line.strip("\n"))
except FileNotFoundError as file_not_found_error:
    print(file_not_found_error)
except Exception as generic_error:
    print(generic_error)
finally:
    file_var.close()
    print("This is the finally code block.")
