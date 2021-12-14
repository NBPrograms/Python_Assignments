#Name: Nicholas Boes (nboes)
#Date: 11/13/2019
#Section number: CSC1700 AM
#Description: Takes the list of scores, find the HW scores, display the scores, what they are, and the calculated average score

def get_scores_by_type(scores, hw):
    #Creates an empty list
    #Checks for the HW string through slicing
    #Appends to the list the HW scores
    hw_scores = []
    for grade_type in scores:
        met_type = grade_type[:2]
        if met_type == hw:
            hw_scores.append(grade_type)
    return hw_scores

def output_results(scores):
    #Finds the number of scores in the list
    #Slices for the grade string
    #Converts the grades to integers
    #Calculates the average
    #Displays the number of scores, what the scores are, and their average
    num_scores = len(scores)
    gr_sum = 0
    print(f"Got {num_scores} HW scores:", end="")
    for grade in scores:
        gr = int(grade[3:])
        gr_sum += gr
        print(f" {gr}", end="")
    avg = gr_sum / num_scores
    print(f"\nThe average HW score: {avg}")

def main():
    #All the scores
    scores = ["HW:65", "HW:75", "Exam:95", "HW:90", "HW:95", "Exam:75"]
    #Finds and puts into a list all the HW scores
    hw_scores = get_scores_by_type(scores, "HW")
    #Outputs the results
    output_results(hw_scores)
main()