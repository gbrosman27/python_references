# kobe = {"name": "Kobe", "age": 7, "fur_color": "black", "mom": "Chelsea", "is_happy": True}
#
# for k in kobe.keys():
#     print(k)
#
# for v in kobe.values():
#     print(v)
#
# for k,v in kobe.items():
#     print(f"{k} is the key and {v} is the value")
# ...................................................................
# game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo",
#                    "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications",
#                    "achievements"]
#
# initial_game_state = {}.fromkeys(game_properties, 0)
#
# print(initial_game_state)
# ....................................................................
# inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}
#
# stock_list = inventory.copy()
#
# stock_list.update({"cookie": 18})
#
# print(inventory)
# print(stock_list)
# .......................................................................
# playlist = {
#     "title": "Southern, Blues, and Grit",
#     "author": "Greg Brosman",
#     "songs": [
#         {"title": "Nose to the Grindstone", "artist": ["Tyler Childers"], "duration": 3},
#         {"title": "Guys like me", "artist": ["Eric Church"], "duration": 4},
#         {"title": "In Color", "artist": ["Jamey Johnson"], "duration": 3.5},
#         {"title": "Enter Sandman", "artist": ["Metallica"], "duration": 5}
#             ]
# }
# song_duration = 0
# for song in playlist['songs']:
#     print(song["title"])
#     song_duration += song["duration"]
#     print(song_duration)
# ............................................................................
# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]
#
# answer = {list1[i]: list2[i] for i in range(0, len(list1))}
# print(answer)
# ...........................................................................
# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
#
# # use the person variable in your answer
# answer = {val[0]:  val[1] for val in person}
# print(answer)
# .........................................................................

answer = {num: chr(num) for num in range(65, 91)}
print(answer)


