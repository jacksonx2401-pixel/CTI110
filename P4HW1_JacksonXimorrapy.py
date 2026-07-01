#Ximorra Jackson
#07/01/26
#PHW1
# In this assignment teaches us how to use lists and loops to store and process user input.

scores = []
num_scores = int(input("How many scores do you want to enter? "))

i = 0
while i < num_scores:
    score = float(input(f"Enter score {i + 1}: "))
    
    if score < 0 or score > 100:
        print("Invalid score entered! Score should be between 0 and 100.")
        print(f"Enter score #{i + 1} again.")
        continue
        

print("\n----------------Results-------------------")

if scores:
    lowest = min(scores)
    average = sum(scores) / len(scores)
    scores.remove(lowest) # Remove the lowest score from the list

    # Determine letter grade (Added quotes here)
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print(f"{'Lowest score:':<20} {lowest:>5.2f}")
    print(f"{'Modified List:':<20} {scores}")
    print(f"{'Scores Average:':<20} {average:>5.2f}")
    print(f"{'Grade:':<20} {grade}")
    print("----------------------------------------------------")

