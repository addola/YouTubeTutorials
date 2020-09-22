BOLD_BLACK='\033[1;32m'       # Black
END_COLOR='\033[0m'

SIM_TIME=3600

#Generate a White passenger car every 1 second
PASS_PARAMS=-e $(SIM_TIME) -p 1 --vehicle-class passenger --trip-attributes="color=\"255,255,255\""
#Generate a bus every 30 seconds that has acceleration 0.8 m/s^2
BUS_PARAMS=-e $(SIM_TIME) -p 30 --vehicle-class bus --trip-attributes="accel=\"0.8\""
#Generate a truck every 15 seconds
TRUCK_PARAMS=-e $(SIM_TIME) -p 15 --vehicle-class truck --trip-attributes="color=\"179,223,183\""
#Generate a trailer every 150 seconds
TRAILER_PARAMS=-e $(SIM_TIME) -p 150 --vehicle-class trailer --trip-attributes="color=\"223,179,180\" accel=\"0.5\""
#Generate a delivery car every 30 seconds
DELIVERY_PARAMS=-e $(SIM_TIME) -p 30 --vehicle-class delivery --trip-attributes="color=\"115,211,230\""

all: trips trace

trace:
	@echo "\033[34m Creating a SUMO trace \033[0m"
	sumo -c sim.sumocfg --fcd-output sumoTrace.xml

	@echo "\033[92m Exporting to ns-2 trace \033[0m"
	traceExporter.py --fcd-input sumoTrace.xml --ns2mobility-output ns2mobility.tcl

trips:

	@echo "\033[92m Making Trips \033[0m"

	randomTrips.py -n map.net.xml -r bus_routes.rou.xml  -o bus_trips.xml $(BUS_PARAMS)
	randomTrips.py -n map.net.xml -r truck_routes.rou.xml  -o truck_trips.xml $(TRUCK_PARAMS)
	randomTrips.py -n map.net.xml -r delivery_routes.rou.xml  -o delivery_trips.xml $(DELIVERY_PARAMS)
	randomTrips.py -n map.net.xml -r passenger_routes.rou.xml  -o passenger_trips.xml $(PASS_PARAMS)
	randomTrips.py -n map.net.xml -r trailer_routes.rou.xml  -o trailer_trips.xml $(TRAILER_PARAMS)

	@echo "\033[92m Creating unique IDs in route files \033[0m"

	sed -i "s/vehicle id=\"/vehicle id=\"bus/g" bus_routes.rou.xml
	sed -i "s/vehicle id=\"/vehicle id=\"truck/g" truck_routes.rou.xml
	sed -i "s/vehicle id=\"/vehicle id=\"pass/g" passenger_routes.rou.xml
	sed -i "s/vehicle id=\"/vehicle id=\"deliv/g" delivery_routes.rou.xml
	sed -i "s/vehicle id=\"/vehicle id=\"trailer/g" trailer_routes.rou.xml

buildmap:
	netconvert --node-files=nodes.nod.xml --edge-files=edges.edg.xml --output-file=map.net.xml

osm:
	netconvert  --osm-files map.osm -o map.net.xml

sim:
	sumo-gui sim.sumocfg

clean:
	rm -f sumoTrace.xml ns2mobility.tcl
	rm -f *.rou.xml *.rou.alt.xml *trips.xml