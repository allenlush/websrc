# coding=utf-8
# This is a Class to present Chinese Tradition Year calendar
# and response with TianGan & DiZhi.
# It is taking year 1984 as quick reference of Year Jiazi.

class Year:
    def __init__(self, number):
        self.number = number
        self.Gan = ['Jia', 'Yi', 'Bing', 'Ding', 'Wu', 'Ji', 'Geng', 'Xin', 'Ren', 'Gui']
        self.Zhi = ['Zi', 'Chou', 'Yin', 'Mou', 'Chen', 'Si', 'Wu', 'Wei', 'Shen', 'You', 'Xu', 'Hai']

    def GanZhi(self):
        x = self.number-1984
        g = x % 10
        z = x % 12
        return self.Gan[g]+self.Zhi[z]
#      return self.ganzhi

#__version__='0.1'
