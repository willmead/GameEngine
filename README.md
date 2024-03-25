# ECS Kobold Engine


## Now

* Acceleration -> Gravity
    * The Movement / Acceleration Systems are currently broken.
    * I was able to get them to work up until a collision occurs, it seems we may need to revisit the collision system.


## Soon

* I believe the code could be significantly improved by having systems inject events into each other.
    * That said, a lot of advice online seems to be very anti-events so I need to do a little more research.
    

## At Some Point

* Lighting
    * Not sure how to do this without arcade. Need to investigate what lighting actually is. 

* Particles
    * These would just be small ShapeSprites that are given random velocities and then fade?

* Animation
    * Entities can have an animation component which is basically just a mapping of animation frames to different states.
    * The animation System then chooses the appropriate state based on movement / combat
    * Then it moves the frames along after a timer

* Interaction System Works But Needs Tidying


# Notes
## Collisions / Physics Engine

### 25/03/24
Some good work this morning on collisions. Have started builing a simple physics engine that works like this:

* increments an entity along a straight line towards a target 
* continually check for collisions
* upon a collision stop movement
* upon reaching destination stop movement

This is a good first basic use case. Next tasks: 
* fit it into my current ECS model
* check that it works as intended (player should stop very close to blocker but not get stuck)

Then after:
* Implement different types of collisions
    * pass through
    * slide (like Mario)
    * bounce (like pong)



