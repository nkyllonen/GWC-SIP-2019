'''
PY file for practicing using the school_scores library and database.
'''
import school_scores

'''
main: the function that calls other functions and gets things done
'''
def main():
    # returns all of the score data as a list
    list_of_records = school_scores.get_all()

    # 1. print out the first element
    print("list_of_records[0]:\n", list_of_records[0])

    for record in list_of_records:
        state_info = record["State"]

        # 2. print out the state name and year for each row in the data set
        print(state_info["Name"] , " (" , state_info["Code"] , ")", end="\t")

        # 3. print out the total number of test-takers for each state per year
        total_info = record["Total"]
        print(total_info["Test-takers"] , " test takers")


if __name__ == '__main__':
    main()
