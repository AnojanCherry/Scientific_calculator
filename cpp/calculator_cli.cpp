#include <iostream>
#include <string>
#include <typeinfo>

class calculator_cli{
    public:
        calculator_cli();
        ~calculator_cli();
        void setEquations(std::string);
        std::string getEquations();
        bool isFloat(std::string);
        bool isInt(int &temp);
        void calculate();
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
    for(std::string::iterator it = value.begin(); it != value.end(); ++it){
        std::cout<<"Value: "<<typeid(*it).name()<<std::endl;
    }
    // for(char& it : value){
    //     if(isInt(it)){
    //         std::cout<<"Success: "<<it<<std::endl;
    //     } else{
    //         std::cout<<"Error: "<<it<<std::endl;
    //     }
    // }
    return true;
}

bool calculator_cli::isInt(int &value){
    std::cout<<"Value: "<<value<<std::endl;
    switch (value)
    {
    case 0:
        return true;
        break;
    case 1:
        return true;
        break;
    case 2:
        return true;
        break;
    case 3:
        return true;
        break;
    case 4:
        return true;
        break;
    case 5:
        return true;
        break;
    case 6:
        return true;
        break;
    case 7:
        return true;
        break;
    case 8:
        return true;
        break;
    case 9:
        return true;
        break;
    default:
    return false;
        break;
    }
}

void calculator_cli::calculate(){
    // Run the code in a loop
    // std::cout << "Value ~ "<<eqr<<" ~."<<std::endl;
    isFloat(eqr);
    try{
        float value = std::stof(eqr);
        std::cout<<"Float value: "<<value<<std::endl;
    } catch (...){
        std::cout<<"Not float type"<<std::endl;
    }

}