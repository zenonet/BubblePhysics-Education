# Python Library Documentation

## `connect()`

The connect-functions simply trys to connect to a BubblePhysics Instance. By default, it will try to connect to localhost at port `26541`. 
However, if you want to customise this, you can use these parameters:

- `ip`: A string which is a simple ip-address or domain to connect to.
- `port`: An int which specifies the port at which the library should look for a BubblePhysics Instance.

## `move()`

The move function accepts a tuple of 2 floats as input which specify the x and y movement.<br>
Note that this input will be used by BubblePhysics in every Timestep until `move()` is being called again.

## `aim()`

The aim function accepts a tuple of 2 floats which are interpreted as a directional vector which specifies the direction, in that the player should face.

## `shoot()`

The shoot function has a single bool as parameter which specifies if the player should shoot.

## `raycast()`

This will shoot an invisible ray out of the gun barrel which can only hit walls (enemies and bullets will be ignored).
The raycast function then returns the distance the ray tranvelled until it hit a wall. If the ray didn't hit anything after travelling, the function will return 0.<br>
The return value is the distance in unity units.
