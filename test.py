def deco(func):
	def traitement(*arg, **karg):
		avant = 'Ouedrassi Mohamed'
		aprer = 'Blabla 123'
		return avant + "  "+ str(func(*arg, **karg) + 10)  +" "+ aprer
	return traitement

@deco
def myfunc(a,b):
	return a+b


def to_dict(f):
	def trait(*arg, **karg):
		l = f(*arg, **karg)
		print arg
		
		
		print karg
		return dict([(k, v) for k,v in zip (l[::2], l[1::2])])
	return trait
var = {}
var['d'] = 800

@to_dict
def flist(a,b):
	return [i for i in range(20)]


def funct():
	return 'Data Return the function'

if __name__ == '__main__':
	result = myfunc(10, 500)
	print result
	koko = []
	print flist(40,30)
	
	print '**********************************'
	print funct
	print funct()
	

