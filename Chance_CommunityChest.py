class Container(EventHandler):
    ''' Defines the parameters of any container that handles events '''

    def __init__(self, win, center, space=True):
        ''' Initializes a container '''

        EventHandler.__init__(self)
        self._win = win
        self._center = center
        self._space = space

    def get_center(self):
        return self._center


class chance(Container):
    ''' Defines the parameters for a chance space '''

    def __init__(self, win, width, height, center, game):
        ''' Initializes a chance space '''

        Container.__init__(self, win, center)
        self._ = True
        self._width = width
        self._game = game
        self._height = height
        self._spot = Rectangle(win, width, height, center)
        self._text = Text(win, 'Chance', 8, center)
        self._text.set_depth(3)
        self._win.add(self._spot)
        self._win.add(self._text)
        
        # List of numbers representing chance cards 
        self._chancelist = [0, 1, 2, 3]    
    
    
    
    def choose(self):
        ''' Chooses a chance card at random and performs action on player '''
        
        card = random.choice(self._chancelist)
        self._text = None
        
        if card == 0:
            self._text = Text(self._win, "LOTTERY WIN! GET $50",
                                         16, (250, 385))
            self._text.set_depth(3)
            self._win.add(self._text)
            player.receive(self._game._currentplayer, 50)
        if card == 1:
            self._text = Text(self._win, "PAY HOSPITAL $100",
                                         16, (250, 385))
            self._win.add(self._text)
            self._game._currentplayer.pay(100)
        
        if card == 3:
            self._text = Text(self._win, "PAY ADDITIONAL TAX $90",
                                         16, (250, 385))
            self._win.add(self._text)
            self._game._currentplayer.pay(90)

                if card == 2:
            self._text = Text(self._win, "PAY DOCTOR $50",
                                         16, (250, 385))
            self._win.add(self._text)
            self._game._currentplayer.pay(50)    

    def remove_all(self):
        ''' Removes the chance text '''
        self._win.remove(self._text)


class communitychest(Container):
    ''' Defines the parameters of a community chest space '''

    def __init__(self, win, width, height, center, game):
        ''' Initializes a community chest space '''

        Container.__init__(self, win, center)
        self._space = True
        self._width = width
        self._height = height
        self._game = game
        self._win = win
        
        self._spot = Rectangle(win, width, height, center)
        self._win.add(self._spot)
        
        self._text1 = Text(win, 'Com', 8, (center[0], center[1] - 5))
        self._text2 = Text(win, 'Chest', 8, (center[0], center[1] + 10))
        self._text1.set_depth(3)
        self._text2.set_depth(3)

        self._win.add(self._text1)
        self._win.add(self._text2)
        
        # List of numbers representing community chest cards
        self._cclist = [0, 1, 2, 3]

    def choose(self):
        ''' Chooses a community chest card and performs action on player '''

        card = random.choice(self._cclist)
        self._text = None
        
        if card == 0:
            self._text = Text(self._win, "LOTTERY WIN! GET $50",
                                         14, (250, 385))
            self._text.set_depth(2)
            self._win.add(self._text)
            player.receive(self._game._currentplayer, 50)
        
        if card == 1:
            self._text = Text(self._win, "PAY HOSPITAL $100",
                                         14, (250, 385))
            self._win.add(self._text)
            self._game._currentplayer.pay(100)
        
        if card == 2:
            self._text = Text(self._win, "PAY DOCTOR $50",
                                         14, (250, 385))
            self._win.add(self._text)
            self._game._currentplayer.pay(50)

                if card == 3:
            self._text = Text(self._win, "PAY ADDITIONAL TAX $90",
                                         16, (250, 385))
            self._win.add(self._text)
            self._game._currentplayer.pay(90)