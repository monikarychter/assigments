
lista =input("Can you give me the list of numbers? If yes click ENTER:")
numbers=[1, 2, 56, 32, 51, 2, 8, 92, 15]
i = 1
j = 0
N = len(numbers)

def print_numbers():
    print(numbers)
print_numbers()

lista_sort = input("Can you write the sorted number? If yes click ENTER")

def sort_number(numbers):  #sorting an array
    
    for i in range(1, N):
        for j in range(0, N - 1):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j + 1]
                numbers[j + 1] = numbers[j]
                numbers[j] = temp
              
sort_number(numbers)
print(numbers)
            
                

def main_menu():
   
    if __name__ == '__main__':
        main_menu()        


