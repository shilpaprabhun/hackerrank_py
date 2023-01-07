
import re
def fun(s):
    #pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    pat = r'\b[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Z|a-z]{1,3}\b'
    if re.match(pat,s):
        return True
    else:
        return False
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)