class wordle:

    def __init__(self, secret_word, words):
        self.secret_word = secret_word
        self.words = words
        self.prev_attempts = []
        self.max_attempts = 6 
   

    def valid_guess_length(self, guess):
        return len(guess) == 5
     
        
    def valid_guess(self, guess):
        return guess in self.words
    
    def can_attempt(self):
        return len(self.prev_attempts) < self.max_attempts

    
    def attempts_left(self):
        return self.max_attempts - len(self.prev_attempts)
    
    def is_winner(self, guess):
        return guess == self.secret_word
    
    def format_guess(self, guess):
        
        colour_string = ""
            
        for i in range(5):
            if guess[i] == self.secret_word[i]:
                colour_string = colour_string + "[bold green]" + guess[i] + "[/bold green]"
            elif guess[i] in self.secret_word:
                colour_string = colour_string + "[bold yellow]" + guess[i] + "[/bold yellow]"
            else:
                colour_string = colour_string + guess[i] 
                    

        self.prev_attempts.append(colour_string)
    
    



        





