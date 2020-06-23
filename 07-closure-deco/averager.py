def make_averager():
    # Free variable
    series = []

    # This is an inner function
    def averager(new_value: float) -> float:
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager


def make_averager_with_nonlocal():
    count = 0
    total = 0
    
    def averager(new_value: float) -> float:
        nonlocal count, total
        '''
        Without nonlocal declaration, count and total is treated as local
        variables because of the assignments. In the example above, series
        is never assigned which works fine.
        '''
        count += 1
        total += new_value
        return total / count
    
    return averager
