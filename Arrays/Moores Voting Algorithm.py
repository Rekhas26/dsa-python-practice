def majority_element(arr):
    candidate = None
    count = 0

    # Step through the array
    for num in arr:
        if count == 0:
            candidate = num  # Start a new candidate
        if num == candidate:
            count += 1  # Increment if it matches the candidate
        else:
            count -= 1  # Decrement if it doesn't match the candidate

    return candidate

# Test
arr = [2, 2, 1, 1, 2, 2, 2]
print(majority_element(arr))  # Output: 2



Understanding Moore’s Voting Algorithm
The key observation here is that the majority element will appear more times than all other elements combined. So if we can "vote" and eliminate non-majority candidates step-by-step, we can identify the majority element efficiently.

Step-by-Step Explanation of the Algorithm
Start with the assumption that the first element is the majority.

Traverse through the array:

If the current element is the same as the candidate, increase the count (we "vote" for the candidate).

If the current element is different, decrease the count (the candidate loses a vote).

When the count becomes 0, change the candidate to the current element (as this element has more votes now).

In the end, the candidate will be the majority element.

How Does It Work?
Let’s see a step-by-step walkthrough with the example:

Example: arr = [2, 2, 1, 1, 2, 2, 2]
Initialization:
candidate = None, count = 0 (We don't have a candidate yet, and the count is 0).

Iteration 1:
Element = 2.

count = 0, so set candidate = 2, count = 1.

Now, candidate = 2, count = 1.

Iteration 2:
Element = 2.

candidate = 2, so increase count → count = 2.

Iteration 3:
Element = 1.

candidate = 2, count = 2.

Since 1 != candidate, decrement count → count = 1.

Iteration 4:
Element = 1.

candidate = 2, count = 1.

Since 1 != candidate, decrement count → count = 0.

count = 0, so change candidate = 1, count = 1.

Iteration 5:
Element = 2.

candidate = 1, count = 1.

Since 2 != candidate, decrement count → count = 0.

count = 0, so change candidate = 2, count = 1.

Iteration 6:
Element = 2.

candidate = 2, count = 1.

candidate = 2, so increase count → count = 2.

Iteration 7:
Element = 2.

candidate = 2, count = 2.

candidate = 2, so increase count → count = 3.

Final Result:
After traversing the entire array, the candidate = 2 and count = 3.

Since 2 appears more than n/2 = 7/2 = 3.5 times, 2 is the majority element.

Code Implementation
Here is the code for Moore’s Voting Algorithm:

python
Copy
Edit
def majority_element(arr):
    candidate = None
    count = 0

    # Step through the array
    for num in arr:
        if count == 0:
            candidate = num  # Start a new candidate
        if num == candidate:
            count += 1  # Increment if it matches the candidate
        else:
            count -= 1  # Decrement if it doesn't match the candidate

    return candidate

# Test
arr = [2, 2, 1, 1, 2, 2, 2]
print(majority_element(arr))  # Output: 2
Why Does This Work?
Key Insight: The majority element outnumbers all other elements combined.

When traversing the array, we effectively cancel out pairs of elements that aren't the majority, leaving the majority element as the surviving candidate.
