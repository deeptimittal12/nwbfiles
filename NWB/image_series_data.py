from datetime import datetime
from dateutil.tz import tzlocal

import numpy as np

import pynwb
from pynwb.ophys import ImageSeries, OpticalChannel
from pynwb.device import Device

start_time = datetime(2019, 1, 1, 11, tzinfo=tzlocal())

nwbfile = pynwb.NWBFile('Example imaging data', 'EXAMPLE_ID', datetime.now(tzlocal()),
                  experimenter='Padraig Gleeson',
                  lab='Silver Lab',
                  institution='UCL',
                  experiment_description=('Images generated from a simulation generated by neuroConstruct'),
                  session_id='nC')
                  
'''
device = Device('PovRay')
nwbfile.add_device(device)
optical_channel = OpticalChannel('my_optchan', 'description', 500.)

imaging_plane = nwbfile.create_imaging_plane('my_imgpln', optical_channel, 'cerebellum',
                                             device, 600., 300., 'neuroConstruct', 'cerebellum',
                                             np.ones((5, 5, 3)), 4.0, 'manifold unit', 'A frame to refer to')'''
                                             
ext_files = []
for i in range(82):
    ext_files.append('images/MyNetwork_T%i.png'%i)
    
image_series = ImageSeries(name='test_image_series', dimension=[2],
                               external_file=ext_files,
                               starting_frame=[0], 
                               format='png', 
                               starting_time=0.0, 
                               rate=0.001,
                               description='Series of images from a simulation of the cerebellum via neuroConstruct')
                               
nwbfile.add_acquisition(image_series)


nwb_file_name = 'image_series_data.nwb'
io = pynwb.NWBHDF5IO(nwb_file_name, mode='w')
io.write(nwbfile)
io.close()
print("Written NWB file to %s"%nwb_file_name)
