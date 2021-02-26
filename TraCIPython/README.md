SUMO TraCI using `python` API 
======================

pre-requisite
-------------
1. You need `python3`.
2. Install `traci` API for python with `pip`
```
pip install traci
```

The route file
--------------
Generates traffic that goes from East to West. All vehicles enter the simulation at the right lane for simplicity.


I created a `Makefile`. You can run
```
make gui
```
To run normal GUI simulation. Vehicles start in the right lane going east to west. Sometimes vehicles change their lane.

You can then try `traci`, in which I have a command that stops a vehicle at the 100th second.
```
./traci_connector.py
```
Which should start SUMO GUI interface. Click the `play` button to start the simulation. At the 100th second, a vehicle will stop by decelerating to zero speed. Other vehicles will go around it.