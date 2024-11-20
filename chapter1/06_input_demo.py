name = input("Enter your name: ")
is_student = input("Are you a student? (yes/no)").lower() == "yes"

print(f"name: {name}")
print(f"is_student: {is_student}")

if is_student:
    print(f"welcome student {name}")
else:
    print(f"{name} you are not a student")
