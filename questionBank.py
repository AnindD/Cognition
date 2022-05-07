import random 

PhysicsQuestions = [
"In a slap shot, a hockey player accelerates the puck from a velocity of 8.00 m/s to 40.0 m/s in the same direction. If this shot takes  3.33×10^−2s , calculate the distance over which the puck accelerates.",
"Freight trains can produce only relatively small accelerations and decelerations. (a) What is the final velocity of a freight train that accelerates at a rate of  0.0500 m/s^2  for 8.00 min, starting with an initial velocity of 4.00 m/s? (b) If the train can slow down at a rate of  0.550 m/s^2 , how long will it take to come to a stop from this velocity? (c) How far will it travel in each case?",
"A swan on a lake gets airborne by flapping its wings and running on top of the water. (a) If the swan must reach a velocity of 6.00 m/s to take off and it accelerates from rest at an average rate of  0.350 m/s^2 , how far will it travel before becoming airborne? (b) How long does this take?",
"An unwary football player collides with a padded goalpost while running at a velocity of 7.50 m/s and comes to a full stop after compressing the padding and his body 0.350 m. (a) What is his deceleration? (b) How long does the collision last?",
"Consider a grey squirrel falling out of a tree to the ground. (a) If we ignore air resistance in this case (only for the sake of this problem), determine a squirrel's velocity just before hitting the ground, assuming it fell from a height of 3.0 m. (b) If the squirrel stops in a distance of 2.0 cm through bending its limbs, compare its deceleration with that of the airman in the previous problem.",
"Dragsters can actually reach a top speed of 145 m/s in only 4.45 s. (a) Calculate the average acceleration for such a dragster. (b) Find the final velocity of this dragster starting from rest and accelerating at the rate found in (a) for 402 m (a quarter mile) without using any information on time. (c) Why is the final velocity greater than that used to find the average acceleration? Hint: Consider whether the assumption of constant acceleration is valid for a dragster. If not, discuss whether the acceleration would be greater at the beginning or end of the run and what effect that would have on the final velocity.",
"In 1967, New Zealander Burt Munro set the world record for an Indian motorcycle, on the Bonneville Salt Flats in Utah, with a maximum speed of 183.58 mi/h. The one-way course was 5.00 mi long. Acceleration rates are often described by the time it takes to reach 60.0 mi/h from rest. If this time was 4.00 s, and Burt accelerated at this rate until he reached his maximum speed, how long did it take Burt to complete the course?",
"(a) A world record was set for the men's 100-m dash in the 2008 Olympic Games in Beijing by Usain Bolt of Jamaica. Bolt “coasted” across the finish line with a time of 9.69 s. If we assume that Bolt accelerated for 3.00 s to reach his maximum speed, and maintained that speed for the rest of the race, calculate his maximum speed and his acceleration. (b) During the same Olympics, Bolt also set the world record in the 200-m dash with a time of 19.30 s. Using the same assumptions as for the 100-m dash, what was his maximum speed for this race?",
"Calculate the displacement and velocity at times of (a) 0.500, (b) 1.00, (c) 1.50, and (d) 2.00 s for a ball thrown straight up with an initial velocity of 15.0 m/s. Take the point of release to be  y0=0 .",
"A basketball referee tosses the ball straight up for the starting tip-off. At what velocity must a basketball player leave the ground to rise 1.25 m above the floor in an attempt to get the ball?",
"A dolphin in an aquatic show jumps straight up out of the water at a velocity of 13.0 m/s. (a) List the knowns in this problem. (b) How high does his body rise above the water? To solve this part, first note that the final velocity is now a known and identify its value. Then identify the unknown, and discuss how you chose the appropriate equation to solve for it. After choosing the equation, show your steps in solving for the unknown, checking units, and discuss whether the answer is reasonable. (c) How long is the dolphin in the air? Neglect any effects due to his size or orientation.",
"(a) Calculate the height of a cliff if it takes 2.35 s for a rock to hit the ground when it is thrown straight up from the cliff with an initial velocity of 8.00 m/s. (b) How long would it take to reach the ground if it is thrown straight down with the same speed?",
"You throw a ball straight up with an initial velocity of 15.0 m/s. It passes a tree branch on the way up at a height of 7.00 m. How much additional time will pass before the ball passes the tree branch on the way back down?",
"Standing at the base of one of the cliffs of Mt. Arapiles in Victoria, Australia, a hiker hears a rock break loose from a height of 105 m. He can't see the rock right away but then does, 1.50 s later. (a) How far above the hiker is the rock when he can see it? (b) How much time does he have to move before the rock hits his head?",
"There is a 250-m-high cliff at Half Dome in Yosemite National Park in California. Suppose a boulder breaks loose from the top of this cliff. (a) How fast will it be going when it strikes the ground? (b) Assuming a reaction time of 0.300 s, how long will a tourist at the bottom have to get out of the way after hearing the sound of the rock breaking loose (neglecting the height of the tourist, which would become negligible anyway if hit)? The speed of sound is 335 m/s on this day.",
"Suppose you drop a rock into a dark well and, using precision equipment, you measure the time for the sound of a splash to return. (a) Neglecting the time required for sound to travel up the well, calculate the distance to the water if the sound returns in 2.0000 s. (b) Now calculate the distance taking into account the time for sound to travel up the well. The speed of sound is 332.00 m/s in this well.",
". A coin is dropped from a hot-air balloon that is 300 m above the ground and rising at 10.0 m/s upward. For the coin, find (a) the maximum height reached, (b) its position and velocity 4.00 s after being released, and (c) the time before it hits the ground."
]
Solutions = [
"0.799 m",
"(a)  28.0 m/s  (b)  50.9 s  (c) 7.68 km to accelerate and 713 m to decelerate",
"(a)  51.4m (b)  17.1 s",
"(a)  −80.4m/s2  (b)  9.33×10^−2s",
"(a)  7.7 m/s  (b)  −15×10^2m/s^2 . This is about 3 times the deceleration of the pilots, who were falling from thousands of meters high!",
"(a)  32.6 m/s^2  (b)  162 m/s  (c)  v>vmax , because the assumption of constant acceleration is not valid for a dragster. A dragster changes gears, and would have a greater acceleration in first gear than second gear than third gear, etc. The acceleration would be greatest at the beginning, so it would not be accelerating at  32.6 m/s^2  during the last few meters, but substantially less, and the final velocity would be less than 162 m/s.",
"104 s",
"(a)  v=12.2 m/s ;  a=4.07 m/s2 (b)  v=11.2 m/s",
"(a)  y1=6.28 m ;  v1=10.1 m/s  (b)  y2=10.1 m ;  v2=5.20 m/s  (c)  y3=11.5 m ;  v3=0.300 m/s (d)  y4=10.4 m ;  v4=−4.60 m/s", 
"v0=4.95 m/s",
"a=−9.80 m/s^2 ;  v0=13.0 m/s ;  y0=0 m  (b)  v=0m/s . Unknown is distance  y  to top of trajectory, where velocity is zero. Use equation  v^2 = v0^2 + 2a(y−y0)  because it contains all known values except for  y , so we can solve for  y . Solving for  y  gives:\nv^2 - v0^2 = 2a(y-y0)\n(v^2 - v0^2)/2a = y - y0\ny = y0 + (v^2 - v0^2)/2a\ny = 0 + [(0 m/s)^2-(13.0 m/s)^2]/[2(-9.80m/s^2)]\ny = 8.26m\nDolphins measure about 2 meters long and can jump several times their length out of the water, so this is a reasonable result. (c)  2.65 s",
"(a) 8.26 m (b) 0.717 s",
"1.91 s",
"(a) 94.0 m (b) 3.13 s",
"(a) -70.0 m/s (downward) (b) 6.10 s",
"(a)  19.6 m  (b)  18.5 m",
"(a) 305 m (b) 262 m, -29.2 m/s (c) 8.91 s",
]
VectorQuestions = [ 
"A plane can travel with a speed of 80 mi/hr with respect to the air. Determine the resultant velocity of the plane (magnitude only) if it encounters:\na. 10 mi/hr headwind. \nb. 10 mi/hr tailwind. \nc. 10 mi/hr crosswind. \nd. 60 mi/hr crosswind.",
"A motorboat traveling 5 m/s, East encounters a current traveling 2.5 m/s, North. \na. What is the resultant velocity of the motor boat? \nb. If the width of the river is 80 meters wide, then how much time does it take the boat to travel shore to shore? \nc. What distance downstream does the boat reach the opposite shore?", 
"3. A motorboat traveling 5 m/s, East encounters a current traveling 2.5 m/s, South. \na. What is the resultant velocity of the motor boat? \n b. If the width of the river is 80 meters wide, then how much time does it take the boat to travel shore to shore? \n c. What distance downstream does the boat reach the opposite shore?"
]
VectorSolutions = [
"a. A headwind would decrease the resultant velocity of the plane to 70 mi/hr. \nb. A tailwind would increase the resultant velocity of the plane to 90 mi/hr. \nc. A 10 mi/hr crosswind would increase the resultant velocity of the plane to 80.6 mi/hr. This can be determined using the Pythagorean theorem: SQRT[ (80 mi/hr)2 + (10 mi/hr)2 ] )\nd. A 60 mi/hr crosswind would increase the resultant velocity of the plane to 100 mi/hr. This can be determined using the Pythagorean theorem: SQRT[ (80 mi/hr)2 + (60 mi/hr)2 ] )",
"a. The resultant velocity can be found using the Pythagorean theorem. The resultant is the hypotenuse of a right triangle with sides of 5 m/s and 2.5 m/s. It is SQRT[(5 m/s)2 + (2.5 m/s)2] = 5.59 m/s. Its direction can be determined using a trigonometric function. Direction = invtan [ (2.5 m/s) / (5 m/s)] = 26.6 degrees \nb. The time to cross the river is t = d / v = (80 m) / (5 m/s) = 16.0 s \nc. The distance traveled downstream is d = v • t = (2.5 m/s)*(16.0 s) = 40 m",
"a. The resultant velocity can be found using the Pythagorean theorem. The resultant is the hypotenuse of a right triangle with sides of 5 m/s and 2.5 m/s. It is SQRT [ (5 m/s)2 + (2.5 m/s)2 ] = 5.59 m/s Its direction can be determined using a trigonometric function.Direction = 360 degrees - invtan[ (2.5 m/s) / (5 m/s) ] = 333.4 degrees NOTE: the direction of the resultant velocity (like any vector) is expressed as the counterclockwise angle of rotation from due East. \nb. The time to cross the river is t = d / v = (80 m) / (5 m/s) = 16.0 s\nc. The distance traveled downstream is d = v • t = (2.5 m/s) • (16.0 s) = 40 m"
]

ForcesQuestions = [
"A 63.0-kg sprinter starts a race with an acceleration of 4.20 m/s2. What is the net external force on him?",
"A cleaner pushes a 4.50-kg laundry cart in such a way that the net external force on it is 60.0 N. Calculate the magnitude of its acceleration.",
"Suppose two children push horizontally, but in exactly opposite directions, on a third child in a wagon. The first child exerts a force of 75.0 N, the second a force of 90.0 N, friction is 12.0 N, and the mass of the third child plus wagon is 23.0 kg. (a) What is the system of interest if the acceleration of the child in the wagon is to be calculated? (b) Draw a free-body diagram, including all forces acting on the system. (c) Calculate the acceleration. (d) What would the acceleration be if friction were 15.0 N?",
"The rocket sled accelerates at a rate of  49.0m/s^2 . Its passenger has a mass of 75.0 kg. (a) Calculate the horizontal component of the force the seat exerts against his body. Compare this with his weight by using a ratio. (b) Calculate the direction and magnitude of the total force the seat exerts against his body.", 
"What net external force is exerted on a 1100-kg artillery shell fired from a battleship if the shell is accelerated at  2.40×10^4m/s^2 ? What is the magnitude of the force exerted on the ship by the artillery shell?",
"(a) Calculate the tension in a vertical strand of spider web if a spider of mass 8.00×10^−5kg hangs motionless on it. (b) Calculate the tension in a horizontal strand of spider web if the same spider sits motionless in the middle of it. The strand sags at an angle of 12º below the horizontal. Compare this with the tension in the vertical strand (find their ratio).",
"A 5.00×10^5-kg rocket is accelerating straight up. Its engines produce 1.250×10^7N of thrust, and air resistance is 4.50×10^6N. What is the rocket’s acceleration?",
"A freight train consists of two  8.00×10^4-kg  engines and 45 cars with average masses of  5.50×10^4kg  . (a) What force must each engine exert backward on the track to accelerate the train at a rate of  5.00×10^–2m/s^2  if the force of friction is  7.50×10^5N , assuming the engines exert identical forces? This is not a large frictional force for such a massive system. Rolling friction for trains is small, and consequently trains are very energy-efficient transportation systems. (b) What is the force in the coupling between the 37th and 38th cars (this is the force each exerts on the other), assuming all cars have the same mass and that friction is evenly distributed among all of the cars and engines?",
"A 76.0-kg person is being pulled away from a burning building as shown in Figure 4.40 (https://openstax.org/apps/archive/20220228.174637/resources/c1e1b868b916f63786905d5f951f8b72d56d4b17). Calculate the tension in the two ropes if the person is momentarily motionless. Include a free-body diagram in your solution.",
"A flea jumps by exerting a force of  1.20×10−5N  straight down on the ground. A breeze blowing on the flea parallel to the ground exerts a force of  0.500×10−6N  on the flea. Find the direction and magnitude of the acceleration of the flea if its mass is  6.00×10−7kg . Do not neglect the gravitational force.",
"A 1100-kg car pulls a boat on a trailer. (a) What total force resists the motion of the car, boat, and trailer, if the car exerts a 1900-N force on the road and produces an acceleration of  0.550 m/s^2 ? The mass of the boat plus trailer is 700 kg. (b) What is the force in the hitch between the car and the trailer if 80% of the resisting forces are experienced by the boat and trailer?",  
]
ForcesSolutions = [
"265 N", 
"13.3 m/s^2", 
"(a) The system is the child in the wagon plus the wagon. (c) a=0.130m/s^2 in the direction of the second child’s push.(d) a=0.00m/s^2",
"(a)  3.68×10^3 N.This force is 5.00 times greater than his weight.(b)  3750 N; 11.3ºabove horizontal",
"Force on shell:  2.64×107N Force exerted on ship =  −2.64×107N , by Newton’s third law",
"(a)  7.84×10−4N (b)  1.89×10–3N  . This is 2.41 times the tension in the vertical strand.",
"6.20 m/s^2",
"(a)  4.41×10^5N (b)  1.50×10^5N",
"T1=736 N T2=194 N",
"10.2m/s2, 4.67º from vertical",
"(a)  910 N (b)  1.11×10^3N",
]
EnergyQuestions = [
"Calculate the work done by an 85.0-kg man who pushes a crate 4.00 m up along a ramp that makes an angle of 20.0º with the horizontal (https://openstax.org/apps/archive/20220118.185250/resources/cd89f8d1f8ad4a55d07b4c2ebe5fb568b2ae98f7). He exerts a force of 500 N on the crate parallel to the ramp and moves at a constant speed. Be certain to include the work he does on the crate and on his body to get up the ramp.", # Question 1 
"Boxing gloves are padded to lessen the force of a blow. (a) Calculate the force exerted by a boxing glove on an opponent’s face, if the glove and face compress 7.50 cm during a blow in which the 7.00-kg arm and glove are brought to rest from an initial speed of 10.0 m/s. (b) Calculate the force exerted by an identical blow in the gory old days when no gloves were used and the knuckles and face would compress only 2.00 cm.", #Question 2
"A 60.0-kg skier with an initial speed of 12.0 m/s coasts up a 2.50-m-high rise as shown. Find her final speed at the top, given that the coefficient of friction between her skis and the snow is 0.0800. (Hint: Find the distance traveled up the incline assuming a straight-line path as shown in the figure.) (https://openstax.org/apps/archive/20220118.185250/resources/aa03854737d65448aa7406fad9c4e4f698329221)", # Question 3 
"(a) How high a hill can a car coast up (engine disengaged) if work done by friction is negligible and its initial speed is 110 km/h? (b) If, in actuality, a 750-kg car with an initial speed of 110 km/h is observed to coast up a hill to a height 22.0 m above its starting point, how much thermal energy was generated by friction? (c) What is the average force of friction if the hill has a slope  2.5º  above the horizontal?", #Question 4 
"In an amusement park, a car rolls in a track as shown below. Find the speed of the car at A, B, and C. Note that the work done by the rolling friction is zero since the displacement of the point at which the rolling friction acts on the tires is momentarily at rest and therefore has a zero displacement. (https://openstax.org/apps/archive/20220325.143432/resources/5af031008d5587f4330e7deb2fab26dbfc5b6b4d)", # Question 5 
"Suppose that the air resistance a car encounters is independent of its speed. When the car travels at 15 m/s, its engine delivers 20 hp to its wheels. (a) What is the power delivered to the wheels when the car travels at 30 m/s? (b) How much energy does the car use in covering 10 km at 15 m/s? At 30 m/s? Assume that the engine is 25% efficient. (c) Answer the same questions if the force of air resistance is proportional to the speed of the automobile. (d) What do these results, plus your experience with gasoline consumption, tell you about air resistance?", #Question 6 
"The two masses held together by a pulley, one being hold on the table, another being held off the table are released from rest. After the 3.0-kg mass has fallen 1.5 m, it is moving with a speed of 3.8 m/s. How much work is done during this time interval by the frictional force on the 2.0 kg mass?", # Question 7 
]
EnergySolutions = [
  "3.14×10^3 J", # Question 1 
  "a) 4.67 * 10^3 N b) 1.75 * 10^4 c)", # Question 2
  "9.46 m/s", # Question 3 
  "a) 47.8m b) -1.89 * 10^5 c) 375 N" # Question 4 
  "vA=24m/s; vB=14m/s; vC=31m/s", #Question 5 
  " a. 40 hp; b. 39.8 MJ, independent of speed; c. 80 hp, 79.6 MJ at 30 m/s; d. If air resistance is proportional to speed, the car gets about 22 mpg at 34 mph and half that at twice the speed, closer to actual driving experience.", # Question 6
  "Wf = -8 J", #Question 7 
]

