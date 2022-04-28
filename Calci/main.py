import fire

def main(number1,operator, number2):
    return number1+number2 if operator == "+" \
        else number1-number2 if operator == "-" \
        else number1/number2 if operator == "/" \
        else number1*number2 if operator == "*" \
        else None

if __name__ == "__main__":
    fire.Fire(main)