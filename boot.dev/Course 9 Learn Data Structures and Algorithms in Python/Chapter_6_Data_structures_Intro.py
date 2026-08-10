#lesson 1
def count_marketers(job_titles):
    count = 0
    for i in job_titles:
        if "marketer" == i.lower():
            count += 1
    return count

#lesson 4
def last_work_experience(work_experiences):
    if work_experiences == []:
        return None
    return work_experiences[-1]