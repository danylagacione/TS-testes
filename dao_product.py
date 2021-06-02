class DaoProduct:

    def read_category(self, list_products):
        
        with open('products.txt', 'a') as arquivo:
            for product in list_products:
                arquivo.write(f'{str(product)} \n')
