# advancement_dict = {
#   "loseInfluence": ,
#   "mot": ,
#   "motAgain": ,
#   "retire": ,

#   "playbookChange": ,

#   "burns": ,
#   "confront": ,
#   "paragon": ,
#   "maskLabel": ,
#   "drives": ,
#   "sanctuary": ,
#   "powers": ,
#   "flares": ,
#   "heart": ,
#   "abilities": ,
#   "identity": ,
#   "mentorLabel": ,
#   "resources": ,
#   "doom": ,
#   "mutate": ,
#   "lockLessons": ,
#   "mentor": ,
#   "pastParagon": ,
#   "legacy": ,
#   "joinAbilities": ,
#   "advance": ,
#   "shame": ,
#   "enhancement": ,
#   "lockSoldier": ,
#   "noAegis": ,
#   "civilian": ,
#   "future": ,
#   "depart": ,
#   "mask": ,
# }
from utils import get_moves as get_moves_json_array, get_key_and_content_from_message, get_args_from_content, format_labels, validate_labels, format_flares
from s3_utils import info_from_s3, get_s3_client, upload_to_s3, get_files_from_dir
from language_handler import get_translation
from constants import PLAYBOOK_INTERACTIONS, MOVES, PENDING_ADVANCEMENTS, PICKED, SHORT_NAME, SPECIAL, ID, PLAYBOOK, LABELS, VALUE, MAX_LABEL_VALUE, MIN_LABEL_VALUE, HEART, BULL, ROLES, ADULT, DELINQUENT, DOOMED, DOOMSIGNS, NOVA, FLARES

def add_move_from_your_playbook(message, lang):
    key, content = get_key_and_content_from_message(message)
    s3_client = get_s3_client()
    char_info = info_from_s3(key, s3_client)

    if not char_info:
        return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.no_character')

    move_name = get_args_from_content(content)

    moves_array = get_moves_json_array(lang)[MOVES]
    move_list = list(filter(lambda move_dict: move_dict[SHORT_NAME] == move_name and not move_dict[SPECIAL], moves_array))

    if not len(move_list):
        return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.no_moves_pb')

    id = move_list[0][ID]

    move = list(filter(lambda dic: dic[ID] == id, char_info[MOVES]))[0]

    if move[PICKED]:
        return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.move_already_taken')

    char_info[PENDING_ADVANCEMENTS] = char_info[PENDING_ADVANCEMENTS] - 1
    move[PICKED] = True
    upload_to_s3(char_info, key, s3_client)

    return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.successfully_added_move')(move_name)


def add_move_from_other_playbook(message, lang):
    key, content = get_key_and_content_from_message(message)
    s3_client = get_s3_client()
    char_info = info_from_s3(key, s3_client)

    if not char_info:
        return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.no_character')
    move_name = get_args_from_content(content)

    moves_array = get_moves_json_array(lang)[MOVES]
    move_list = list(filter(lambda move_dict: move_dict[SHORT_NAME] == move_name, moves_array))

    if not len(move_list):
        return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.no_moves_pb')

    move = move_list[0]

    if move[PLAYBOOK] == char_info[PLAYBOOK]:
        return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.your_playbook')

    id = move_list[0][ID]

    move = list(filter(lambda dic: dic[ID] == id, char_info[MOVES]))

    if len(move):
        return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.move_already_taken')

    char_info[PENDING_ADVANCEMENTS] = char_info[PENDING_ADVANCEMENTS] - 1
    char_info[MOVES].append({ "id": id, "picked": True })
    upload_to_s3(char_info, key, s3_client)

    return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.successfully_added_move')(move_name)


def rearrange_labels(message, lang):
    key, content = get_key_and_content_from_message(message)
    s3_client = get_s3_client()
    char_info = info_from_s3(key, s3_client)
    new_label_values = get_args_from_content(content)
    labels = char_info[LABELS]

    total_sum = 0
    new_sum = 0

    labels_do_not_exist = validate_labels(lang, labels)
    if labels_do_not_exist:
        return labels_do_not_exist

    for value in new_label_values:
        int_value = int(value)

        if int_value < MIN_LABEL_VALUE:
            return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.less_than_min')(MIN_LABEL_VALUE, int_value)

        if int_value > MAX_LABEL_VALUE:
            return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.greater_than_max')(MAX_LABEL_VALUE, int_value)

        new_sum = new_sum + int_value

    for label in labels:
        total_sum = total_sum + int(labels[label][VALUE])

    if total_sum + 1 != new_sum:
        difference = abs(new_sum - total_sum)
        if new_sum - total_sum > 0:
            direction = get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.more')
        elif total_sum == new_sum:
            difference = ''
            direction = get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.equal')
        else:
            direction = get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.less')

        return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.add_one_to_label')(difference, direction)

    index = 0
    for label in labels:
        labels[label][VALUE] = int(new_label_values[index])
        index += 1

    upload_to_s3(char_info, key, s3_client)
    return format_labels(labels, lang)
    

def get_more_bull_roles(message, lang):
    key, content = get_key_and_content_from_message(message)
    s3_client = get_s3_client()
    char_info = info_from_s3(key, s3_client)

    if char_info[PLAYBOOK] != BULL:
        return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.no_playbook')(get_translation(lang, f'playbooks.inverted_names.{BULL}'))

    new_roles = get_args_from_content(content)
    already_picked = ''
    acum = ''
    roles = char_info[HEART][ROLES]
    translated_roles = []

    for role in new_roles:
        translated_role = get_translation(lang, f'playbooks.bull.roles.titles_dict')[role]
        translated_roles.append(translated_role)

        if translated_role not in roles:
            acum += f'\n• {role}'
        elif roles[translated_role]:
            already_picked = get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.role_is_picked')(role)


    if len(acum):
        return already_picked + '\n' + get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.invalid_roles') + acum
    if already_picked:
        return already_picked

    for translated_role in translated_roles:
        roles[translated_role] = True

    upload_to_s3(char_info, key, s3_client)
    return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.successfull_update')


def add_adult_move(message, lang):
    key, content = get_key_and_content_from_message(message)
    s3_client = get_s3_client()
    char_info = info_from_s3(key, s3_client)

    if not char_info:
        return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.no_character')

    move_name = get_args_from_content(content)

    moves_array = get_moves_json_array(lang)[MOVES]
    move_list = list(filter(lambda move_dict: move_dict[SHORT_NAME] == move_name, moves_array))

    if not len(move_list):
        return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.no_moves_pb')

    move = move_list[0]

    if move[PLAYBOOK] != ADULT:
        return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.not_adult')(move_name)

    id = move_list[0][ID]

    move = list(filter(lambda dic: dic[ID] == id, char_info[MOVES]))

    if len(move):
        return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.move_already_taken')

    char_info[PENDING_ADVANCEMENTS] = char_info[PENDING_ADVANCEMENTS] - 1
    char_info[MOVES].append({ "id": id, "picked": True })
    upload_to_s3(char_info, key, s3_client)

    return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.successfully_added_move')(move_name)


def add_one_to_two_labels(message, lang):
    key, content = get_key_and_content_from_message(message)
    s3_client = get_s3_client()
    char_info = info_from_s3(key, s3_client)

    if char_info[PLAYBOOK] != DELINQUENT:
        return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.no_playbook')(get_translation(lang, f'playbooks.inverted_names.{DELINQUENT}'))

    labels_to_upgrade = get_args_from_content(content)
    labels = char_info[LABELS]

    labels_do_not_exist = validate_labels(lang, labels_to_upgrade)
    if labels_do_not_exist:
        return labels_do_not_exist

    for label_name in labels_to_upgrade:
        label_to_increase = get_translation(lang, f'inverted_labels.{label_name}')
        value = int(labels[label_to_increase][VALUE])

        if value == MAX_LABEL_VALUE:
            return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.already_max')(value, label_name)

        labels[label_to_increase][VALUE] = 1 + value

    upload_to_s3(char_info, key, s3_client)
    return format_labels(labels, lang)


def clear_doomsign(message, lang):
    key, content = get_key_and_content_from_message(message)
    s3_client = get_s3_client()
    char_info = info_from_s3(key, s3_client)

    if char_info[PLAYBOOK] != DOOMED:
        return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.no_playbook')(get_translation(lang, f'playbooks.inverted_names.{DOOMED}'))

    doomsign_og = get_args_from_content(content)

    doomsign = get_translation(lang, f'playbooks.doomed.doomsigns.accessors.{doomsign_og}')
    if not doomsign:
        return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.invalid_doomsign')(doomsign_og)

    char_doomsign = char_info[DOOMSIGNS][doomsign]
    if not char_doomsign:
        return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.doomsign_not_marked')(doomsign_og)

    char_doomsign = True
    upload_to_s3(char_info, key, s3_client)
    return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.successfull_update')


def get_burns(message, lang):
    key, content = get_key_and_content_from_message(message)
    s3_client = get_s3_client()
    char_info = info_from_s3(key, s3_client)

    if char_info[PLAYBOOK] != DOOMED:
        return get_translation(lang, f'{PLAYBOOK_INTERACTIONS}.no_playbook')(get_translation(lang, f'playbooks.inverted_names.{DOOMED}'))

    nova = info_from_s3(f'playbooks/{NOVA}', s3_client)
    char_info[FLARES] = nova[FLARES]
    upload_to_s3(char_info, key, s3_client)

    return format_flares(lang, char_info[FLARES])