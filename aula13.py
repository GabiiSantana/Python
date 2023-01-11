num1 = input("Digite algo: ")
num2 = input("Digite denovo: ")

# if num1.isdigit() and num2.isdigit():
#     num1 = int(num1)
#     num2 = int(num2)
#     print(num1 + num2)
# else:
#     print('Não pude converter os números para fazer as contas.')

try:
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
except:
    print('Não pude converter os números para fazer as contas.')