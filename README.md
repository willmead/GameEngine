# ECS Kobold Engine


## Now

* Improve Physics System Collisions
    * Currently they works perfectly in one dimension along the y-axis
    * Implement a more complex algorithm to stop / bounce at multiple angles

## Soon

* First Game: PONG!
    * Create 2 paddle entities
        * ShapeSprite, KeyboardController, Collider(Bounce), Velocity, Position
    * Create 1 ball entity
        * ShapeSprite, Velocity, Position, Collider(Passing)
    * Create 4 wall entities
        * ShapeSprite, Position, Collider(Bounce)


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

* Rewrite Input System To Make Custom Button Mapping Easier
    * Input Component Describes Possible Actions
    * Keyboard Component Matches Buttons To Actions in Input Component

* Text Components / Data Components
    * For storing a score or timer variable for example.
    * Interaction Components could update these.



