import argparse
from calculator_cli import calculator_cli as cli

if __name__ == "__main__":

    # Initiate 
    cal = cli()

    # Parse arguments
    parser = argparse.ArgumentParser(description="Take cli inputs")
    parser.add_argument("--equation", type=str, default="None", help="Pass in an equation to get result.")
    args = parser.parse_args()

    ## Unparse
    # unparse equations
    if(args.equation != "None"):
        for i in range(ord("a"),ord("z")+1):
            if chr(i) in args.equation:
                error_msg = f"Can't solve for \"{chr(i)}\""
                raise Exception(error_msg)
        for i in range(ord("A"),ord("Z")+1):
            if chr(i) in args.equation:
                error_msg = f"Can't solve for \"{chr(i)}\""
                raise Exception(error_msg)
        cal.calculate(args.equation)
    else:
        print("No equations to process")