B = 100
A = 10
N = 1

sum =0 
str = "QUALIFYING FOR CODE WAR IS QUITE TRICKY, DEMANDING BOTH BRILLIANCE AND AMBITION. PARTICIPANTS MUST BALANCE ANALYTICAL SKILLS AND NIMBLE PROBLEM-SOLVING, NAVIGATING THROUGH COMPLEX CHALLENGES WITH SPEED AND INNOVATION. IT'S A BATTLEFIELD REQUIRING ADVANCED CODING KNOWLEDGE, A KNACK FOR SOLVING PUZZLES, AND A DEEP PASSION FOR TECHNOLOGY. ONLY THOSE WITH THE DETERMINATION TO EXCEL AND A KEEN ABILITY TO ANALYZE AND INNOVATE CAN HOPE TO STAND OUT IN THIS COMPETITIVE ARENA."
for c in str:
    if c =='B':
        sum += 100
    elif c=='A':
        sum += 10
    elif c =='N':
        sum +=1

print(sum)