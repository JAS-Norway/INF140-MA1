
import hashlib
import sys

# STUDENT ID: jsu046

def userPasswordKnown(userpassword):
    """
    Takes known password userPassword.
    Returns a hash using SHA-256(userPassword).
    """
    sha256 = hashlib.sha256(userpassword)
    sha256 = sha256.hexdigest()
    # print(sha256)
    return sha256

def userPasswordBrute(*args):
    """
    Takes the hash input from the know password.
    Checks "uuudddd", where:
    u = upper case letter (A-Z) (65, 90)
    d = random number (0-9)
    Returns string uuudddd when userHASH is found.
    """
    print("Working.", end="")
    sys.stdout.flush()
    foundPasswords = {}
    userHashList = []
    for x in args:
        userHashList.append(x)

    uLim = 91
    dLim = 10

    u1 = 65
    u2 = 65
    u3 = 65
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0

    count = 0
    foundCount = 1

    while(len(userHashList) > 0):
        u1Str = chr(u1)
        u2Str = chr(u2)
        u3Str = chr(u3)
        d1Str = str(d1)
        d2Str = str(d2)
        d3Str = str(d3)
        d4Str = str(d4)
        inputString = (u1Str+u2Str+u3Str+d1Str+d2Str+d3Str+d4Str).encode("utf-8")

        sha256 = hashlib.sha256(inputString)
        sha256 = sha256.hexdigest()

        if sha256 in userHashList:
            
            for x in range(len(args)):
                if args[x] == sha256:
                    foundPasswords.update({f"Password{x+1}": inputString})

            userHashList.remove(sha256)
            print(f"\nHash found ({foundCount}/{len(args)}).", end="")
            sys.stdout.flush()
            foundCount += 1
            continue

        u1 += 1
        if u1 == uLim:
            u1 = 65
            u2 += 1
        if u2 == uLim:
            u2 = 65
            u3 += 1
        if u3 == uLim:
            u3 = 65
            d1 += 1
        if d1 == dLim:
            d1 = 0
            d2 += 1
        if d2 == dLim:
            d2 = 0
            d3 += 1
        if d3 == dLim:
            d3 = 0
            d4 += 1
        if d4 == dLim:
            return "No solutions found."
        
        count += 1
        if count % 1000000 == 0:
            count = 0
            print(".", end="")
            sys.stdout.flush()
    print()
    return foundPasswords

print("u = upper case letter (A-Z)")
print("d = random number (0-9)")
pass1 = input("Enter password1 uuudddd: ").encode("utf-8")
pass2 = input("Enter password2 uuudddd: ").encode("utf-8")
pass3 = input("Enter password3 uuudddd: ").encode("utf-8")

userPasswordHASH1 = userPasswordKnown(pass1)
userPasswordHASH2 = userPasswordKnown(pass2)
userPasswordHASH3 = userPasswordKnown(pass3)

userPasswordHASHGuess = userPasswordBrute(
    userPasswordHASH1, 
    userPasswordHASH2, 
    userPasswordHASH3
)

print(userPasswordHASHGuess)
