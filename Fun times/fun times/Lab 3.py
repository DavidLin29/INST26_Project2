from tkinter import *
import random 




class card(): # creates and manipulates card objects
    """This basically just makes the card class and allows all cards to have the properties listed below"""
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank # face rank of the card
        self.value = value # integer value of the card
        self.name = f"{rank}_of_{suit}"
        self.face = f"images/{rank} of {suit}.png" # relative address
        self.back = "images/BackOfCard.png"  # relative address
        self.state = False # default state = False = face down
        self.suit_val = suits.index(suit)
    
    def face_down(self): # set state to 0 = face down; return the Tkinter formatted image
        self.state = False
        img_file = self.back
        img_out = PhotoImage(file=img_file)
        return img_out
    
    def face_up(self): # set state to True = face up; return the Tkinter formatted image
        self.state = True
        img_file = self.face
        img_out = PhotoImage(file = img_file)
        return img_out
    
    def display(self): #returns the image file address
        if self.state:
            img = self.face
        else:
            img = self.back
        return img
    
    def photoimage(self): # returns the image in Tkinter format
        if self.state == 1:
            img_file = self.face
        else:
            img_file = self.back
            
        img_out = PhotoImage(file=img_file)
        return img_out





#Creating the deck itself

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]

# function to make a deck (list) of card objects
def make_deck(suits = suits, ranks = ranks, card_values = card_values):
    """Makes my deck :D"""
    deck = [] # initialize the list
    for suit in suits: # loop through the suits
        for index, rank in enumerate(ranks): # loop through the ranks; enumerate gives us the index number
            value = card_values[index] # We use the index number here to get the card value
            newcard = card(suit, rank, value) #create a new card object by calling the card class
            deck.append(newcard) # append the new card to the ceck list
    return deck

# create the deck
mydeck = make_deck() # create the deck
random.shuffle(mydeck) # shuffle the deck



#Dealing the deck out to each player

def deal_deck(mydeck):
    """How I create my hands for each player, starts with empty lists and having it deal to dealer first. """
    player_hand = []
    dealer_hand = []
    
    #Dealing cards to the dealer first
    for i in range(2):
        dealer_hand.append(mydeck.pop())
        
    #Dealing cards to the player now
    for i in range(2):
        player_hand.append(mydeck.pop())

    return dealer_hand, player_hand
dealer_hand, player_hand = deal_deck(mydeck)  

window = Tk()

"""Creating the window"""
window.title("Lab 02")
window.geometry('1000x800')
window.config(bg='green')

frame = Frame(window,bg="white",bd=5)
frame.pack(pady = 50)

label = Label(frame,
              text = 'INST_326 Lab 2',
              background = '#fcba03',
              fg = '#FFFFFF',
              font = ('Gill Sans','20'),
              wraplength = 200,)       
label.pack()



#Putting all the initial cards on the gui
backOfCard = PhotoImage(file='images/BackOfCard.png')
dealers_card = card.face_up(dealer_hand[0])
buttonsFrame = Frame(window, bg = 'green', bd = 1)
buttonsFrame.pack()

dealer_label = Label(buttonsFrame, text = "Dealer", font = ('Gill Sans', '8'))
cardButton1 = Button(buttonsFrame, image = dealers_card, bd = 0)
cardButton2 = Button(buttonsFrame, image = backOfCard, bd = 0)
player_label = Label(buttonsFrame, text = 'Player 1', font = ('Gill Sans', '8'))
cardButton3 = Button(buttonsFrame, image = backOfCard, bd = 0)
cardButton4 = Button(buttonsFrame, image = backOfCard, bd = 0)

dealer_label.grid(row= 0, column = 0)
cardButton1.grid(row = 0, column = 1)
cardButton2.grid(row = 0, column = 2)
player_label.grid(row = 1, column = 0)
cardButton3.grid(row = 1, column = 1)
cardButton4.grid(row = 1, column = 2)



"""Code below is how I create the peek window"""
peek_num = 0
def peek():
    global peek_num
    global card

    new_window = Toplevel()
    for rot in player_hand:
        image = card.face_up(rot)
        peek_num += 1
        card_player = Button(new_window, image = image)
        card_player.photo = image
        card_player.grid(column = peek_num, row = 0)

Button(window, text = "peek", command = peek).pack()
"""If a click is detected on the button then a new card is dealt and player hand is appended with the image being face up"""
def hitme():
    global player_hand, mydeck
    hit_card = mydeck.pop()
    player_hand.append(hit_card)
    img = card.face_up(hit_card)
    card_button = Button(buttonsFrame, image=img, bd=0)
    card_button.image = img  
    card_button.grid(row=1, column=len(player_hand) + 1)  

hit_button = Button(buttonsFrame, text="Hit Me", command=hitme)
hit_button.grid(row=2, column=0, columnspan=3)
    




window.mainloop()

