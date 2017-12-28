def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class Const(object):
    @constant
    def BOOTSTRAP_SERVER():
	#return '172.17.0.1:9092'
        #return '10.0.2.15:9092'
        return 'localhost:9092'  #use docker run --net="host" ... 

    @constant		
    def TOPIC1():
        return 'topic1'
		
    @constant
    def TOPIC2():
        return 'topic2'

CONST = Const()
