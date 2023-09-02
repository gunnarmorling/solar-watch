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

Create a Python virtual environment and install the required Python dependencies:

```bash
python3 -m venv .env
source .env/bin/activate
pip install goodwe
```

# License

This code base is available ander the Apache License, version 2.
