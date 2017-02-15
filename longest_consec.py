def longest_consec(strarr, k):
    strarrGroups = []
    lengthCombo = []
    lengthCount = 0
    if len(strarr) < k or len(strarr) == 0 or k <= 0:
        return ''
    for combo in range(0, len(strarr), 1):
        strarrGroups.append(strarr[combo: combo + k])
    for i in range(len(strarrGroups)):
        for words in range(len(strarrGroups[i])):
            lengthCount += len(strarrGroups[i][words])
        lengthCombo.append(lengthCount)
        lengthCount = 0
    return ''.join(strarrGroups[lengthCombo.index(max(lengthCombo))])

print longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)
print longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1)
print longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2)
print longest_consec([], 3)

def longest_consec_improved(s, k):
    return max(["".join(s[i:i + k]) for i in range(len(s) - k + 1)], key=len) if s and 0 < k <= len(s) else ""