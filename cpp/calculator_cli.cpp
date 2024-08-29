#include <iostream>
#include <string>
#include <typeinfo>
#include <cmath>

class calculator_cli{
    public:
        calculator_cli();
        ~calculator_cli();
        void setEquations(std::string);
        std::string getEquations();
        bool isFloat(std::string);
        bool validateEquation(std::string);
        bool validateChar(std::string,char);
        bool validateChar(std::string, std::string);
        // bool isInt(int &temp);
        std::string calculate(std::string);
        std::string brackets(std::string);
        std::string indices(std::string);
        std::string division(std::string);
        std::string multiplication(std::string);
        std::string addition(std::string);
        std::string subraction(std::string);
    private:
        std::string eqr;
};

calculator_cli::calculator_cli(){
}

calculator_cli::~calculator_cli(){
}

void calculator_cli::setEquations(std::string equations){
    eqr = equations;
    //std::cout << "eqr has been set to: "<<eqr<< " ("<<equations<<")."<<std::endl;
}

std::string calculator_cli::getEquations(){
    return eqr;
}

bool calculator_cli::isFloat(std::string value){
    try{
        size_t idx = 0;
        while (idx < value.size()){
            if (!std::isdigit(value[idx])){
                char c = value[idx];
                if(!(c == '.')){
                    return false;
                }
            }
            ++idx;
        }
        return true;        
    } catch (...){
        return false;
    }
}

bool calculator_cli::validateEquation(std::string value){
    size_t idx = 0;
    while(idx < value.size()){
        char c = value[idx];
        if(!std::isdigit(c)){
            switch (c){
            case '(':
                break;
            case ')':
                break;
            case '/':
                break;
            case '*':
                break;
            case '+':
                break;
            case '-':
                break;
            case '.':
                break;
            default:
            // std::cout<<"Not a valid character: "<<c<<std::endl;
            return true;
                break;
            }
        }
        ++idx;
    }
    return false;
}

bool calculator_cli::validateChar(std::string value, char c){
    size_t idx = 0;
    bool brc = false;   
    int count = 0;
    while(idx<value.size()){
        char c_i = value[idx];
        // std::cout<<idx<<". "<<c_i<<"\tCount: "<<count<<std::endl;
        if(!std::isdigit(c_i)){ 
            // switch (c)
            // {
            if (c_i==c && c=='('){
            // case '(':
                brc = true;
                // std::cout<<idx<<". ( "<<c_i<<std::endl; 
                ++count;
            //     break;
            } else if(c_i==')' && c=='('){
            // case ')':
                brc = true;
                // std::cout<<idx<<". ) "<<c_i<<std::endl;
                --count;
            //     break;
            } else if(c_i==c && c=='/'){
            // case '/':
            //     return true;
            //     break;
            } else if(c_i==c && c=='*'){
            // case '*':
            //     return true;
            //     break;
            } else if(c_i==c && c=='+'){
            // case '+':
            //     return true;
            //     break;
            } else if(c_i==c && c=='-'){
            // case '-':
            //     return true;
            //     break;
            }
            // default:
            //     // std::cout<<"default: "<<value.substr(idx,2)<<std::endl;
            //     break;
            // }
        }
        ++idx;
    }
    // std::cout<<idx<<". "<<value<<"\tCount: "<<count<<std::endl;
    if (brc){
        if (count==0){
            return true;
        } else if (count<0){
            std::cout << "Error: more )"<<std::endl;
        } else if (count>0){
            std::cout << "Error: more ("<<std::endl;
        }
    }
    return false;
}

bool calculator_cli::validateChar(std::string value, std::string c){
    size_t idx = 0;
    while(idx<value.size()-1){
        std::string c_i = value.substr(idx,2);
        bool bl = c_i == "**";
        // std::cout<<idx<<". "<<c_i<<"   "<<bl<<std::endl;
        if(bl){
            return true;
        }
        ++idx;
    }
    return false;
}

std::string calculator_cli::calculate(std::string value){
    if(validateEquation(value)){
        std::cout<<"Not an Equation: "<<value<<std::endl;
    } else{
        // int ind = 1;
        while(!isFloat(value)){
            value = brackets(value);
            // std::cout<<ind<<". Simplified: "<<value<<"\n"<<std::endl;
            // ind++;
            // if (ind > 1){
            //     break;
            // }
        }
        std::cout<<"Calculated value: "<<value<<std::endl;
    }
    return value;
}

std::string calculator_cli::brackets(std::string value){
    if(validateChar(value,'(')){

        bool lp = true;
        int idx_1,idx_3, i = 0;
        while (lp){
            // std::cout<<i<<std::endl;
            char c = value[i];
            if (c==')'){
                idx_3 = i;
                lp = false;
            } else if (c=='('){
                idx_1 = i;
            }
            ++i;
        }
        idx_3++;
        // std::cout<<"Over here - diff: "<<idx_1<<std::endl;
        std::string val_1 = value.substr(0,idx_1);
        // std::cout<<val_1<<std::endl;
        // std::cout<<"Over here - diff: "<<(idx_3-idx_1)<<std::endl;
        std::string val_2 = value.substr(idx_1,(idx_3-idx_1));
        val_2 = val_2.substr(1,val_2.size()-2);
        // std::cout<<val_2<<std::endl;
        // std::cout<<"Over here - diff: "<<(value.size())<<std::endl;
        std::string val_3 = value.substr(idx_3,(value.size()));
        // std::cout<<val_3<<std::endl;
        // std::cout<<"Over here"<<std::endl;

        // std::cout<<"Original: "<<value<<std::endl;
        std::cout<<"[Bracket] "<<value<<" > "<<val_1<<" ~ "<<val_2<<" ~ "<<val_3<<std::endl;
        // std::cout<<"Its a bracket"<<std::endl;

        val_2 = calculate(val_2);
        std::cout<<"[Bracket] "<<value<<" > "<<val_1<<" ~ "<<val_2<<" ~ "<<val_3<<std::endl;
        // std::cout<<std::isdigit(val_1[val_1.size()-1])<<std::endl;
        // std::cout<<(val_1[val_1.size()-1])<<std::endl;
        if (std::isdigit(val_1[val_1.size()-1])){
            value = val_1+"*"+val_2;
        } else{
            value = val_1+val_2;
        }

        if (std::isdigit(val_3[0])){
            value += "*"+val_3;
        } else{
            value += val_3;
        }
        std::cout<<"[Bracket] "<<value<<std::endl;
        return value;
    } else{
        return indices(value);
        // std::cout<<"Its not a bracket"<<std::endl;
    }
}

std::string calculator_cli::indices(std::string value){
    if(validateChar(value,"**")){
        int idx = 0;
        bool lp=true, trig = true;
        std::string val_1="", bse="", pwe="", val_3="";
        // while(idx<value.size()-1){
        while (lp){
            std::string c_i = value.substr(idx,2);
            // std::cout<<"[Indices] "<<idx<<". "<<c_i<<" ~ "<<(c_i=="**")<<std::endl;
            if (c_i == "**"){
                lp=false;
            }
            // bool bl = c_i == "**";
            // // std::cout<<idx<<". "<<c_i<<"   "<<bl<<std::endl;
            // if(bl){
            //     return true;
            // }
            ++idx;
        }

        int i = idx-2;
        // lp = true;
        std::cout<<"[Indices] "<<value<<std::endl;
        while(!(i<0)){
            char c = value[i];
            if (!(std::isdigit(c) || c == '.')){
                trig = false;
            }
            if(trig){
                bse = c+bse;
            } else{
                val_1 = c+val_1;
            }
            // std::cout<<"[Indices] "<<c<<std::endl;
            // std::cout<<"[Indices] "<<val_1<<" ~ "<<bse<<"^"<<pwe<<val_3<<std::endl;
            i--;
        }

        i = idx+1;
        trig = true;
        while (i<value.size()){
            char c = value[i];
            if(!(std::isdigit(c)||c=='.')){
                trig=false;
            }
            if(trig){
                pwe += c;
            } else{
                val_3 += c;
            }
            // std::cout<<"[Indices] "<<c<<std::endl;
            // std::cout<<"[Indices] "<<val_1<<" ~ "<<bse<<"^"<<pwe<<" ~ "<<val_3<<std::endl;
            i++;
        }

        std::cout<<"[Indices] "<<val_1<<" ~ "<<bse<<"^"<<pwe<<val_3<<std::endl;
        std::string val_2 = calculate(std::to_string(std::pow(std::stof(bse),std::stof(pwe))));

        return val_1+val_2+val_3;
    } else{
        return division(value);
    }
}

std::string calculator_cli::division(std::string value){
    if(validateChar(value,'/')){
        return "24";
    } else{
        return multiplication(value);
    }
}

std::string calculator_cli::multiplication(std::string value){
    if(validateChar(value,'*')){
        return "24";
    } else{
        return addition(value);
    }
}

std::string calculator_cli::addition(std::string value){
    if(validateChar(value,'+')){
        return "28";
    } else{
        return subraction(value);
    }
}

std::string calculator_cli::subraction(std::string value){
    if(validateChar(value,'-')){
        return "44";
    } else{
        return value;
    }
}   