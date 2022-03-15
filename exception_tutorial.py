try:
    file_var = open("course.txt")
    a = 5 / 0
except FileNotFoundError as file_not_found_error:
    print("Please create the file first.")  # print custom error message
    print(file_not_found_error)             # print default exception error message
except ZeroDivisionError as zero_division_error:
    print("You can not divide by zero.")
    print(zero_division_error)
except Exception as ex:
    print("A error happened.")
    print(ex)
finally:
    print("This is the finally code.")
print("End of file.")
