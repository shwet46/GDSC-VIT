def unique_elements(input_array):
    unique_array = []
    seen_set = set()

    for num in input_array:
        if num not in seen_set:
            unique_array.append(num)
            seen_set.add(num)

    return unique_array

def main():
    try:
        input_array = [int(x) for x in input("Enter integers separated by spaces: ").split()]
        result = unique_elements(input_array)
        print("Unique elements in the original order:", result)
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")

if __name__ == "__main__":
    main()
