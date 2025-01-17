en = {
  "embed_commands_dict": {
    "mot": "mot",
    "celebrate": "celebrate",
    "triumph": "celebrate",
    "weakness": "weakness",
    "vulnerability": "weakness",
    "weak": "weakness",
    "playbooks": "playbooks"
  },
  "generic_playbook_dict": {
    "lock": "lock",
    "editlabels": "editlabels",
    "potential": "potential",
    "removepotential": "removepotential",
    "markcondition": "markcondition",
    "clearcondition": "clearcondition",
    "create": "create",
    "labels": "labels",
    "conditions": "conditions",
    "get_potential": "get_potential",
    "pending_advancements": "pending_advancements",
    "advancements": "advancements",
    "print": "print",
    "deletecharacter": "deletecharacter",
    "replicate": "replicate",
    "el": "editlabels",
    "cc": "clearcondition",
    "mc": "markcondition"
  },
  "settings_dict": {
    "helphere": "helphere",
    "settings": "settings",
    "changesettings": "change_settings",
    "language": "language",
    "teamname": "teamname",
    "dicedisplay": "dicedisplay",
    "updatelang": "update_lang",
    "updategm": "update_gm",
    "updateteamname": "update_teamname",
    "createsettings": "create_settings",
    "deletesettings": "delete_settings",
    "team": "add_team",
    "spend": "spend_team",
    "pool": "check_team",
    "empty": "empty_team",
    "dicetoggle": "toggle_dice"
  },
  "generic_advancements_dict": {
    "mov_my_playbook": "mov_my_playbook",
    "mov_other_playbook": "mov_other_playbook",
    "rearrange": "rearrange"
  },
  "playbook_specific_advancements_dict": {
    "more_roles": "more_roles",
    "add_adult": "add_adult",
    "more_to_labels": "more_to_labels",
    "clear_sign": "clear_sign",
    "mark_sign": "mark_sign",
    "get_burns": "get_burns",
    "mask_label": "mask_label",
    "get_drives": "get_drives",
    "get_sanctuary": "get_sanctuary",
    "more_flares": "more_flares",
    "get_heart": "get_heart",
    "get_mask": "get_mask",
    "mentor_label": "mentor_label",
    "more_resources": "more_resources",
    "get_mentor": "get_mentor",
    "get_legacy": "get_legacy",
    "lock_soldier": "lock_soldier"
  },
  "dice_rolling": {
    "calculation_title": "Calculation",
    "calculation": lambda result1, result2, mod, calc: f"Dice **{result1}** + **{result2}**, Modifier {mod} **{calc}**",
    "dice": "Dice",
    "label": lambda label_name, label_value: f"**{label_name}** is **{label_value}**\n",
    "result": "Result",
    "condition_text": lambda condition, name: f"-2 as **{name}** is **{condition}**!\n",
    "conditions_marked": lambda conditions, name: f"**{name}** has {conditions} conditions marked!\n",
    "command_modifier": lambda mod: f"Modifier from command is **{mod}**\n"
  },
  "description": "Description",
  "moves": {
    "moves": "moves",
    "adult": "adult",
    "non_existent_playbook_intro": "Sorry, I couldn't find that playbook, the available playbooks are:",
    "non_existent_playbook_end": "\nType an exclamation sign and one of the names in lowercase and without the 'The', moves or adult\ne.g.: !beacon, !moves, !adult",
    "moves_plus": {
      "response_header": "**Name - description, keyword, label**\n"
    }
  },
  "playbook_interactions": {
    "fail_preffix": "Oh no, ",
    "already_locked": lambda label_name: f"Oh no, {label_name} is already locked!",
    "is_locked": lambda label_name: f"Oh no, {label_name} is locked, this one can't change!",
    "labels_base": "Your labels are:\n",
    "up": "up",
    "down": "down",
    "value_is_in_border": lambda value, label_name, direction: f"Oh no, with a value of {value}, your {label_name} can't go {direction}! You get a condition!",
    "locked": "[LOCKED]",
    "condition_not_marked": "You don't have any condition marked",
    "youre": "You are:\n",
    "dont": "don't ",
    "condition_status": lambda status: f"Oh, you {status}have that condition marked.",
    "no_character": "I'm sorry but it appears you have no character created",
    "existing_character": "I'm sorry but it appears you already have character created in this channel",
    "invalid_condition": lambda condition_name: f"Oh no, {condition_name} is not a valid condition",
    "different_labels": "The labels must be different",
    "congrats_pending_advancements": lambda adv_count: f"Nice, you can now do {adv_count} advancements",
    "congrats_potential": lambda potential: f"Nice, you have {potential} potential marked",
    "no_template": lambda playbook_name: f"It seems I don't have a template for a playbook called {playbook_name}",
    "congrats_on_creation": lambda char, playbook: f"Congratulations {char}, The {playbook} on joining the team!",
    "potential": lambda potential: f"You have {potential} potential marked",
    "nopotential": "Sorry, you have no potential marked",
    "basic": "\nBasic:",
    "advanced": "\nAdvanced:",
    "taken": "[TOMADO] ",
    "pending_advancements": lambda adv_count: f"You can do {adv_count} advancements",
    "no_moves_pb": "I'm sorry, but there are no moves from your playbook that match that name",
    "no_moves": "I'm sorry, but there are no moves that match that name",
    "move_already_taken": "You already have this move, choose another one",
    "successfully_added_move": lambda move_name: f"Nice, you can now use the move {move_name}",
    "your_playbook": "You can't add a move from your playbook with this advancement",
    "more": "more",
    "less": "less",
    "equal": "equal",
    "add_one_to_label": lambda difference, direction: f"You should add one to a label, the difference with these values has {difference} {direction} than the original sum",
    "less_than_min": lambda min_allowed, intended: f"I'm sorry, but {intended} is not a valid label value. The minimum is {min_allowed}",
    "greater_than_max": lambda max_allowed, intended: f"I'm sorry, but {intended} is not a valid label value. The maximum is {max_allowed}",
    "no_playbook": lambda name: f"To take this advancement you must have one of the following playbooks:{name}",
    "invalid_roles": "The valid roles are: defender, friend, listener and enabler. The following ones are invalid:",
    "successfull_update": "The update was successfull",
    "role_is_picked": lambda role: f"The role {role} has already been chosen, you must pick two new ones",
    "not_adult": lambda name: f"The move {name} is not adult",
    "already_max": lambda value, name: f"The {name} label already has the max value ({value})",
    "invalid_label": lambda name: f"The label {name} does not exist. ",
    "invalid_doomsign": lambda doomsign: f"The doomsign {doomsign} does not exist, the valid ones are visions, infinite, portal, bright, bolstered and perish",
    "doomsign_not_marked": lambda doomsign: f"The doomsign {doomsign} must be marked to be cleared",
    "doomsign_marked": lambda doomsign: f"The doomsign {doomsign} has been marked",
    "already_mask_label": lambda label_name: f"The label {label_name} is already your mask label, you must choose a new one",
    "already_have": lambda name: f"You already have {name}",
    "invalid_flares": "The valid flares are: storm, shield, constructs, moat, worship, move, boost, overcharge, elemental and snatch. The following ones are invalid:",
    "flare_is_picked": lambda name: f"The flare {name} has already been chosen, you must pick three new ones",
    "not_exactly_three_flares": lambda current_count: f"You must choose 3 new flares, not {current_count}",
    "invalid_label_type": lambda invalid_name: f"The options are embodies and denies, {invalid_name} isn't a valid option",
    "max_mentor_label_value": lambda name, current_value: f"The label {name} must have a value of 1 or less for the change to be valid, not {current_value}",
    "invalid_resource": lambda name: f"You can't have a {name} as a resource, the valid ones are:",
    "resource_already_acquired": "You already have the following resources:",
    "more_than_four_resources": lambda max_count, wanted_count: f"The maximum ammount of resources to add with this advancement is {max_count}, not {wanted_count}",
    "character_deletion": lambda char, playbook: f"Goodbye {char}, the {playbook} - You have deleted your character in this channel.",
    "character_replication": lambda char, playbook: f"Successfully replicated {char}, the {playbook}.  This character now exists in 2 places at once."
  },
  "labels": {
    "danger": "danger",
    "freak": "freak",
    "superior": "superior",
    "savior": "savior",
    "mundane": "mundane",
    "soldier": "soldier"
  },
  "inverted_labels": {
    "danger": "danger",
    "freak": "freak",
    "superior": "superior",
    "savior": "savior",
    "mundane": "mundane",
    "soldier": "soldier"
  },
  "conditions": {
    "afraid": "afraid",
    "angry": "angry",
    "guilty": "guilty",
    "hopeless": "hopeless",
    "insecure": "insecure",
    "damaged": "damaged"
  },
  "inverted_conditions": {
    "afraid": "afraid",
    "angry": "angry",
    "guilty": "guilty",
    "hopeless": "hopeless",
    "insecure": "insecure",
    "damaged": "damaged"
  },
  "configuration": {
    "settings": "Settings\n",
    "language": "Language",
    "teamname": "Team name",
    "gm": "GM",
    "customNames": "Custom names",
    "dicetoggle": "Dice toggle",
    "no_file": "This chat doesn't have a configuration file. To create it write the following command:\n!createsettings en\nif you wish for it to be in english.\n",
    "existing_settings": "This chat already has a configuration file.",
    "successfull_update": "The update was successful",
    "successfull_creation": "The configuration file has been created",
    "successfull_deletion": "The configuration file has been deleted",
    "invalid_lang": lambda lang: f"{lang} is not a valid language, the options are: en (english), es (spanish)",
    "gm": "GM",
    #"team_pool": lambda team: f"You have {team} in the team pool",
    "team_pool": lambda team: f"You have {team} in the team pool",
    "insufficient_team": "You don't have enough team for that!",
    "dicedisplay": "dicedisplay",
    "dicedisplayswitched": lambda dice: f"Dice display toggled, currently set to {dice}"
  },
  "playbooks": {
    "the": "The",
    "list": ['beacon', 'bull', 'delinquent', 'doomed', 'janus', 'legacy', 'nova', 'outsider', 'protege', 'transformed', 'brain', 'harbinger', 'innocent', 'joined', 'newborn', 'nomad', 'reformed', 'scion', 'soldier', 'star'],
    "names": {
      "beacon": "beacon",
      "bull": "bull",
      "delinquent": "delinquent",
      "doomed": "doomed",
      "janus": "janus",
      "legacy": "legacy",
      "nova": "nova",
      "outsider": "outsider",
      "protege": "protege",
      "transformed": "transformed",
      "brain": "brain",
      "harbinger": "harbinger",
      "innocent": "innocent",
      "joined": "joined",
      "newborn": "newborn",
      "nomad": "nomad",
      "reformed": "reformed",
      "scion": "scion",
      "soldier": "soldier",
      "star": "star"
    },
    "inverted_names": {
      "beacon": "beacon",
      "bull": "bull",
      "delinquent": "delinquent",
      "doomed": "doomed",
      "janus": "janus",
      "legacy": "legacy",
      "nova": "nova",
      "outsider": "outsider",
      "protege": "protege",
      "transformed": "transformed",
      "brain": "brain",
      "harbinger": "harbinger",
      "innocent": "innocent",
      "joined": "joined",
      "newborn": "newborn",
      "nomad": "nomad",
      "reformed": "reformed",
      "scion": "scion",
      "soldier": "soldier",
      "star": "star"
    },
    "playbooks": "Playbooks",
    "available": "Available Playbooks are - ",
    "playbook_re": r"![a-z]+ ([a-z]+)",
    #"celebrate_re": r"!celebrate ([a-z]+)",
    #"weakness_re": r"!weakness ([a-z]+)",
    "moment_of_truth": "MOMENT OF TRUTH",
    "celebrate": "Triumphant Celebration",
    "weakness": "Vulnerability or Weakness",
    "this_is_mot": lambda usr: f"This is {usr}'s moment!",
    "this_is_celebrate": lambda usr: f"{usr} celebrates a triumph!",
    "this_is_weakness": lambda usr: f"{usr} opens up and shares!",
    "advances": {
      "moveYouPlaybook": "Take another move from your playbook",
      "moveOtherPlaybook": "Take a move from another playbook",
      "loseInfluence": "Someone permanently loses Influence over you; add +1 to a Label",
      "rearrange": "Rearrange your Labels as you choose, and add +1 to a Label",
      "mot": "Unlock your Moment of Truth",
      "moreRoles": "Choose another two roles for the Bull's Heart",
      "motAgain": "Unlock your Moment of Truth after it's been used once",
      "playbookChange": "Change playbooks",
      "adult": "Take an adult move",
      "lock": "Lock a Label and add +1 to a Label your Choice",
      "retire": "Retire from the life or become a paragon of the city",
      "plusOne": "Add +1 to any two Labels",
      "clear": "Clear a doomsign; you lose access to that move for now",
      "burns": "Get burn and three flares (from the Nova's playbook)",
      "confront": "Confront your doom on your terms; if you survive, change playbooks",
      "paragon": "Become a paragon of the city for however long you have left",
      "maskLabel": "Change your mask's Label; add +1 to your new mask's Label",
      "drives": "Take drives from the Beacon's playbook",
      "sanctuary": "Take a Sanctiary from the Doomed playbook",
      "powers": "Unlock the remaining two powers of your suite",
      "flares": "Unlock three new flares",
      "heart": "Take The Bull's Heart from the Bull playbook",
      "abilities": "Choose two new abilities from any playbook as you come into your own",
      "identity": "You adopt a human life, take Secret Identity and The Mask from the Janus playbook",
      "mentorLabel": "Add +2 to the Label your mentor embodies or denies",
      "resources": "Choose up to four more resources from your mentor",
      "doom": "Take a doom, doomtrack, and doomsigns from the Doomed playbook",
      "mutate": "Mutate further and reveal another two new abilities (chosen from any playbook)",
      "lockLessons": "Lock down your lessons and change playbooks",
      "mentor": "Choose a mentor for yourself (from the Protege's playbook)",
      "pastParagon": "Go back to your own time or become a paragon of the city",
      "legacy": "Become part of a larger superhero tradition and take a legacy (from the Legacy playbook)",
      "joinAbilities": "Gain two new abilities from any playook",
      "advance": "Take an advancement from your other half's playbook",
      "shame": "Confront your Shame in your terms; if you survive, change playbooks",
      "enhancement": "Undergo enhancement; take two new abilities",
      "lockSoldier": "Lock Soldier, and add +1 to a Label of your choice",
      "noAegis": "A.E.G.I.S. permanently loses Influence over you; change playbooks",
      "civilian": "Retire From A.E.G.I.S. to a civilian life or join the upper echelons of A.E.G.I.S. as a Senior Director",
      "future": "Return to the future and accept its new form, or jump to a different point in the past to begin your mission anew",
      "depart": "Depart for reaches unknown, never to return",
      "mask": "Take The Mask and a secret identity from the Janus playbook"
    },
    "beacon": {
      "drives": "drives",
      "drivesDescription": "Choose four drives to mark at the start of play. When you fulfill a marked drive, strike it out, and choose one: mark potential, clear a condition, take Influence over someone involved.\nWhen your four marked drives are all struck out, choose and mark four new drives. When all drives are struck out, change playbooks, retire from the life, or become a paragon of the city.",
      "lead": "lead the team successfull in battle",
      "kissDanger": "kiss someone dangerous",
      "hitYouShouldnt": "punch someone you probably shouldn't",
      "helpTeammate": "help a teammate when they most need you",
      "endThreat": "take down a threat all on your own",
      "outperform": "outperform an adult hero",
      "ridiculous": "pull off a ridiculous stunt",
      "saveTeammateLife": "save a teammate's life",
      "drunkOrDrug": "get drunk or high with a teammate",
      "drive": "drive a fantastical vehicle",
      "newSuit": "get a new costume",
      "newName": "get a new hero name",
      "gainRespect": "earn the respect of a hero you admire",
      "kissTeammate": "make out with a teammate",
      "punchTeammate": "punch out a teammate",
      "breakRelation": "break up with someone",
      "stopFight": "stop a fight with calm words",
      "trueFeelings": "tell someone your true feelings for them",
      "placeOrTime": "travel to a incredible place (or time)",
      "reject": "reject someone who tells you `you shouldn't be here`"
    },
    "bull": {
      "rival": "rival",
      "lover": "lover",
      "title": "The Bull's Heart",
      "explanation": "You always have exactly one love and one rival. You can change your love or rival at any time; give the new subject of your affections or disdain Influence over you. Take +1 ongoing to any action that impress your love or frustrates your rival.",
      "description": "Choose a role you commonly fulfill with your love or rival",
      "roles": {
        "list": ["defender", "friend", "listener", "enabler"],
        "titles_dict": {
          "defender": "defender",
          "friend": "friend",
          "listener": "listener",
          "enabler": "enabler"
        },
        "titles": {
          "defender": "Defender",
          "friend": "Friend",
          "listener": "Listener",
          "enabler": "Enabler"
        },
        "descriptions": {
          "defender": "When you leap to defend your love or rival in battle, roll +Danger instead of +Savior to defend them.",
          "friend": "When you comfort or support your love or rival, mark potential on a hit. When your love or rival comforts or supports you, mark potential when they roll a hit.",
          "listener": "When you pierce the mask of your love or rival, you can always let them ask you a question to ask them an additional question in turn, even on a miss. These additional questions do not have to be on the list.",
          "enabler": "When you provoke your love or rival, roll +Danger if you are trying to provke them to rash or poorly thought out action."
        }
      }
    },
    "doomed": {
      "nemesis": {
        "title": "Nemesis",
        "description": "You have a nemesis, an epic and powerful enemy representing and embodying your doom. It's going to take everything you have to take them down in the time you have left.\nWho is your nemesis _______________?\nAt the end of every session, answer the question: Did you make progress on defeating your nemesis? If the answer is yes, mark potential. If the answer is no, mark your doom track."
      },
      "doomBringers": {
        "title": "Doom",
        "description": "You're doomed. Your powers may be killing you, or maybe you're hunted ruthlessly, or maybe you embody an apocalypse. But one way or another, your future is grim. What brings your doom closer? Choose two.",
        "markExplanation": "Whenever you bring your doom closer, mark one box on your doom track.",
        "track": "Doom Track:",
        "fillExplanation": "When your doom track fills, clear it and take one of your doomsigns.",
        "overexerting": "overexerting yourself",
        "innocents": "injuring innocents",
        "alone": "facing danger alone",
        "loved": "frightening loved ones",
        "mercy": "showing mercy",
        "openly": "talking about it openly"
      },
      "doomsigns": {
        "title": "Doomsigns",
        "description": "These are abilities that come to you with your approaching doom. Once you have taken all five doomsigns above the line, you must take 'Your doom arrives' the next time your doom track fills. Choose one doomsign you already hold at character creation.",
        "accessors": {
          "visions": "visions",
          "infinite": "infinite",
          "portal": "portal",
          "bright": "bright",
          "bolstered": "bolstered",
          "perish": "perish"
        },
        "titles": {
          "visions": "Dark Visions",
          "infinite": "Infinite Powers",
          "portal": "Portal",
          "bright": "Burning Bright",
          "bolstered": "Bolstered",
          "perish": ""
        },
        "descriptions": {
          "visions": "Mark your doom track to have a vision about the situation at hand. After the vision, ask the GM a question; they will answer it honestly.",
          "infinite": "Mark your doom track to use an ability from any playbook, one time.",
          "portal": "Mark your doom track to appear in a scene with anyone you want.",
          "bright": "Mark your doom track to ignore one of the GM's stated requirements when you call upon the resources of your sanctuary.",
          "bolstered": "Mark your doom track to use an Adult Move one time.",
          "perish": "Your doom arrives; confront it and perish."
        },
        "sanctuary": {
          "title": "Sanctuary",
          "description": "You have a place where you can rest, recover, and reflect upon your powers. Choose and underline three features of your sanctuary:",
          "callResources": "When you call upon the resources of your sanctuary to solve a problem, say what you want to do. The GM will give you one to four conditions you must fulfill to complete your solution:",
          "features": {
            "assistant": "an aide or assistant",
            "traps": "locks and traps",
            "tomes": "a library full of valuable tomes",
            "relics": "a scattering of ancient relics",
            "teleportal": "a teleportal",
            "containment": "a containment system",
            "computer": "a powerful computer",
            "tools": "useful tools",
            "meditation": "a meditation space",
            "battery": "a power battery",
            "enhancement": "a power enhancement system",
            "healing": "healing equipment",
            "art": "art, music and food"
          },
          "downsides": {
            "access": "difficult to access",
            "attention": "draws dangerous attention",
            "location": "location known to many",
            "damaged": "easily damaged or tampered with",
            "tied": "tied intricately to your doom"
          },
          "conditions": {
            "first": "First, you must ______________",
            "help": "You'll need help from _____________",
            "danger": "You and your team will rist danger from ____________",
            "lesser": "The best you can do is a lesser version, unreliable and limited",
            "doom": "You'll need to mark one box on your doom track",
            "obtain": "You'll have to obtain ______________"
          }
        }
      }
    },
    "janus": {
      "title": "Secret identity",
      "description": "Your mundane life comes with a series of obligations. Choose a total of three obligations.",
      "jobs": {
        "barista": "barista",
        "intern": "intern",
        "host": "host/ess",
        "sales": "salesperson",
        "delivery": "delivery person",
        "fastfood": "fast-food worker",
        "babysitter": "babysitter",
        "dishwasher": "dishwasher",
        "tech": "tech support",
        "waiter": "waitress/er"
      },
      "school": {
        "schoolwork": "schoolwork",
        "athletic": "athletic team",
        "chess": "chess club",
        "photography": "photography club",
        "government": "student government"
      },
      "home": {
        "caring": "caring for someone",
        "chores": "household chores",
        "bills": "paying bills",
        "parenting": "surrogate parenting"
      },
      "social": {
        "significant": "significant other",
        "friend": "best friend",
        "popularity": "popularity",
        "relative": "close relative",
        "teacher": "coach/teacher"
      }
    },
    "legacy": {
      "active": "is still active and prominent in the city.",
      "retired": "is retired and quite judgemental.",
      "possible": "is the next possible member of your legacy",
      "opponent": "is the greatest opponent of your legacy ever faced... and is still at large."
    },
    "nova": {
      "flares": "flares",
      "yourFlares": "Your flares are:",
      "accessors": {
        "storm": "storm",
        "shield": "shield",
        "constructs": "constructs",
        "moat": "moat",
        "worship": "worship",
        "move": "move",
        "boost": "boost",
        "overcharge": "overcharge",
        "elemental": "elemental",
        "snatch": "snatch"
      },
      "names": {
        "storm": "Reality storm",
        "shield": "Shielding",
        "constructs": "Constructs",
        "moat": "Moat",
        "worship": "Worship",
        "move": "Move",
        "boost": "Boost",
        "overcharge": "Overcharge",
        "elemental": "Elemental awareness",
        "snatch": "Snatch"
      },
      "descriptions": {
        "storm": "You channel a destructive burst with your powers. Spend 1 burn to directly engage a threat using your powers, rolling + Freak instead of + Danger. If you do, you will cause unwanted collateral damage unless you spend another burn.",
        "shield": "You call up a fast protective field to stop a danger. Spend 1 burn to defend someone else from an immediate threat, rolling + Freak instead of + Savior.",
        "constructs": "Spend 1 burn to create any object with your powers, up to the size of a person. Spend an additional burn to animate it independently of yourself. The construct dissolves at the end of the scene.",
        "moat": "Spend 1 burn to create a barrier that will hold back threats as long as you keep your atention on it. The GM may call for you to spend another burn if the barrier is threatened by particularly powerful enemies.",
        "worship": "You put a tremendous display of your might. Spend 1 burn to awe an audience into silence, respect and attention when you unleash your powers.",
        "move": "Spend 1 burn to move to any place you choose within the scene, breaking trough or slipping any barriers or restraints in your way. Spend a second burn to move to any place you've previously been.",
        "boost": "Spend 1 burn to supercharge a teammate's efforts with your powers, giving them a +1 bonus to their rols as if you had spent Team from the pool.",
        "overcharge": "You channel the full capacity of your increible powers to overcome an obstacle, reshape your enviroment, or extend your senses. Spend 2 burn to take a 10+ when you unleash your powers.",
        "elemental": "Spend 1 burn and mark a condition to open your mind up to the world around you with your powers. You can ask any one question about the world around you, and the GM will answer honestly.",
        "snatch": "Spend 1 burn to use your powers to seize any one object up to the size of a person from someone within view."
      }
    },
    "protege": {
      "embodies": "embodies",
      "denies": "denies",
      "mentor": {
        "title": "Mentor",
        "description": "You have a mentor, someone who's taught you, given you aid, or raised you up. Someone who might have confined you a bit too rigidly to a single path. Which label do they embody, and which do they deny? (circle one each)",
        "embodies": "Encarna",
        "denies": "Niega"
      },
      "resources_accessors": {
        "base": "base",
        "vehicle": "vehicle",
        "supercomputer": "supercomputer",
        "communicators": "communicators",
        "surveillance": "surveillance",
        "identities": "identities",
        "badges": "badges",
        "chem": "chem",
        "med": "med",
        "teleportal": "teleportal",
        "weapon": "weapon",
        "security": "security",
        "robots": "robots"
      },
      "resources": {
        "base": "a hidden base",
        "vehicle": "a vehicle",
        "supercomputer": "a supercomputer",
        "communicators": "communicators",
        "surveillance": "surveillance equipment",
        "identities": "false identities",
        "badges": "badges of authority",
        "chem": "a chem lab",
        "med": "a med lab",
        "teleportal": "a teleportal",
        "weapon": "a weapon of last resport",
        "security": "security systems",
        "robots": "simple robots"
      }
    },
    "reformed": {
      "title": "Friends in low places",
      "description": "You have ties to villains from your previous career. Choose three names to fill in:",
      "nameExamples": "Finch, Ellen 'Devil' Drummond, Mr. Cane, The Mad Magpie, Dr. Cutler, Armorer, Tegan Queen, Lovelace",
      "choose": "For each of them, choose a speciality.",
      "speciality": "Speciality",
      "obligation": "Obligation",
      "specialities": ["weapons", "materials", "cosmic artifacts", "alien tech", "insider info"],
      "atCreation": "When you create your character, mark two obligations on one villain, and mark one obligation on another."
    },
    "newborn": {
      "title": "A Blank Slate",
      "description": "You were created with a basic understanding of the world. When you learn something that helps you make sense of the world, write it down as a lesson. Fill in two lessons when you create your character; fill in the other two when you've learned those lessons during play.",
      "iam": "I am",
      "should": "A superhero should",
      "always": "Always",
      "never": "Never"
    },
    "innocent": {
      "title": "Your future self",
      "description": "Your future self is out there, an important figure in Halcyon City and the world beyond - and everything you'd hoped you'd never be. But finding out how they became who they are may be al it takes to push you along a similar path. Pick one step of your future self's path that you already know about and circle it.",
      "lost": "They lost someone they cared about deeply",
      "failed": "They failed horrifically in a noble pursuit or cause",
      "crime": "They committed a major crime",
      "betray": "They betrayed a close friend or ally",
      "cost": "They won a victory at enormous cost to the world around them",
      "kill": "They killed someone",
      "battled": "They publicly battled another hero",
      "innocent": "They injured an innocent"
    },
    "star": {
      "title": "Audience",
      "description": "You are a celebrity in the city. By default, your audience is a limited group of interested fans, and you speak to them trough after-action interviews and infrequent press conferences.",
      "lovesDescription": "Why does your audience love you? Mark all that apply.",
      "loves": {
        "alike": "You're just like them",
        "dangerous": "You're a dangerous person, a bad seed",
        "noble": "You're a noble warrior for justice",
        "beautiful": "You're stunning, unique, and beautiful",
        "charming": "You're charming, well-spoken, and smart",
        "firebrand": "You're a firebrand, a rabble rouser"
      },
      "advantagesDescription": "Choose two advantages:",
      "advantages": {
        "devoted": "Your audience is utterly devoted to you",
        "speak": "You can easily speak to them at any time",
        "agent": "You have a PR agent to handle your audience",
        "money": "You earn a lot of money from their interest",
        "endorsement": "You have a major hero's endorsement",
        "wider": "You have a much wider audience"
      },
      "demandsDescription": "Choose two demands your audience makes on you:",
      "demands": {
        "stimulation": "They require constant stimulation",
        "perfection": "They require - no mistakes",
        "drama": "They require frequent bouts of drama",
        "heroism": "They require major acts of heroism",
        "novelty": "They require novelty and brand new action",
        "chemistry": "They require chemistry with your allies"
      }
    },
    "joined": {
      "otherHalf": {
        "title": "Your other half",
        "description": "You share a deep bond with your other half. You are stronger together than you are apart, for now. If your other half is a Delinquent, Outsider or Transformed, take two moves from theid playbook: one they have and one they don't. Remember that you share much beyond your moves; i.e. if your other half is an Outsider, you both hail from the same dimension/planet/etc. For all other playbooks, you share in the core extras of your other half",
        "beacon": "Take drives and mark four of your choice. When your other half strikes out a drive, strike it out as well.",
        "bull": "Take The Bull's Heart with the same love and rival as your other half. Choose a different role that you commonly fulfill.",
        "janus": "Take The Mask and a secret identity. Choose a different Label for your Mask. Take two obligations: one shared, one unique to you.",
        "legacy": "Take a legacy. Your other half fills in as many names in the initial list as they choose; you fill in the rest. You can never answer the questions for your other half's Legacy move.",
        "protege": "You share a mentor with your other half. When they finish defining your mentor and resources, choose an additional resource.",
        "doomed": "Take a sanctuary, a doom, and a doom track. You and your other half share the conditions that bring your doom closer and a doom track; when it fills, you both choose a new doomsign. You start with the doomsign your other half chose. Your other half picks the initial features and downsides of your shared sanctuary. You choose one more of each.",
        "nova": "Take burn and four flares, two shared and two unique to you."
      },
      "bondsDistinctions": {
        "title": "Bonds and distinctions",
        "description": "At character creation you start with Two of a kind, and choose one other bond. When either you or your other half locks a Label, cross of one of your chosen bonds and choose a distinction.",
        "bonds": {
          "titles": {
            "two": "Two of a kind",
            "fastball": "Fastball special",
            "activate": "Powers, activate!",
            "eyes": "Four eyes are better"
          },
          "descriptions": {
            "two": "When time passes, ",
            "fastball": "",
            "activate": "When you and your other half",
            "eyes": "Four eyes are better"
          }
        }
      }
    },
    "brain": {
      "title": "Your shame",
      "description": "You have a deep and abiding sense of guilt for something you have created or had a hand in creating. It could have been something you invented when you first came into your genius, or something you set into motion that you no longer have the power to stop. It may even be something beyond your ability to achieve again, this one in a lifetime creation. Just as you are a world-class intellect, your sheme is a world-class problem. Whatever the case may be, your role in its creation is not publicly known... yet.",
      "is": "What is your shame",
      "isOptions": ["A prototype AI", "A cosmic phenomenon", "A catastrophic weapon", "A dangerous chamical", "A living monstrosity", "An altered former ally"]
    },
    "soldier": {
      "title": "A higher calling",
      "description": "You work for a metahuman law enforcement agency (A.E.G.I.S.) that keeps the world safe from all manner of superhuman, supernatural, and extraterrestrial threats. You volunteered to work with a team of young superheroes as part of a new A.E.G.I.S. program designed to keep Halcyon City safe.",
      "label": "You have an additional Label:",
      "labelExplanation": "Soldier functions like any other Label. Characters with Influence over you can shift it, and you mark a condition if it would ever shift above +3 or below -2. You can only cancel the influence A.E.G.I.S. holds over you with the appropiate advancement. You cannot lock Soldier with a Moment of Truth."
    },
    "harbinger": {
      "monster": "Monster",
      "traitor": "Traitor",
      "corruptor": "Corruptor",
      "martyr": "Martyr",
      "builder": "Builder",
      "leader": "Leader"
    },
    "nomad": {
      "title": "Putting down roots",
      "description": "You’re here, but not, and it shows. Over time, you may be able to commit to this place, and find out why it is that some people choose to invest in others.\nAdults do not have Influence over you by default. No one does. You can only give out a total of 6 Influence. During play, you can only give out Influence by revealing a vulnerability or weakness to someone. You can still give out Influence through the end of session move. You cannot give Influence to somebody who already has Influence over you.\nOthers cannot take Influence over you; if they would, instead they can mark potential or inflict a condition on you, their choice. You reject Influence at -2 by default, instead of +0. When someone takes advantage of their Influence over you, they can choose two options from the list. At the end of every session, you can take back 1 Influence from someone of your choice.\nIf you have given out 0-Influence, you cannot comfort or support anyone. If you would trigger that move, instead mark a condition as you say exactly the wrong thing. If you have given out 0-Influence and someone tries to comfort or support you, you cannot open up to them.",
      "benefits": "You gain benefits based on how much Influence you have given out. These benefits stack.",
      "oneTwo": "When you defend someone who has Influence over you, you can ignore the Insecure condition. When you directly engage someone who has Influence over you, you can ignore the Afraid condition.",
      "three": "When you take a powerful blow from someone with Influence over you, take -2 to the roll.",
      "four": "When you pierce the mask of someone who has Influence over you, you can always ask them one question, even on a miss.",
      "five": "When you spend a Team to help someone who has Influence over you, it gives them +2.",
      "six": "When you accept the words of someone who has Influence over you, mark potential, clear a condition, or take +1 forward."
    },
    "scion": {
      "title": "Respect",
      "description": "Write down the names of at least two other characters whose respect you need to earn in order to differentiate yourself from your parent. You may fill in new names whenever appropriate.",
      "enemy": "Your parent's greatest enemy",
      "victim": "Your parent's greatest victim",
      "idol": "Your personal idol",
      "leader": "The city's greatest leader",
      "hero": "The city's greatest hero",
      "celebrity": "The city's biggest celebrity"
    }
  }
}


def get_en_dict():
    return en