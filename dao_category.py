class DaoCategory:

    def category(self, list_categories):

        with open('categories.txt', 'a') as arquivo:
            for category in list_categories:
                arquivo.write(f'{str(category)} \n')

    def read(self):
        with open('categories.txt', 'r') as arquivo:
            return arquivo.read()


