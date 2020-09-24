SUMO Simulation Examples
========================

In this example, I created multiple `SUMO` simulations that you can run to generate traces that can be used in `ns-3`.

The examples contain a `Makefile` that can automate the process for you, but before you are able to use it, you need to make some changes to `~/.bashrc`

If you installed `sumo` using `apt-get install`, then `SUMO_HOME` should be set as follows:
```bash
export SUMO_HOME=/usr/share/sumo
export PATH=$PATH:$SUMO_HOME/bin:$SUMO_HOME/tools
```

If you installed `sumo` by building sources, then set `SUMO_HOME` accordingly
```bash
export SUMO_HOME=/path/to/sumo
```

Every folder contains a `Makefile` that you can modify to your needs.