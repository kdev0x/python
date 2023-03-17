kylian_mbappe = ["kylian mbappé", 24 , " france" , " psg", 91 ]
kylian_mbappe_states = ["kylian mbappé", "PAC", 97 , "SHO", 89 ,"PAS" , 80 , "DRI", 92 , "DEF" , 36 , "PHY", 76]
neymar=["neymar", 31 , " brazile" , " psg", 89 ]
neymar_states =['PAC', 87 , 'SHO', 83 , 'PAS', 85 ,  'DRI', 93 , 'DEF', 37 , 'PHY', 61]
salem_aldawsery = ["salem aldawsery", 31 , "saudi arabia" , "alhilal" , 76]
salem_aldawsery_states =['PAC', 84 , 'SHO', 73 , "PAS", 69 , "DRI" , 81 , "DEF", 52 , "PHY" , 79 ]
amount_time = int(input("how many times do you want to run the app"))


for x in  range (0, amount_time):
 user_info = input("what do you want to compare or searech a player")
 if user_info == "search a player":
      player = input("what player do u want to search")
      if player == "kylian mbappé":
          print(kylian_mbappe)
      elif player == "salem_aldawsery":
          print(salem_aldawsery)
      elif player == "neymar":
          print(neymar)
      else:
        print("sorry we dont have this player availbel")



 if user_info == "compare":
     player_1_cmp = input("how is player 1")
     if player_1_cmp == "salem aldawsery":
         print(salem_aldawsery_states)
     elif player_1_cmp == "kylian mbappé":
         print(kylian_mbappe_states)
     elif player_1_cmp == "neymar":
         print(neymar_states)
     else:
         print("we dont have this player availbel")



     player_2_cmp = input("how is player 2")
     if player_2_cmp == "salem aldawsery":
         print(salem_aldawsery_states)
     elif player_2_cmp == "kylian mbappé":
         print(kylian_mbappe_states)
     elif player_2_cmp == "neymar":
         print(neymar_states)
     else:
         print("we dont have this player availbel")

