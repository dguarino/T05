# -*- coding: utf-8 -*-
"""
This is implementation of basic SpatioTemporal FIlters in Retina+LGN
"""
import sys
from pyNN import nest
from mozaik.controller import run_workflow, setup_logging
import mozaik
from model import T05_Model
from experiments import create_experiments
from mozaik.storage.datastore import Hdf5DataStore,PickledDataStore
from analysis_and_visualization import perform_analysis_and_visualization
from parameters import ParameterSet


try:
    from mpi4py import MPI
except ImportError:
    MPI = None
if MPI:
    mpi_comm = MPI.COMM_WORLD
MPI_ROOT = 0

logger = mozaik.getMozaikLogger()

print sys.argv

if False:
    data_store,model = run_workflow( 'T05', T05_Model, create_experiments )
    model.connectors['LGN_PGN_ConnectionOn'].store_connections(data_store)    
    model.connectors['LGN_PGN_ConnectionOff'].store_connections(data_store)    
    model.connectors['PGN_PGN_Connection'].store_connections(data_store)    
    model.connectors['PGN_LGN_ConnectionOn'].store_connections(data_store)    
    model.connectors['PGN_LGN_ConnectionOff'].store_connections(data_store)    

else: 
    setup_logging()
    data_store = PickledDataStore(
        load=True,
        parameters=ParameterSet({ 'store_stimuli':False, 'root_directory':'T05_data_____' })
        ,replace=True
    )
    logger.info('Loaded data store')


if mpi_comm.rank == MPI_ROOT:
    perform_analysis_and_visualization(data_store)
