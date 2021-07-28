def main():
    #write your code below this line
    inheritance =  int(input("Inheritance:"))
    years = int(input("Years since death:"))
    taxable = inheritance - 325000
    tax = 0.0

    if years < 3:
        tax_rate = 0.40
    elif years < 4:
        tax_rate = 0.32
    elif years < 5:
        tax_rate = 0.24
    elif years < 6:
        tax_rate = 0.16
    elif years < 7:
        tax_rate = 0.08
    else:
        tax_rate = 0.0

    tax = taxable * tax_rate

    print("Tax: " + str(tax))

if __name__ == '__main__':
    main()
