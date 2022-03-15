try:
    # with open("course.txt", "r") as file_var:
    #     file_lines = file_var.readlines()
    #     for line in file_lines:
    #         print(line.rstrip("\n"))
    # with open("course.txt", "w") as file_var:
    #     file_var.write("Writing from Python, line 1\n")
    #     file_var.write("Writing from Python, line 2")
    # with open("course.txt", "a") as file_var:
    #     file_var.write("Writing from Python, line 1\n")
    #     file_var.write("Writing from Python, line 2\n")
    with open("course.txt", "r+") as file_var:
        file_lines = file_var.readlines()
        for line in file_lines:
            print(line.rstrip("\n"))
        file_var.write("Writing from Python, new line\n")
        file_var.write("Writing from Python, even newer line\n")
except FileNotFoundError as file_not_found_error:
    print(file_not_found_error)
except Exception as generic_error:
    print(generic_error)
finally:
    print("This is the finally code block.")
