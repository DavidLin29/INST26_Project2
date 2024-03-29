from tkinter import *
import random 




class card(): # creates and manipulates card objects
    
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank # face rank of the card
        self.value = value # integer value of the card
        self.name = f"{rank}_of_{suit}"
        self.face = f"images\\{rank} of {suit}.png" # relative address
        self.back = "images\\BackOfCard.png"  # relative address
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

suits = ['clubs', 'diamonds', 'hearts', 'spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]

# function to make a deck (list) of card objects
def make_deck(suits = suits, ranks = ranks, card_values = card_values):
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

    
    
window = Tk()


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



def deal_deck(mydeck):
    player_hand = []
    dealer_hand = []
    
    #Dealing cards to the player first
    for i in range(2):
        player_hand.append(mydeck.pop(0))

    #Dealing cards to the dealer now
    for i in range(2):
        dealer_hand.append(mydeck.pop(0))

    return player_hand, dealer_hand
    
    
backOfCard = PhotoImage(file='images/BackOfCard.png')

buttonsFrame = Frame(window, bg = 'green', bd = 1)
buttonsFrame.pack()

dealer_label = Label(buttonsFrame, text = "Dealer", font = ('Gill Sans', '8'))
cardButton1 = Button(buttonsFrame, image = backOfCard, bd = 0)
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


def create_window():
    new_window = Tk()
    # window.destroy()


peek_num = 0
def peek():
    global peek_num
    new_window = Toplevel()
    for card in player_label:
        peek_num += 1
        image = PhotoImage(file = card.face)
        card_player = Button(new_window, image = image)
        card_player.photo = image
        card_player.grid(column = peek_num, row = 0)

Button(window, text = "peek", command = peek).pack()




hitmeButton = Button(window, text = 'hit me')
hitmeButton.pack()




window.mainloop()
