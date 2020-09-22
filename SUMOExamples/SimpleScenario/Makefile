
BOLD_BLACK='\033[1;30m'       # Black
END_COLOR='\033[0m'

all: trips trace

trace:
	echo "$(date) : Creating SUMO trace" 
	sumo -c sim.sumocfg --fcd-output sumoTrace.xml
	echo "Make NS2 $(date)"
	python $(SUMO_HOME)/tools/traceExporter.py --fcd-input sumoTrace.xml --ns2mobility-output ns2mobility.tcl

trips:
	echo "$(date) : Making trips" 
	python $(SUMO_HOME)/tools/randomTrips.py -n map.net.xml -r routes.rou.xml  -o trips.xml -e 600 -p 0.2


clean:
	rm -f sumoTrace.xml ns2mobility.tcl
	rm -f routes.rou.xml routes.rou.alt.xml trips.xml

