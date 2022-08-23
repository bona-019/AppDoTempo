class Styles():
    def __init__(self):
        self.dropdown = {'margin-top': '65px'}
        self.desc = {'color': 'white', 'text-align': 'center', 'font-size': '30px', 'margin-top': '15px'}
        self.temp_text = {'text-align': 'center', 'font-size': '25px', 'font-weight': 'bold', 'color': 'white', 'margin-top': '15px'}
        self.temp_values = {'temp': {'text-align':'center', 'color': 'white'}, 'sense': {'text-align':'center', 'color': 'white'}, 'min': {'text-align':'center', 'color': 'lightblue'}, 'max': {'text-align':'center', 'color': 'orange'}}
        self.header = {'font-size': '100px', 'margin-top': '20px', 'text-align': 'center','color': 'lightgreen'}
        self.cidade = {'color': 'white', 'font-weight': 'bold', 'text-align': 'center', 'margin-top': '15px', 'font-size': '75px'}

    def dropdownMenu(self):
        return self.dropdown

    def showDesc(self):
        return self.desc

    def tempText(self):
        return self.temp_text

    def tempValues(self):
        return self.temp_values

    def showHeader(self):
        return self.header

    def showCidade(self):
        return self.cidade