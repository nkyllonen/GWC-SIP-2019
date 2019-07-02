import json, os.path

def ask_survey(questions, keys):
    # Create the dictionary to store the responses.
    answers = {}
    print("New entry! Please answer the questions below.")

    # Iterate over the list of survey questions and take in user responses.
    for x in range(len(questions)):
        response = input(questions[x] +":     ")
        answers[keys[x]] = response

    return answers

'''
output_to_file:
    list_of_answers(list)   :   list of dictionaries
    filename(str)           :   string containing the file name
'''
def output_to_file(list_of_answers, filename):
    # collect all of the old data if this file already exists
    if os.path.isfile(filename):
        with open(filename, 'r') as json_file:
            old_data = json.load(json_file)
        print("\n old: " , old_data)
        list_of_answers = old_data + list_of_answers

    # output all of the new data to the file
    with open(filename, 'w') as json_file:
        json_file.write('[\n')
        line = 0
        for entry in list_of_answers:
            json.dump(entry, json_file)
            if (line < len(list_of_answers) - 1):
                json_file.write(',\n')
            else:
                json_file.write('\n')
            line += 1
        json_file.write(']')

    # if os.path.isfile("allanswers.json"):
    #     f = open("allanswers.json", "r")
    #     olddata = json.load(f)
    #     list_of_answers.extend(olddata)
    #     f.close()
    #
    # # Reopen the file in write mode and write each entry in json format.
    # f = open("allanswers.json", "w")
    # f.write('[\n')
    # index = 0
    # for t in list_of_answers:
    #     if (index < len(list_of_answers)-1):
    #         json.dump(t, f)
    #         f.write(',\n')
    #     else:
    #         json.dump(t, f)
    #         f.write('\n')
    #     index += 1
    #
    # f.write(']')
    # f.close()

def main():
    # Create a list of survey questions and a list of related keys that
    # will be used when storing survey results.
    survey = [
        "What is your name?",
        "How old are you?",
        "What is your hometown?",
        "What is your date of birth? (DD/MM/YYYY)"]
    keys = ["name", "age", "hometown", "DOB"]

    # Create a list that will store each person's individual survey responses.
    list_of_answers = []

    done = "NO"
    while done == "NO":

        answers = ask_survey(survey, keys)
        list_of_answers.append(answers)
        done = input("Are you done collecting information? Type YES or NO.     ").upper()

    # Print the list of dictionaries.
    print(list_of_answers)

    output_to_file(list_of_answers, "survey_answers.json")

if __name__ == "__main__":
    main()
