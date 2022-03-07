def main():
    inputs = input().split(maxsplit=2)

    number_of_exams = int(inputs[0])
    max_grade = int(inputs[1])
    required_avg = int(inputs[2])

    exam_lst = []
    for i in range(number_of_exams):
        inputs = input().split(maxsplit=1)
        
        exam_lst.append(
            (
                int(inputs[0]),
                int(inputs[1]),
            )
        )

    total_grade = sum([exam[0] for exam in exam_lst])


    ''' 
        Early checking
    '''
    if total_grade / number_of_exams >= required_avg:
        print(0)
        return
    
    
    '''
        Sort the exam list using
        number of extra essay required to increase 1 point
        
        Time: O(nlogn)
    '''
    exam_lst.sort(key=lambda x : x[1])
    
    
    '''
        Find the minimum number of essay required by
        iteratively tranverse the sorted exam list,
        correspondingly increase [extra_essay_needed] 
        and decrease [extra_point_required]
        
        Time: O(nlogn)
        Space: O(1)
    '''
    extra_point_required = required_avg * number_of_exams - total_grade
    extra_essay_needed = 0
    
    for exam in exam_lst:
        point_left_for_exam = max_grade - exam[0]
        
        if point_left_for_exam:
            extra_essay_needed += exam[1] * min(point_left_for_exam, extra_point_required)
            extra_point_required -= min(point_left_for_exam, extra_point_required)
        
        if extra_point_required == 0:
            break
            
            
    print(extra_essay_needed)
            
if __name__ == '__main__':
    main()