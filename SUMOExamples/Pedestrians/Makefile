
BOLD_BLACK='\033[1;32m'       # Black
END_COLOR='\033[0m'

SIM_TIME=600


all: trips trace

trace:
	echo "$(date) : Creating SUMO trace" 
	sumo -c sim.sumocfg --fcd-output sumoTrace.xml
	echo "Make NS2 $(date)"
	python $(SUMO_HOME)/tools/traceExporter.py --fcd-input sumoTrace.xml --ns2mobility-output ns2mobility.tcl

trips:
	@echo "$(BOLD_BLACK)Making random trips$(END_COLOR)"
	
	python $(SUMO_HOME)/tools/randomTrips.py -n map.net.xml -r bus_routes.rou.xml  -o bus_trips.xml -e $(SIM_TIME) -p 30 --vehicle-class bus --trip-attributes="accel=\"0.8\""
	python $(SUMO_HOME)/tools/randomTrips.py -n map.net.xml -r truck_routes.rou.xml  -o truck_trips.xml -e $(SIM_TIME) -p 15 --vehicle-class truck --trip-attributes="color=\"179,223,183\""
	python $(SUMO_HOME)/tools/randomTrips.py -n map.net.xml -r delivery_routes.rou.xml  -o delivery_trips.xml -e $(SIM_TIME) -p 30 --vehicle-class delivery --trip-attributes="color=\"115,211,230\""
	python $(SUMO_HOME)/tools/randomTrips.py -n map.net.xml -r passenger_routes.rou.xml  -o passenger_trips.xml -e $(SIM_TIME) -p 0.1 --vehicle-class passenger --trip-attributes="color=\"255,255,255\""
	python $(SUMO_HOME)/tools/randomTrips.py -n map.net.xml -r trailer_routes.rou.xml  -o trailer_trips.xml -e $(SIM_TIME) -p 150 --vehicle-class trailer --trip-attributes="color=\"223,179,180\" accel=\"0.5\""
	python $(SUMO_HOME)/tools/randomTrips.py -n map.net.xml -r ped_routes.rou.xml  -o ped_trips.xml -e $(SIM_TIME) -p 5 --pedestrians



	# If we have multiple route files, vehicle must have unique ids, so we use sed to replace text in these files. 
	sed -i "s/vehicle id=\"/vehicle id=\"bus/g" bus_routes.rou.xml
	sed -i "s/vehicle id=\"/vehicle id=\"truck/g" truck_routes.rou.xml
	sed -i "s/vehicle id=\"/vehicle id=\"pass/g" passenger_routes.rou.xml
	sed -i "s/vehicle id=\"/vehicle id=\"deliv/g" delivery_routes.rou.xml
	sed -i "s/vehicle id=\"/vehicle id=\"trailer/g" trailer_routes.rou.xml

sim:
	sumo-gui sim.sumocfg

osm:
	netconvert --osm-files map.osm -o map.net.xml

clean:
	rm -f sumoTrace.xml ns2mobility.tcl
	rm -f *.rou.xml *.rou.alt.xml *trips.xml

