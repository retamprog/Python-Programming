# numbers=[5,2,5,2,2]
# for x in numbers:
#     for y in range(0,x):
#         print('x',end='')
#     print('')
# names=['Retake','Prince','Architect','Soulmate Bioswale']
# for x in names:
#     print(x,end=",")
# Bubble sort
numbers = [18, 45, 67, 89, 90, 23, 56]
# we will do simple bubble sort in this program
for i in range(0, len(numbers)-1):
    for j in range(0, len(numbers)-i-1):
        if numbers[j] > numbers[j+1]:
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp

print(numbers)
