#include <iostream>
#include <string>
#include "cpp/calculator_cli.cpp"

//Prototypes
void equations(std::string);

int main(int argc, char* argv[]){
    bool equation_bool = false;
    std::string equation_str;

    std::string args_a = "", args_b = "";

    calculator_cli scientific_calculator;

    if (argc>1){
        for (int i = 1; i<argc; ++i){
            // std::cout<<"args: "<<argv[i]<<std::endl;
            // if (i<argc-1){
            //     args_b = args_a;
            //     args_a = "";
                // std::cout<<args_a<<" ~ "<<args_b<<std::endl;
            // }
            // args_a += argv[i];
            // std::cout << "Loop " << i << ". " << args_a << " ~ " << argv[i] << std::endl;
            if (args_a=="--equation" || args_a=="-eq"){
                scientific_calculator.setEquations(argv[i]);
                std::string value = scientific_calculator.calculate(scientific_calculator.getEquations());
                std::cout<<"Calculated value: "<<scientific_calculator.getEquations();
            }
            args_a = argv[i];
        }
    }

    std::cout<<std::endl;
    return 0;
}