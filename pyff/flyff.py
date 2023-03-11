# -*- coding: utf-8 -*-

""" A python library and wrapper for the Flyff Project M API """

import requests
import logging
from pyff.exceptions import FlyffException

logger = logging.getLogger(__name__)


def normalize_list(lst):
    if isinstance(lst, list):
        lst = [str(i) for i in lst]
        lst = ",".join(lst)

    lst = lst.replace(" ", ",")
    return lst


class Flyff(object):
    """
        Example usage::

            import Flyff

            flyff = Flyff()
            print(flyff.get_all_items())
    """

    def __init__(self):
        """
        Creates an instance of the Flyff Project M API wrapper
        """
        self.prefix = "https://api.flyff.com/"
        self.version = self.get_version()

    def _get(self, url: str, headers=None, method=None):
        if not url.startswith("http"):
            url = self.prefix + url

        if not headers:
            headers = {"content-type": "application/json"}
        else:
            headers = {"content-type": headers}

        if not method:
            method = "GET"
        else:
            method = method

        try:
            response = requests.request(method, url, headers=headers)
            results = response.json()
        except requests.exceptions.HTTPError as http_error:
            response = http_error.response
            try:
                json_response = response.json()
                error = json_response.get("error", {})
                msg = error.get("message")
                reason = error.get("reason")
            except ValueError:
                msg = response.text or None
                reason = None

            logger.error("HTTP Error for GET to %s returned %s due to %s", url, response.status_code, msg)
            raise FlyffException(response.status_code, -1, "%s:\n %s" % (response.url, msg), reason)
        except ValueError:
            results = None

        return results

    def get_version(self):
        """
        Get the current data API version

        :return: The current data API version
        """
        return self._get("version/data")

    def get_all_items(self):
        """
        Get all the available item IDs

        :return: A list containing the ID of all available items
        """
        return self._get("item")

    def get_item_by_id(self, item_id):
        """
        Get information about a single item by the ID

        :param item_id: The ID of the item to search for
        :return: Information about a single item
        """
        return self._get("item/" + str(item_id))

    def get_items_by_ids(self, ids):
        """
        Get a list of items for the specified IDs

        :param ids: a list (or comma separated string) or item IDs
        :return: a list of individual items corresponding to the given IDs
        """
        ids = normalize_list(ids)
        limit = 350
        res = []

        if len(ids) > limit:
            strings = []
            s = ids.split(",")
            for n in range(0, len(s), 100):
                joined = ",".join(s[n:n+100])
                strings.append(joined)

            for string in strings:
                res += self._get("item/" + string)
        else:
            res = self._get("item/" + ids)

        return res

    def get_all_single_items(self):
        ids = self.get_all_items()
        ids = normalize_list(ids)
        return self._get("item/" + ids, method="POST")

    def get_all_classes(self):
        """
        Get all the available class IDs

        :return: all the available class IDs
        """
        return self._get("class")

    def get_class_by_id(self, class_id):
        """
        Get an individual class by the given ID

        :return: An individual class
        """
        return self._get("class/" + str(class_id))

    def get_classes_by_ids(self, ids):
        """
        Get a list of classes corresponding to the given IDs

        :param ids: A list (or comma separated string) of class IDs
        :return: A list of classes
        """
        ids = normalize_list(ids)
        return self._get("class/" + ids)

    def get_all_worlds(self):
        """
        Get a list of all available world IDs

        :return: a list of all available world IDs
        """
        return self._get("world")

    def get_world_by_id(self, world_id):
        """
        Get an individual world by the given ID

        :param world_id: The world ID
        :return: An individual world
        """
        return self._get("world/" + str(world_id))

    def get_worlds_by_ids(self, ids):
        """
        Get a list of worlds corresponding to the given IDs

        :param ids: ids: A list (or comma separated string) of world IDs
        :return: A list of worlds
        """
        ids = normalize_list(ids)
        return self._get("world/" + ids)

    def get_all_monsters(self):
        """
        Get a list of all available monster IDs

        :return: a list of all available monster IDs
        """
        return self._get("monster")

    def get_monster_by_id(self, monster_id):
        """
        Get an individual monster by the given ID

        :param monster_id: The monster ID
        :return: An individual monster
        """
        return self._get("monster/" + str(monster_id))

    def get_monsters_by_ids(self, ids):
        """
        Get a list of monsters corresponding to the given IDs

        :param ids: ids: A list (or comma separated string) of monster IDs
        :return: A list of monsters
        """
        ids = normalize_list(ids)
        return self._get("monster/" + ids)

    def get_all_equipment(self):
        """
        Get a list of all available equipment set IDs

        :return: a list of all available equipment set IDs
        """
        return self._get("equipset")

    def get_equipment_by_id(self, equipment_id):
        """
        Get an individual equipment set by the given ID

        :param equipment_id: The equipment set ID
        :return: An individual equipment set
        """
        return self._get("equipset/" + str(equipment_id))

    def get_equipment_by_ids(self, ids):
        """
        Get a list of equipment sets corresponding to the given IDs

        :param ids: ids: A list (or comma separated string) of equipment set IDs
        :return: A list of equipment sets
        """
        ids = normalize_list(ids)
        return self._get("equipset/" + ids)

    def get_all_skills(self):
        """
        Get a list of all available skill IDs

        :return: a list of all available skill IDs
        """
        return self._get("skill")

    def get_skill_by_id(self, skill_id):
        """
        Get an individual skill by the given ID

        :param skill_id: The skill ID
        :return: An individual skill
        """
        return self._get("skill/" + str(skill_id))

    def get_skills_by_ids(self, ids):
        """
        Get a list of skills corresponding to the given IDs

        :param ids: ids: A list (or comma separated string) of skill IDs
        :return: A list of skills
        """
        ids = normalize_list(ids)
        return self._get("skill/" + ids)

    def get_all_npcs(self):
        """
        Get a list of all available NPC IDs

        :return: a list of all available NPC IDs
        """
        return self._get("npc")

    def get_npc_by_id(self, npc_id):
        """
        Get an individual NPC by the given ID

        :param npc_id: The npc ID
        :return: An individual NPC
        """
        return self._get("npc/" + str(npc_id))

    def get_npcs_by_ids(self, ids):
        """
        Get a list of NPCs corresponding to the given IDs

        :param ids: ids: A list (or comma separated string) of NPC IDs
        :return: A list of NPCs
        """
        ids = normalize_list(ids)
        return self._get("npc/" + ids)

    def get_pk_info(self):
        """
        Get an object of all PK information

        :return: an object of all PK information
        """
        return self._get("pk")

    def get_all_partyskill(self):
        """
        Get a list of all available party skill IDs

        :return: a list of all available party skill IDs
        """
        return self._get("partyskill")

    def get_partyskill_by_id(self, partyskill_id):
        """
        Get an individual party skill by the given ID

        :param partyskill_id: The party skill ID
        :return: An individual party skill
        """
        return self._get("partyskill/" + str(partyskill_id))

    def get_partyskills_by_ids(self, ids):
        """
        Get a list of party skills corresponding to the given IDs

        :param ids: ids: A list (or comma separated string) of party skill IDs
        :return: A list of party skills
        """
        ids = normalize_list(ids)
        return self._get("partyskill/" + ids)

    def get_all_quests(self):
        """
        Get a list of all available quest IDs

        :return: a list of all available quest IDs
        """
        return self._get("quest")

    def get_quest_by_id(self, quest_id):
        """
        Get an individual quest by the given ID

        :param quest_id: the quest ID
        :return: An individual quest
        """
        return self._get("quest/" + str(quest_id))

    def get_quests_by_ids(self, ids):
        """
        Get a list of quests corresponding to the given IDs

        :param ids: ids: A list (or comma separated string) of quest IDs
        :return: A list of quests
        """
        ids = normalize_list(ids)
        return self._get("quest/" + ids)

    def get_all_achievements(self):
        """
        Get a list of all available achievement IDs

        :return: a list of all available achievement IDs
        """
        return self._get("achievement")

    def get_achievement_by_id(self, achievement_id):
        """
        Get an individual achievement by the given ID

        :param achievement_id: The achievement ID
        :return: An individual achievement
        """
        return self._get("achievement/" + str(achievement_id))

    def get_achievements_by_ids(self, ids):
        """
        Get a list of achievements corresponding to the given IDs

        :param ids: ids: A list (or comma separated string) of achievment IDs
        :return: A list of achievements
        """
        ids = normalize_list(ids)
        return self._get("achievement/" + ids)

    def get_upgrade_bonus(self):
        """
        Get a list of all the upgrade bonuses
        :return: a list of upgrade bonuses
        """
        return self._get("upgradelevelbonus")

    def get_skill_awakes(self):
        """
        Get a list of all the skill awakes
        :return: a list of all skill awakes
        """
        return self._get("skillawake")

    def get_pets(self):
        """
        Get a list of all the raised pets
        :return: a list of all raised pets
        """
        return self._get("raisedpet")

    def get_dungeons(self):
        """
        Get list of all dungeons
        :return: a list of all dungeons
        """
        return self._get("dungeon")
