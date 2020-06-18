def ev(start, questions, lower_bound):
    # If we have no questions left to answer, we have no choice but
    # to walk away with what we started with
    if questions == 0:
        return start

    # Otherwise, calculate what our EV would be if we successfully
    # answered the next question. We would double our money, and
    # have one fewer question to answer. We'll use this to compute
    # the EVs of the current question later.
    ev_chance = ev(2 * start, questions - 1, lower_bound)

    # If we end up with a question where the probability of answering
    # is less than breakeven, we're better off walking away with what
    # we started with. If it's greater, we expect more by attempting
    # to answer the question.
    breakeven = start / ev_chance

    if lower_bound > breakeven:
        # We'll always attempt to answer. This calculation is simplified
        # by instead taking the average probability of answering the
        # question correctly. This is valid because of the uniform distribution.
        average = (lower_bound + 1.0) / 2.0
        return ev_chance * average
    else:
        # Otherwise, there are some cases where we would attempt to answer, and
        # some where we would walk away. We therefore compute the EV via
        # a weighted average.
        bail_contribution = start * (breakeven - lower_bound)
        average = (breakeven + 1.0) / 2.0
        chance_contribution = ev_chance * average * (1.0 - breakeven)
        return (bail_contribution + chance_contribution) / (1.0 - lower_bound)


while True:
    tokens = input().split()
    n, t = int(tokens[0]), float(tokens[1])
    if n == 0:
        break

    print("{:.3f}".format(ev(1, n, t)))