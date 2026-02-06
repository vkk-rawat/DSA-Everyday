"understand the problem first then solve and go for understanding"


def kokoEat(arr, k):
    mx = max(arr)

    for speed in range(1, mx + 1):

        reqTime = 0
        for i in range(len(arr)):

            # time required to eat this pile
            # of bananas at current speed
            reqTime += \
                (arr[i] + speed - 1) // speed

        # if total eating time at current speed
        # is smaller than given time
        if reqTime <= k:
            return speed

    return mx


if __name__ == "__main__":
    arr = [5, 10, 3]
    k = 4
    print(kokoEat(arr, k))
