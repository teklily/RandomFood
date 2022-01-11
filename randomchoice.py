    import random
    lunch=["Peaunt butter and chocolate chip sandwich","nuggets",,"Pizza","Seitan stir fry","PB+Jelly","lunchable","toasted sandwich","something new"]
    breakfast=["Pop Tart","Kale Smoothie","Waffle","Streudel","pancakes","something new"]
    snack=["yogurt","cheese","banana","turkey","apple"]
    dinner=["seitan stir fry","baby pizza","pb+j","nuggets"]
    mommasays=["Eat up!! hearts hearts hearts","B'lanna says eat!!!","Meow","<3 <3 <3 <3"]
    def meal_sentence():
        while True:
            Meal = input("What meal would you like suggestions for? Options: breakfast, lunch, dinner or snack, press return to end: ")
            cute = (random.choice(mommasays))
            if Meal == "lunch":
                Meal = random.choice(lunch)  
                lunch_sentence =  Meal + "!!    BTW, " + cute + "!"
                print(lunch_sentence)
                break
            if Meal == "breakfast":
                Meal = random.choice(breakfast)
                breakfast_sentence =  Meal + "!!   BTW, " + cute + "!"
                break
            if Meal == "snack":
                Meal = random.choice(snack)
                snack_sentence =  Meal + "!!   BTW, " + cute + "!"
              #  snack_sentence = Meal.capitalize()
                print(snack_sentence) 
                break
            if Meal == "dinner":
                Meal = random.choice(dinner)
                dinner_sentence =  Meal + "!!   BTW, " + cute + "!"
                #dinner_sentence = Meal.capitalize()
                print(dinner_sentence) 
                break
            
            if Meal == "":
                break
           
