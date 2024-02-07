# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using Classes and Separation of Concerns
#   AFH, 2/5/2024,Created Script
#   AFH, 2/5/2024,Established structure for Var, Const, Classes, Functions
#   AFH, 2/6/2024, rearranged code to form classes and functions, simplified body of code
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"
# End of Constants

# Define the Data Variables
students: list = []
menu_choice: str = ""  # Hold the choice made by the user.


# End of Variables


# Create Classes
class FileProcessor:
    """
        This Class provides reading and writing functionality to and from files

        AFH,1.6.2024
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):

        """
        This function reads data from a JSON file and stores it into a list of dictionaries

        AFH, 2/6/2024, Created function

        @param file_name: accepts string value
        @param student_data: accepts list of dictionaries
        @return: List of Dictionaries
        """

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(f"Error: There was a problem with reading the file."
                                     f"Please check that the file exists and that it is in a json format", e)
        finally:
            if not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function writes data into a JSON file from a list of dictionaries

        AFH, 2/6/2024, Created function

        @param file_name: accepts a string value
        @param student_data: accepts a list of dictionaries
        @return: No Return
        """
        try:
            file = open(file_name, "w")
            json.dump(students, file)
            file.close()
            print("The following data was saved to file!\n")
            for student in student_data:
                print(f'{student["FirstName"]},{student["LastName"]},{student["CourseName"]}')
                # Amended original print function from starter to only show data values, not a custom message
        except Exception as e:
            if not file.closed:
                file.close()
            IO.output_error_messages(f"Error: There was a problem with writing to the file."
                                     f"Please check that the file is not open by another program.", e)


class IO:
    """
    This Class contains all the functions that require either input or output by the script
    including error messages / exception handling

    AFH, 2/6/2024, Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function will display an error message to the user

        AFH, 2/6/2024, Created function

        @param message: accepts a string value
        @param error: accepts a value of type Exception
        @return: No Return
        """
        print("-- Technical Error Message -- ")
        print(message)  # Prints the custom message
        print(error.__doc__)
        print(error.__str__())

    @staticmethod
    def output_menu(menu: str):
        """
        This function provides the user with a menu of choices

        AFH, 2/6/2024, Created function

        @param menu: accepts a string value
        @return: No Return
        """
        print(menu)
        # This function seems unnecessary

    @staticmethod
    def input_menu_choice():
        """
        This function returns the user's input selection

        AFH, 2/6/2024, Created function

        @return: String value of user input
        """
        return input("What would you like to do: ")
        # This function seems unnecessary

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function requests user input and amends a list of dictionaries

        AFH, 2/6/2024, Created function

        @param student_data: accepts a list of dictionaries
        @return: No Return
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"\nYou have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("The provided value is not strictly alphabetical", e)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with your entered data", e)

    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function displays the full list of data read in from a JSON file as well as any additional
        data provided by the user

        AFH, 2/6/2024, Created function

        @param student_data:
        @return: No Return
        """
        print("-" * 50)
        print("The current active enrollments are as follow:\n")
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)


# End of Classes

# When the program starts, read the file data into a list of dictionaries
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        IO.input_student_data(student_data=students)
        continue

    # Present the current data (all active enrollments)
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

    elif menu_choice not in ("1", "2", "3", "4"):
        print("Please enter a selection of 1, 2, 3, or 4")

    else:
        break

print("Program Ended")
