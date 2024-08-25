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
            # print("Here")
            print(eqr)
            try:
                int(eqr)
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
            # tmp = []
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
                # print(f"{ind}. {eq_i}")
            # for i in eqr:
            #     if "(" in i:
            #         tmp.append(eq_splt)
            #         eq_splt = ""
            #         count += 1
            #     elif ")" in i:
            #         tmp.append(eq_splt)
            #         eq_splt = ""
            #         count -= 1
            #     else:
            #         eq_splt += i
            # print(tmp)
            # if tmp[0] == "":
            #     del tmp[0]
            # if tmp[-1] == "":
            #     del tmp[-1]
            # input(tmp)
            # input(count)
            if count <0:
                raise Exception("More ) than (")
            elif count>0:
                raise Exception("More ( than )")
            # else:
            #     input(tmp)
            eqr_s = eqr[:ind_s]
            eqr_splt = eqr[ind_s+1:ind_e]
            eqr_e = eqr[ind_e+1:]
            # print(eqr_s)
            # print(eqr_splt)
            # input(eqr_e)
            # input(f"Calc: {eqr_splt}")
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
            # print("Here")
            return self.indices(eqr)
    
    def indices(self, eqr:str)->str:
        """
        Python solve for indices

        Parameters:
            eqr: Takes input in the form of string.
        
        Returns:
            str: returns after substituting string
        """
        if "**" in eqr:
            indice_char = ["**"]
            ind = eqr.index("**")
            i=1
            try:
                while ind-i>=0:
                    # input(eqr[ind-i])
                    int(eqr[ind-i])
                    i+=1
                ind_s=0
                eqr_s=""
            except:
                ind_s = ind-i+1
                eqr_s = eqr[:ind_s]
            print(eqr_s)
            i=ind+2
            try:
                while i<=len(eqr):
                    # input(eqr[i])
                    int(eqr[i])
                    i+=1
                ind_e=-1
                eqr_e=""
            except:
                ind_e = i
            eqr_e = eqr[ind_e:]
            # input(f"{eqr_s}\t{eqr_e}")
            # input(f"{eqr[ind_s:ind_e]}")
            eqr_splt = eqr[ind_s:ind_e]
            base,powe = eqr_splt.split("**")
            # input(f"{base}\t{powe}")
            eqr_splt = pow(int(base), int(powe))
            return eqr_s+str(eqr_splt)+eqr_e
            # if ind_s==0:
            #     if ind_e==0:
            #         print(eqr)
            # input()
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
    
    def subract(self, eqr:str)->str:
        """
        Python solve for subraction

        Parameters:
            eqr: Takes input in the form of string.
        
        Returns:
            str: returns after substituting string
        """