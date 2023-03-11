from flyff import Flyff
import json

flyff = Flyff()


def get_items():
    s = flyff.get_items_by_ids(flyff.get_all_items())
    items = sorted(s, key=lambda item: item['id'])
    with open('items.json', 'w+') as f:
        json.dump(items, f, indent=3)


def get_monsters():
    s = flyff.get_monsters_by_ids(flyff.get_all_monsters())
    monsters = sorted(s, key=lambda item: item['level'])
    with open('monsters.json', 'w+') as f:
        json.dump(monsters, f, indent=3)


def get_skills():
    s = flyff.get_skills_by_ids(flyff.get_all_skills())
    skills = sorted(s, key=lambda item: item['id'])
    with open('skills.json', 'w+') as f:
        json.dump(skills, f, indent=3)


def get_jobs():
    s = flyff.get_classes_by_ids(flyff.get_all_classes())
    classes = sorted(s, key=lambda item: item['id'])
    with open('classes.json', 'w+') as f:
        json.dump(classes, f, indent=3)


def get_sets():
    s = flyff.get_equipment_by_ids(flyff.get_all_equipment())
    sets = sorted(s, key=lambda item: item['id'])
    with open('sets.json', 'w+') as f:
        json.dump(sets, f, indent=3)


def get_achievements():
    s = flyff.get_achievements_by_ids(flyff.get_all_achievements())
    achievements = sorted(s, key=lambda item: item['id'])
    with open('achievements.json', 'w+') as f:
        json.dump(achievements, f, indent=3)


def get_quests():
    s = flyff.get_quests_by_ids(flyff.get_all_quests())
    quests = sorted(s, key=lambda item: item['id'])
    with open('quests.json', 'w+') as f:
        json.dump(quests, f, indent=3)


def get_pk():
    s = flyff.get_pk_info()
    with open('pk.json', 'w+') as f:
        json.dump(s, f, indent=3)


def get_dungeons():
    s = flyff.get_dungeons()
    with open('dungeons.json', 'w+') as f:
        json.dump(s, f, indent=3)


def get_upgrade_bonus():
    upgrade_bonus = flyff.get_upgrade_bonus()
    with open('upgradeBonus.json', 'w+') as f:
        json.dump(upgrade_bonus, f, indent=3)


def get_npcs():
    s = flyff.get_npcs_by_ids(flyff.get_all_npcs())
    npcs = sorted(s, key=lambda item: item['id'])
    with open('npcs.json', 'w+') as f:
        json.dump(npcs, f, indent=3)


def get_skill_awakes():
    s = flyff.get_skill_awakes()
    with open('skillawakes.json', 'w+') as f:
        json.dump(s, f, indent=3)


if __name__ == '__main__':
    print("Working...")
    print("Game version: " + str(flyff.get_version()))
    # get_pk()
    # get_dungeons()
    print("Done!")
