import asyncio
import goodwe
import sys

from argparse import ArgumentParser

async def get_inverter_data():
    arg_parser = ArgumentParser()
    arg_parser.add_argument('address', help='IP address of the inverter, e.g. 192.168.1.10')

    args = arg_parser.parse_args()

    inverter = await goodwe.connect(args.address)
    device_info = await inverter.read_device_info()
    sensor_data = await inverter.read_runtime_data()

    measurement_data = "solar-data "

    for sensor in inverter.sensors():
        if (sensor.id_ in sensor_data):
            # print(f"{sensor.id_}: \t\t {sensor.name} = {sensor_data[sensor.id_]} {sensor.unit}")

            if (not sensor.id_.__eq__("timestamp")):
                is_string = len(sensor.unit) == 0
                field_value = "\"" + str(sensor_data[sensor.id_]).replace('"','\\"') + "\"" if is_string else str(sensor_data[sensor.id_])
                measurement_data = measurement_data + f"{sensor.id_}={field_value},"

    measurement_data = measurement_data[:-1] + " " + str(int(sensor_data["timestamp"].timestamp()))

    print(measurement_data)

asyncio.run(get_inverter_data())
