
def compute_hw_average(grades):
    if len(grades) == 0:
        return 0
    if len(grades) == 1:
        return grades[0]
    return (grades[0] + grades[1]) / 2
