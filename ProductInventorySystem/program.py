from abc import *

class Entity(metaclass = ABCMeta):
    
    @abstractproperty
    def id_number(self):
        return 0
class Product(Entity):
    
    id = 0 #initially no id exist (this is class variable)
    #Constructor
    def __init__(self,name = None,value =0,amount =0, scale ='kg'):
        self._id = Product.id # accessing the class variable
        Product.id = Product.id+1
        self._value = value
        self._amount = amount
        self._scale = scale
        if not name:
            self._name = "{0}_{1}".format(self.__class__,self.id)
        else:
            self._name = name
    
    @property
    def id_number(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self,val):
        self._value = val
    
    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self,other):
        self._amount = other
    @property
    def scale(self):
        return self._scale
    @scale.setter
    def scale(self,other):
        self._scale = other
    def __repr__(self):
        return "{0}: {1}".format(self.__class__.__name__,self._id)
    def __str__(self):
        return "{amount}{scale} of {name} valued at {value}".format(amount = self._amount,scale = self._scale, name = self._name,
                                                                    value = self._value)   
 class Inventory(Entity):
    
    id = 0 # Class variable
    
    def __init__(self):
        self._id = Inventory.id # assiging class variable to object instance variable
        Inventory.id = Inventory.id+1
        self._products = {}
    
    def product_add(self,*args):
        
        def add_to_category(item):
            try:
                self._products[item.name].append(item)
            except:
                self._products[item.name]=[item]
        
        for arg in args:
            if isinstance(arg,tuple) or isinstance(arg,list):
                for item in arg:
                    add__to_category(item)
            elif isinstance(arg,Product):
                add_to_category(arg)
            # if it is not a product, then it will not be added
    
    @property
    def product_value(self):
        
        #Returns the sum of values of each item for each product category
        return sum([each.value for category in self._products for each in self._products[category]])
    
    @property
    def product_count(self):
    
        #Returns the total count of products
        return len([each for category in self._products for each in self._products[category]])
    
    @property
    def product_diff_categories(self):
        
        #Returns the number of different categories
        return len(self._products)
    
    @property
    def products (self):
        
        #Returns the list of products
        return self._products
    
    @property
    def id_number(self):
        
        #Returns the identity number of the product
        return self._id
    
    def __repr__(self):
        return "{0}:{1}".format(self.__class__.__name__,self._id)

class ObjFactory(metaclass = ABCMeta):
    
    @abstractmethod
    def get_object(self):
        return 0
    
    def __repr__(self):
        return "{0}:{1}".format(self.__class__.__name__,self._id)

class InventoryFactory(ObjFactory):
    
    def get_object(self,amt =1):
        for i in range(amt):
            yield Inventory()

class ProductFactory(ObjFactory):
    
    def get_object(self,amt =1):
        for i in range(amt):
            yield Product()
if __name__ =="__main__":
    
    #create an inventory
    inventory = Inventory()
    #add some products to the inventory
    genProd = lambda value:Product(value = value)
    for i in range(1,10):
        inventory.product_add(genProd(value = i))
    for i in range(1,5):
        inventory.product_add(genProd(value = i))
        
    Total_Products = inventory.product_count
    Total_Value = inventory.product_value
    Total_categories = inventory.product_diff_categories
    
    for name, info in (("Total Products are",Total_Products),("Total Value of the products is",Total_Value),("Total number of categories",Total_categories)):
        print ("{0}: {1}".format(name,info))
    print (inventory.products)
    for product in inventory.products:
        print (product + "prob details :" + str(inventory.products[product]))
