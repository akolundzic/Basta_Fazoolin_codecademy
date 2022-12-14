import sys
# ---- Menu class declaration ------
class Menu:
# 1 add motto to class
  motto = "At Basta Fazoolin’ with my Heart our motto is simple: when you’re here with family, that’s great! We have four different menus: brunch, early-bird, dinner, and kids."

# 3 brunch menu
  brunch ={ 'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

# 4 early bird menu
  early_bird = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
# 5 dinner menu
  dinner = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
# 6 kids menu
  kids = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
} 
# 22 create arepa mennu
  arepa = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
# when are the menus avaialble
  time_available ={'brunch':[11,16],'early_bird':[15,18],'dinner':[17,23], 'kids':[11,21],'arepa':[10,20]}

# 2 create constructor
  def __init__(self,name,start_time,end_time):
    self.name = name
    self.start_time = start_time
    self.end_time = end_time
    print(repr(self))
# 8 --------------------
  def __repr__(self):
    info_string = "This is not availalbe, exit programm "
    if(hasattr(self,self.name)):
        start,start_time=self.convert_time_ampm(self.start_time)
        end,end_time = self.convert_time_ampm(self.end_time)
        info_string = f"{str.title(self.name)} menu is available from {start_time}{start} to {end_time}{end}"  
    else: 
      print(info_string)
      sys.exit('')
    return info_string

# time string in am,pm
  def convert_time_ampm(self,timein):
    if timein <= 12: return('am',timein)
    else: return('pm',timein-12)

# 9 calculate bill
  def calculate_bill(self,purchased_items):
    sum = 0
    obj = getattr(self,self.name)
    for dish in purchased_items:
        sum += obj.get(dish,0)
    return round(sum,1)
  
  def info_for_customer(self,itemlist):
    return f"You have ordered {len(itemlist)} dishes:\n{','.join(itemlist)}"
  # get menu list
  def get_menulist(self):
    dic_menu = {'early_bird':self.early_bird,'dinner':self.dinner,'kids':self.kids,'brunch':self.brunch}
    return dic_menu

# ---- Franchise class declaration ------
# 12 create class franchise
class Franchise:
# 13 constructor
  def __init__(self,address,Menu):
    self.address = address
# 14 declare menu object, access its methods
    self.menu = Menu
    print(repr(self))

# 15 show repr string
  def __repr__(self):
    return f"Restaurant's address is : {self.address}"

  # 18 get available menus for time_in
  def available_menus(self,time_in):
    availalbe_menus =[]
    for menu in self.menu.time_available:
        [begin,end] = self.menu.time_available[menu]
        if time_in in range(begin,end+1):
          availalbe_menus.append(menu)
    return availalbe_menus

# print available menu list
  def print_menu(self,time_in):
    string_out = self.available_menus(time_in)
    postfix,time = self.menu.convert_time_ampm(time_in)
    if string_out:
      return f"Available menus at {time}{postfix}: {','.join(string_out)}"
    else: 
      return "No menu is at this time available"

# --- Business Class ---
# 19,20,21
class Business:
  def __init__(self,name,franchises):
    self.name = name
    self.franchises = franchises
    print(repr(self))
  
  def __repr__(self):
     string_out ='franchises'
     if type(list()) != type(self.franchises):
       print('Pass the right list argument')
       sys.exit('')
     length = len(self.franchises)
     if length == 1 : string_out='franchise'
     return f"{self.name} has {length} {string_out}"

# 10 test for brunch
brunch_menu = Menu('brunch',11,15)
print(brunch_menu.motto)
brunch_items = ['pancakes', 'home','coffee']
print(brunch_menu.info_for_customer(brunch_items))
print(f"Total amount is: {brunch_menu.calculate_bill(brunch_items)}€\n")

# 11 test for early bird
early_bird = Menu('early_bird',15,23)
early_bird_items = ['salumeria plate','mushroom ravioli (vegan)']
print(early_bird.info_for_customer(early_bird_items))
print(f"Total amount is: {early_bird.calculate_bill(early_bird_items)}€\n")

# 14 create two flagships, get all menus
flagship_store = Franchise("1232 West End Road",early_bird)

# 17 test menu at 12am
print(flagship_store.print_menu(12))

# 18 test menu at 17 o'clock, 5pm
print(flagship_store.print_menu(17))
print("\n")
new_installment = Franchise("12 East Mulberry",brunch_menu)

# 23 create arepa franchise
arepa_place = Franchise("189 Fitzgerald Avenue",brunch_menu)
franchises = [flagship_store,new_installment]
name= "Basta Fazoolin\' with my Heart"
business = Business(name,franchises)
arepa_business = Business("Take a\' Arepa\'",[arepa_place])

