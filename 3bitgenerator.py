class RuleSets:
    def __init__(self):
        self.ruleset = []


def generateRule(n, arr, i, rules):
    if i == n:
        rule = [str(i) for i in arr]
        rules.ruleset.append(rule)
        return

    arr[i] = 0
    generateRule(n, arr, i + 1, rules)
    arr[i] = 1
    generateRule(n, arr, i + 1, rules)
    arr[i] = 2
    generateRule(n, arr, i + 1, rules)


if __name__ == "__main__":
    n = 8
    arr = [None] * n
    rules = RuleSets()

    generateRule(n, arr, 0, rules)

    print(rules.ruleset)
