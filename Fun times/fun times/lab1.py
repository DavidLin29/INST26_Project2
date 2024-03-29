suits = ["clubs", "diamonds", "hearts", "spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
card_values = [2, 3 , 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
#Use loops and string methods to generate a list of cards using the suits and ranks lists and the following naming format for each card ‘rank_of_suit’. Name the list ‘deck’ (Output to turn in: Print the list) 4 points
  card_button = Button(buttonsFrame, image=img, bd=0)
    card_button.image = img  
    card_button.grid(row=1, column=len(player_hand) + 1)  

hit_button = Button(buttonsFrame, text="Hit Me", command=hitme)
hit_button.grid(row=2, column=0, columnspan=3)