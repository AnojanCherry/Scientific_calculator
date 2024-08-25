import copy

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
                float(eqr)
                return(eqr)
            except:
                eqr = self.brackets(eqr)
    
    def brackets(self, eqr:str)->str:
        """
        Python solve for brackets

        Parameters:
            eqr: Takes input in the form of string.
        
        Returns:
            str: returns after substituting string
        """

        if "(" in eqr:
            count = 0
            ind_s = 0
            ind_e = 0
            for ind, eq_i in enumerate(eqr):
                if "(" in eq_i:
                    ind_s = ind
                    count +=1
                if (")" in eq_i):
                    if (ind_e<=ind_s):
                        ind_e = ind 
                    count -= 1
            if count <0:
                raise Exception("More ) than (")
            elif count>0:
                raise Exception("More ( than )")
            eqr_s = eqr[:ind_s]
            eqr_splt = eqr[ind_s+1:ind_e]
            eqr_e = eqr[ind_e+1:]
            eqr_splt = self.calculate(eqr_splt)
            if eqr_s == "":
                if eqr_e == "":
                    return eqr_splt
                else:
                    try:
                        int(eqr_e[0])
                        return eqr_splt+"*"+eqr_e
                    except:
                        return eqr_splt+eqr_e
            elif eqr_e == "":
                try:
                    int(eqr_s[-1])
                    return eqr_s+"*"+eqr_splt
                except:
                    return eqr_s+eqr_splt
            else:
                eqr_return = ""
                try:
                    int(eqr_s[-1])
                    eqr_return+=eqr_s+"*"+eqr_splt
                except:
                    eqr_return+=eqr_s+eqr_splt

                try:
                    int(eqr_e[0])
                    eqr_return+="*"+eqr_e
                except:
                    eqr_return+=eqr_e
                return eqr_return
        else:
            return self.indices(eqr)
    
    def splitter_symb_2_eqr(self, symb:str, eqr:str):
        if symb in eqr:
            ind = eqr.index(symb)
            i=1
            try:
                while ind-i>=0:
                    if eqr[ind-i]!=".":
                        int(eqr[ind-i])
                    i+=1
                ind_s = 0
                eqr_s = ""
            except:
                ind_s = ind-i+1
                eqr_s = eqr[:ind_s]  
            
            i=ind+len(symb)   
            try:
                while i<=len(eqr):
                    if eqr[i]!=".":
                        int(eqr[i])
                    i+=1
                ind_e = -1
                eqr_e = ""
            except:
                ind_e = i
                eqr_e = eqr[ind_e:]
            
            eqr_splt = eqr[ind_s:ind_e]
            return True, eqr_s, eqr_splt, eqr_e
        else:
            return False, None, None, None
    
    def indices(self, eqr:str)->str:
        """
        Python solve for indices

        Parameters:
            eqr: Takes input in the form of string.
        
        Returns:
            str: returns after substituting string
        """
        
        if "**" in eqr:
            _,eqr_s,eqr_splt,eqr_e = self.splitter_symb_2_eqr("**", eqr)
            base, pwe = eqr_splt.split("**")
            eqr_splt = pow(float(base), float(pwe))
            return eqr_s+str(eqr_splt)+eqr_e
        else:
            return self.division(eqr)
    
    def division(self, eqr:str)->str:
        """
        Python solve for division

        Parameters:
            eqr: Takes input in the form of string.
        
        Returns:
            str: returns after substituting string
        """
        if "/" in eqr:
            _,eqr_s,eqr_splt,eqr_e = self.splitter_symb_2_eqr("/",eqr)
            n_ator,d_ator = eqr_splt.split("/")
            eqr_splt = float(n_ator)/float(d_ator)
            return eqr_s+str(eqr_splt)+eqr_e
        else:
            return self.multiplication(eqr)

    def multiplication(self, eqr:str)->str:
        """
        Python solve for multiplication

        Parameters:
            eqr: Takes input in the form of string.
        
        Returns:
            str: returns after substituting string
        """
        if "*" in eqr:
            _,eqr_s,eqr_splt,eqr_e = self.splitter_symb_2_eqr("*",eqr)
            var_a,var_b = eqr_splt.split("*")
            eqr_splt = float(var_a)*float(var_b)
            return eqr_s+str(eqr_splt)+eqr_e
        else:
            return self.addition(eqr)

    def addition(self, eqr:str)->str:
        """
        Python solve for addition

        Parameters:
            eqr: Takes input in the form of string.
        
        Returns:
            str: returns after substituting string
        """
        if "+" in eqr:
            _,eqr_s,eqr_splt,eqr_e = self.splitter_symb_2_eqr("+",eqr)
            var_a,var_b = eqr_splt.split("+")
            eqr_splt = float(var_a)+float(var_b)
            return eqr_s+str(eqr_splt)+eqr_e
        else:
            return self.subract(eqr)
    
    def subract(self, eqr:str)->str:
        """
        Python solve for subraction

        Parameters:
            eqr: Takes input in the form of string.
        
        Returns:
            str: returns after substituting string
        """
        if "-" in eqr:
            _,eqr_s,eqr_splt,eqr_e = self.splitter_symb_2_eqr("-",eqr)
            var_a,var_b = eqr_splt.split("-")
            eqr_splt = float(var_a)-float(var_b)
            return eqr_s+str(eqr_splt)+eqr_e
        return eqr