from itertools import permutations

def fuckProblem(active_orbs):
    skill_map = {
        "QQQ": "COLD SNAP",
        "QQW": "GHOST WALK",
        "QQE": "ICE WALL",
        "WWQ": "TORNADO",
        "WWW": "E.M.P",
        "WWE": "ALACRITY",
        "EEQ": "FORGE SPIRIT",
        "EEW": "CHAOS METEOR",
        "EEE": "SUN STRIKE"
    }
    
    orbs_strs = [''.join(permutation) for permutation in permutations(active_orbs)]
    for orbs_str in orbs_strs:
        if orbs_str in skill_map:
            return skill_map[orbs_str]
    return None

def main():
    sequence = input().strip()
    active_orbs = []
    active_skills = ["", ""]
    result = []

    for char in sequence:
        if char in ['Q', 'W', 'E']:
            active_orbs.append(char)
            if len(active_orbs) > 3:
                active_orbs.pop(0)
        elif char == 'R':
            skill = fuckProblem(active_orbs)
            if skill and skill not in active_skills:
                active_skills.insert(0, skill)
                active_skills.pop()
        elif char == 'S':
            if active_skills[0]:
                result.append(active_skills[0])
        elif char == 'D':
            if active_skills[1]:
                result.append(active_skills[1])

    if result:
        print(', '.join(result))
    else:
        print("EZ MID")

if __name__ == "__main__":
    main()
