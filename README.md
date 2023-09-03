# Solar Watch

This project contains scripts and configuration for retrieving the data from a GoodWe solar inverter, storing it in InfluxDB and visualizing it via Grafana.
It is meant for being run on a Raspberry Pi.

## Setting Up the Raspberry Pi

_Note: I have a Raspberry Pi 4 8 GB RAM with Raspberry Pi OS 64 Bit, but other configurations may work as well._

### Installing the OS

Use the [Raspberry PI OS Imager](https://www.raspberrypi.com/software/) for setting up your PI.
Make sure to enable SSH access and WiFi and use _raspberrypi.local_ as host name.

### Provisioning the Required Software

Clone the project on some other machine (i.e. not the Pi):

```bash
git clone git@github.com:gunnarmorling/solar-watch.git
cd solar-watch
```

Then install the required software on the Pi using Ansible and the provided _playbook.yml_ file (adjust the _hosts_ file as needed):

```bash
ansible-playbook -i ansible/hosts ansible/playbook.yml
```

## Initializing the Project

SSH into the Pi:

```bash
ssh -i ~/.ssh/<your key> pi@raspberrypi.local
```

On the Pi, clone the project:

```bash
git clone https://github.com/gunnarmorling/solar-watch.git
cd solar-watch
```

Start InfluxDB and Grafana:

```bash
docker compose up -d
```

Create a Python virtual environment and install the required Python dependencies:

```bash
python3 -m venv .env
source .env/bin/activate
pip install goodwe
```

Change `INVERTER_ADDRESS` in _post-data.sh_ to the address of your inverter.

Invoke _post-data.sh_ and verify data shows up in InfluxDB and Grafana (see below for endpoints).
If it does, register crontab entries for your desired logging cadence:

```bash
crontab -e

# E.g. like this for logging every 30 sec
* * * * * /home/pi/projects/solar-watch/post-data.sh >> /tmp/solar-watch.log 2>&1
* * * * * sleep 30 && /home/pi/projects/solar-watch/post-data.sh >> /tmp/solar-watch.log 2>&1
```

## Web Interfaces

Use username "admin" and password "adminadmin" for authenticating with both InfluxDB and Grafana.
These are the endpoints:

* InfluxDB: http://raspberrypi.local:8086/
* Grafana: http://raspberrypi.local:3000/

## Useful Commands

* Updating all packages:

```bash
sudo apt update
sudo apt full-upgrade
```

* Exporting and importing data from/into InfluxDB (run from within the Influx container via `docker exec --tty -i solar-watch-influxdb-1 bash`):

```bash
influxd inspect export-lp \
  --bucket-id 7f830c08c8b564f3 \
  --engine-path /var/lib/influxdb2/engine \
  --output-path /tmp/solar-data/export.lp \
  --compress
```

```bash
influx write \
  -b solar-data \
  -o solar-watch \
  -p ns \
  --format=lp \
  -f /tmp/solar-data/export-lp \
  --compression=gzip
```

## License

This code base is available ander the Apache License, version 2.
