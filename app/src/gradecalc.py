# Create a function called: calculate_avg_grade
# Parameters: the function should receive 1 parameter: a list of student objects
#             Remember a list can contain duplicates, so you can expect two student objects with same ID but different grades
# Returns: the function should return a dictionary with student ID as key and student average grade as value
#
# Example:
# input: [Student('s1',20,1824,90.5), Student('s2',21,1823,80.0), Student('s1',20,1824,70.0)]
# output: { 1824: 80.25, 1823: 80.0 }
#
# If the list of students is empty, return an empty dictionary
# Make sure that you add type hints to the function paramter and return value

from app.src.Student import Student 
from app.src.utils import avg_calc

def cal_avg_grade(student: list[Student]) -> dict[int, float]:
    if student == {}:
        return {}

    grade_dict: dict[int, list[Student]] = {}
   
    for st in student: 
        
            st_id: int = st.id
        
            if st_id in grade_dict.keys():
                grade_dict.get(st_id).append(st)
            else:
                grade_dict[st_id] = [st]

        
#        if grade_dict.get(st) == None:
#           grade_dict[st.id] = [st.grade]
#        else:
#            grade_dict[st.id].append(st.grade)        
    score_avg: dict[int, float] = {}
    for s_id, g in grade_dict.items():
        mark = [x.grade for x in g]
        print(mark) 
        score_avg[s_id] = avg_calc(mark) 
    return score_avg
