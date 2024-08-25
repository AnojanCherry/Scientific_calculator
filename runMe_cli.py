import argparse
import copy
from calculator_cli import calculator_cli as cli

if __name__ == "__main__":

    # Initiate 
    cal = cli()

    # Parse arguments
    parser = argparse.ArgumentParser(description="Take cli inputs")
    parser.add_argument("--equation", "-eq", type=str, default="None", help="Pass in an equation to get result.")
    args = parser.parse_args()

    ## Unparse
    # unparse equations
    if(args.equation != "None"):
        tbdl = copy.copy(args.equation)
        for i in range(10):
            tbdl=tbdl.replace(str(i),"")
        tbdl=tbdl.replace("*","")
        tbdl=tbdl.replace("(","")
        tbdl=tbdl.replace(")","")
        tbdl=tbdl.replace("/","")
        tbdl=tbdl.replace("+","")
        tbdl=tbdl.replace("-","")
        print(len(tbdl))
        # if chr(i) in args.equation:
        #         error_msg = f"Can't solve for \"{chr(i)}\""
        #         raise Exception(error_msg)
        if (len(tbdl))>0:
            error_msg = f"Can't solve for \"{args.equation}\", unknown characters: {tbdl}"
            raise Exception(error_msg)
        print(f"Calculated value: {cal.calculate(args.equation)}")
    else:
        print("No equations to process")