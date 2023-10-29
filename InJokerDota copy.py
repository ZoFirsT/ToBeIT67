def fuckkkkkkkkkkkkkkk():
    input_string = input().strip()
    input_string = input_string.upper()

    orbs = []
    skills = {
        "QQQ": "COLD SNAP",
        "QQW": "GHOST WALK",
        "QQE": "ICE WALL",
        "WWW": "E.M.P",
        "WWQ": "TORNADO",
        "WWE": "ALACRITY",
        "EEE": "SUN STRIKE",
        "EEQ": "FORGE SPIRIT",
        "EEW": "CHAOS METEOR",
        "QWE": "DEFEANING BLAST",
    }
    invoked_skills = {"S": "", "D": ""}
    result = []

    for char in input_string:
        if char in ['Q', 'W', 'E']:
            orbs.append(char)
            while len(orbs) > 3:
                orbs.pop(0)
        elif char == 'R':
            if len(orbs) == 3:
                current_orbs = ''.join(sorted(orbs))
                if current_orbs in skills and skills[current_orbs] not in invoked_skills.values():
                    invoked_skills["D"] = invoked_skills["S"]
                    invoked_skills["S"] = skills[current_orbs]
        elif char in ['S', 'D']:
            if invoked_skills[char]:
                result.append(invoked_skills[char])

    if result:
        print(", ".join(result))
    else:
        print("EZ MID")

fuckkkkkkkkkkkkkkk()
