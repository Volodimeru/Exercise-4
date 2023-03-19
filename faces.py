def main():
# Get user input
    inputfromuser = input("Please write down hello or goodbye insert emoticon at the end: ")
# call convert function
    outputconverted = convert(inputfromuser)
# print the result
    print(outputconverted)

def convert(inputfromuser):
# Replace :) for happy emoji
    inputfromuser1 = inputfromuser.replace(':)','🙂')

# Replace :( for sad emoji
    inputfromuser2 = inputfromuser1.replace(':(','🙁')
# Return string
    return inputfromuser2
main()