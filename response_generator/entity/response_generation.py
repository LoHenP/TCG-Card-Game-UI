from enum import Enum

class ResponseGeneration(Enum):
    ACCOUNT_REGISTER = 1
    ACCOUNT_LOGIN = 2



    BATTLE_WAIT_QUEUE_FOR_MATCH = 11
    BATTLE_READY = 12
    CANCEL_MATCH = 13
    CHECK_BATTLE_PREPARE = 14
    WHAT_IS_THE_ROOM_NUMBER = 15
    BATTLE_DECK_LIST = 16
    BATTLE_START_SHUFFLED_GAME_DECK_CARD_LIST = 17
    CHANGE_FIRST_HAND = 18
    ROCKPAPERSCISSORS = 19
    CHECK_ROCKPAPERSCISSORS_WINNER = 20
    BATTLE_START = 21
    CHECK_OPPONENT_MULLIGAN = 22

    ACCOUNT_CARD_LIST = 31
    ACCOUNT_DECK_REGISTER = 41

    SHOP_DATA = 71
    SHOP_GACHA = 72
    FREE_GACHA = 73
    EVENT_DISTRIBUTE_CARDS = 90

    ATTACK_UNIT = 1000

    ATTACH_FIELD_ENERGY_TO_UNIT = 1003
    DEPLOY_UNIT_USAGE = 1004
    ENERGY_BOOST_SUPPORT_USAGE = 1005
    TARGET_DEATH_ITEM_USAGE = 1006
    CATASTROPHIC_DAMAGE_ITEM_USAGE = 1007
    REMOVE_OPPONENT_FIELD_ENERGY_SUPPORT_USAGE = 1008
    ADD_FIELD_ENERGY_BY_FIELD_UNIT_HEALTH_POINT_ITEM_USAGE = 1009
    ATTACH_GENERAL_ENERGY = 1010
    SEARCH_UNIT_SUPPORT_USAGE = 1011
    ATTACH_SPECIAL_ENERGY = 1012
    GENERAL_DRAW_SUPPORT_USAGE = 1013
    MULTIPLE_TARGET_DAMAGE_BY_FIELD_UNIT_SACRIFICE_ITEM_USAGE = 1014
    OPPONENT_FIElD_UNIT_ENERGY_REMOVAL_ITEM_USAGE = 1015
    ATTACK_MAIN_CHARACTER = 1016


    GAME_NEXT_TURN = 3333

    BATTLE_FINISH = 4442

    GAME_SURRENDER = 4443

    PROGRAM_EXIT = 4444

    FAKE_BATTLE_ROOM_CREATION = 8001
    FAKE_MULTI_DRAW = 8003

