def main():
    ls = [1,2,3,4,5,6,6,7]
    dictionary:dict= {"1":0}
    for item in ls :
        if(str(item) in dictionary.keys()):
            dictionary[str(item)] += 1
        else:
            dictionary[str(item)] = 1
    
    print(dictionary)
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()