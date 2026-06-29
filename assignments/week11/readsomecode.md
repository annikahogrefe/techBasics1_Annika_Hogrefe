### Read Some Code (& hopefully understand)

### 1. Where did you find the code and why did you choose it? (Provide the link)

* **https://github.com/erenaksu-x/Gym-App-phyton/blob/main/Gym%20App.py**
* found it on github when I looked for "phyton app gym" because that's what I'm planning to do for my final project. funny enough there was only one result which was perfect tho! very similar what I'm planning to do.
  
---

### 2. What does the program do? What's the general structure of the program?
* first the program asks for basic information about the user, then calculates BMI, asks for the goal of the user and gives them based on that a workout/diet plan.
  
---

### 3. Function analysis: pick one function and analyze it in detail:

'''phython
#normal BMI range : 18.5-24.9
min_ideal_weight = 18.5 * ( height**2 )
max_ideal_weight = 24.9 * (height **2)
#Body Mass Index (BMI) classification
def bmi_result(bmi):
   if bmi is None:
       return "invalid BMI value"
   if bmi < 18.5:
       gain_weight = min_ideal_weight - weight 
       return f"Your weight is below normal. You should gain at least {gain_weight} as much weight."
   elif 18.5 <= bmi <= 24.9:
       return ("Normal (ideal range, maintain your current weight)")
   elif 25 <= bmi < 29.9:
       lose_weight =  weight - max_ideal_weight
       return f"You are above your normal weight. You should lose at least {lose_weight} as much weight."
   else:
       return ("Obese (losing weight is important for your health)")

### What does this function do?
* assigns the calculated BMI to a weight category + tells the user how much weight they should gain/lose 

### What are the inputs and outputs?
* inputs: BMI (weight and height) as a float or int (I'm not sure) and gloabal varibles (min/max_ideal_weight)
* output: text message (string) containing weight classification + weight that should ideally be gained/lost

### How does it work (step by step)?
* if-elif-else structure
* first checks if input is valid, then checks if underweight, normal weight or overweight (based on BMI) and otherwise returns obese. 
* if the users BMI falls under under- or overweight the function calculates the weight that should be gained/lost by subtracting the current weight form the min ideal weight/ subracting max ideal weight from current weight

---

### 4. Takeaways: are there anything you can learn from the code? (How to structure your code, a clean solution for some function you might also need...)
* maybe a godd basic structure to start with, since I'm still a bit scared of an empty file haha

### 5. What parts of the code were confusing or difficult at the beginning to understand?
### Were you able to understand what it is doing after your own research?
* was very simple to be honest, might have been smarter to choose something diffrent to learn more new stuff but I was so happy to see someone already did something like I had in mind
 
---

### Extra notes
* I want my code to be a lot more complex that that and add some more features and focus more on building an actual workout plan with specific exercises :)
