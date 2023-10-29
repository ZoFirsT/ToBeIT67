def validate_otp(otp):
    from collections import Counter
    
    count = Counter(otp)
    
    if len(otp) == 4:
        if list(count.values()).count(2) == 1 and len(count) == 3:
            return 'Valid'
    
    elif len(otp) == 6:
        if 4 in count.values() or (3 in count.values() and len(count) == 3):
            return 'Valid'
    
    elif len(otp) == 8:
        if 6 in count.values() or (4 in count.values() and list(count.values()).count(2) == 1):
            return 'Valid'
    
    return 'Invalid'

def main():
    otps = []
    while True:
        otp = input().strip()
        if otp == '0':
            break
        otps.append(otp)
    
    for otp in otps:
        print(validate_otp(otp))

main()
