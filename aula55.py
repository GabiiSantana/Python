variavel = 'valor'

def func():
		print(variavel)

def func2():
		global variavel
		variavel = 'outro valor'

func()
func2()

print(variavel) # vai ter o mesmo valor da func2()