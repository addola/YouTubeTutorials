#!/usr/bin/env python3

import traci
import os

sumo_home = os.getenv('SUMO_HOME', '/usr/bin')
sumo_binary =  sumo_home + "/bin/sumo-gui"
sumo_cmd = [sumo_binary, "-c", "sim.sumocfg"]

traci.start (sumo_cmd)

stopped_id = ''
while True:
   traci.simulationStep () # Step one second 
   
   sim_time = traci.simulation.getTime()
   id_list = traci.vehicle.getIDList ()
   vehicle_count = len(id_list)
   #print ("Time %.2f \t There are %d vehicles in the simulation" % (sim_time, vehicle_count))
   '''
   At the 100th second, the oldest vehicle in simulation will be stopped.
   We do this by setting its speed to zero, and it will decelerate to reach that speed.
   You will notice that vehicles will move over to another lane because of this.
   '''
   if sim_time == 100: 
      stopped_id = id_list[0]
      print ('Stopping a vehicle %s at time %.2f' % (stopped_id,sim_time))   
      traci.vehicle.setSpeed(stopped_id, 0)
   '''
   After 100 seconds, the stopped vehicle will start moving again. 
   I set its velocity to 30m/s, so it will accelerate to reach that speed (but won't violate the speed limit of the road)
   '''
   if sim_time == 200: #move that vehicle again
      traci.vehicle.setSpeed (stopped_id, 30)
      print ('vehicle %s is moving again. Time %.2f' % (stopped_id,sim_time))   
      
   if sim_time >= 1000:
      break

print ("Ending python script")
traci.close()
exit