math = int(input("Enter Math score: "))
science = int(input("Enter Science score: "))
english = int(input("Enter English score: "))

average = (math + science + english) / 3
below_70 = sum(1 for score in [math, science, english] if score < 70)
perfect = any(score == 100 for score in [math, science, english])

if average > 75 or below_70 <= 1 or perfect:
    print("Pass")
else:
    print("Fail")
