class Palindrome:
    
    def __init__(self, phrase):
        
        self.phrase = phrase
    
    def is_palindrome(self) -> bool:
        
        p = self.phrase
        
        frase = p.replace(' ', '').lower()
        
        
        for i in range(len(frase)):
            
            if frase[i] != frase[len(frase) - i - 1]:
                return False
        
        return True