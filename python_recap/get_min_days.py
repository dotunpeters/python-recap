"""Amazon Delivery Centers dispatch parcels every day. There are n delivery centers,
each having parcels[i] parcels to be delivered. On each day,
an equal number of parcels are to be dispatched from each
delivery center that has at least one parce remaining.
Find the minimum number of days needed to deliver all the parcels.
"""


from typing import List


def get_minimum_days(parcels: List[int]) -> int:
    # Write your code here
    counter = 0
    for _ in parcels:
        parcels = [x for x in parcels if x != 0]
        if len(parcels) == 0:
            break
        if len(parcels) >= 1:
            counter += 1
        parcels = [x - min(parcels) for x in parcels]
    return counter


# Test
init_parcels = [2, 3, 4, 3, 3, 6, 6, 8]
print(get_minimum_days(init_parcels))
