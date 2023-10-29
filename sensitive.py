def sensitivity_finder(inputs):
    # Initial values
    minimum = 0
    maximum = 100
    has_upper_bound = False

    # List to store the sensitivities
    sens_values = ["100.00?"]

    for feedback in inputs:
        # Calculate the midpoint
        current_sens = (minimum + maximum) / 2
        # Add the sensitivity to the list
        sens_values.append(f"{current_sens:.2f}?")

        # Adjust based on feedback
        if feedback == "F":  # Too fast
            maximum = current_sens
            has_upper_bound = True
        elif feedback == "S":  # Too slow
            if has_upper_bound:
                minimum = current_sens
            else:
                minimum = current_sens
                maximum = 2 * current_sens

    # Add the final sensitivity to the list
    sens_values.append(f"Your sensitivity is {current_sens:.2f}.")

    return sens_values

# Sample inputs
samples = [
    (["F", "D"], ["100.00?", "50.00?", "Your sensitivity is 50.00."]),
    (["S", "F", "F", "S", "D"], ["100.00?", "200.00?", "150.00?", "125.00?", "137.50?", "Your sensitivity is 137.50."])
]

# Test the samples
for inputs, expected in samples:
    result = sensitivity_finder(inputs)
    assert result == expected, f"Expected {expected} but got {result}"
    print("\n".join(result))
    print()
