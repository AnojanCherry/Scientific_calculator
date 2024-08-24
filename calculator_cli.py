class calculator_cli:
    def __init__(self):
        """
        Python class for a cli calculator.
        
        Parameters:
            None

        Returns:
            OOP cli
        """
        return
    
    def calculate(self, eqr:str)->str:
        """
        Calculate the passed string data
        
        Parameters:
            eqr: Takes input in the form of string.
        
        Returns:
            str: returns after substituting string
        """

        while True:
            try:
                int(eqr)
                return(eqr)
            except:
                eqr = self.subract(eqr)
    
    def brackets(self, eqr:str)->str:
        """
        Python solve for brackets

        Parameters:
            eqr: Takes input in the form of string.
        
        Returns:
            str: returns after substituting string
        """
    
    def indices(self, eqr:str)->str:
        """
        Python solve for indices

        Parameters:
            eqr: Takes input in the form of string.
        
        Returns:
            str: returns after substituting string
        """
    
    def division(self, eqr:str)->str:
        """
        Python solve for division

        Parameters:
            eqr: Takes input in the form of string.
        
        Returns:
            str: returns after substituting string
        """

    def multiplication(self, eqr:str)->str:
        """
        Python solve for multiplication

        Parameters:
            eqr: Takes input in the form of string.
        
        Returns:
            str: returns after substituting string
        """

    def addition(self, eqr:str)->str:
        """
        Python solve for addition

        Parameters:
            eqr: Takes input in the form of string.
        
        Returns:
            str: returns after substituting string
        """

    def subract_verify(self, eqr:str):
        return
    
    def subract(self, eqr:str)->str:
        """
        Python solve for subraction

        Parameters:
            eqr: Takes input in the form of string.
        
        Returns:
            str: returns after substituting string
        """