# Calculate grade of five subjects.
try:
    subjects = []
    for i in range(1, 6):
        e = float(input(f"Enter the #{i} subject : "))
        if e > 100 or e < 0:
            raise ValueError("Subject's score must be within 0 and 100")
        subjects.append(e)
    print(f"Average marks : {sum(subjects) / len(subjects)}")

except ValueError as err:
    print(err)
