import sys
import numpy
from parameters import ParameterSet
from mozaik.models import Model
from mozaik import load_component
from mozaik.space import VisualRegion

from mozaik.connectors.modular import ModularSamplingProbabilisticConnector



class T05_Model(Model):
    
    required_parameters = ParameterSet({
        'pgn' : ParameterSet, 
        'retina_lgn' : ParameterSet ,
        'visual_field' : ParameterSet 
    })
    
    def __init__(self, sim, num_threads, parameters):
        Model.__init__(self, sim, num_threads, parameters)   

        # Load components
        RetinaLGN = load_component( self.parameters.retina_lgn.component )
        PGN = load_component( self.parameters.pgn.component )
  
        # Build and instrument the network
        self.visual_field = VisualRegion(
            location_x = self.parameters.visual_field.centre[0],
            location_y = self.parameters.visual_field.centre[1],
            size_x = self.parameters.visual_field.size[0],
            size_y = self.parameters.visual_field.size[1]
        )
        # init layers
        self.input_layer = RetinaLGN( self, self.parameters.retina_lgn.params )
        pgn = PGN(self, self.parameters.pgn.params)


        ########################################################
        # LGN-PGN
        ModularSamplingProbabilisticConnector(
            self,
            'LGN_PGN_ConnectionOn',                     # name
            self.input_layer.sheets['X_ON'],            # source
            pgn,                                        # target
            self.parameters.pgn.LGN_PGN_ConnectionOn    # params
        ).connect()

        ModularSamplingProbabilisticConnector(
            self,
            'LGN_PGN_ConnectionOff',                    # name
            self.input_layer.sheets['X_OFF'],           # source
            pgn,                                        # target
            self.parameters.pgn.LGN_PGN_ConnectionOff   # params
        ).connect()

        ModularSamplingProbabilisticConnector(
            self,
            'PGN_PGN_Connection',                       # name
            pgn,                                        # source
            pgn,                                        # target
            self.parameters.pgn.PGN_PGN_Connection      # params
        ).connect()

        ModularSamplingProbabilisticConnector(
            self,
            'PGN_LGN_ConnectionOn',                     # name
            pgn,                                        # source
            self.input_layer.sheets['X_ON'],            # target
            self.parameters.pgn.PGN_LGN_ConnectionOn    # params
        ).connect()

        ModularSamplingProbabilisticConnector(
            self,
            'PGN_LGN_ConnectionOff',                    # name
            pgn,                                        # source
            self.input_layer.sheets['X_OFF'],           # target
            self.parameters.pgn.PGN_LGN_ConnectionOff   # params
        ).connect()


        ########################################################
        # # THALAMO-CORTICAL
        # GaborConnector(
        #     self,
        #     self.input_layer.sheets['X_ON'],
        #     self.input_layer.sheets['X_OFF'],
        #     cortex_exc_l4,                                      # target
        #     self.parameters.l4_cortex_exc.AfferentConnection,   # parameters
        #     'V1AffConnection'                                  # name
        # )

        # GaborConnector(
        #     self,
        #     self.input_layer.sheets['X_ON'],
        #     self.input_layer.sheets['X_OFF'],
        #     cortex_inh_l4,
        #     self.parameters.l4_cortex_inh.AfferentConnection,
        #     'V1AffInhConnection'
        # )


        ########################################################
        # # CORTICO-CORTICAL
        # ModularSamplingProbabilisticConnector(
        #     self,
        #     'V1L4ExcL4ExcConnection',
        #     cortex_exc_l4,
        #     cortex_exc_l4,
        #     self.parameters.l4_cortex_exc.L4ExcL4ExcConnection
        # ).connect()

        # ModularSamplingProbabilisticConnector(
        #     self,
        #     'V1L4ExcL4InhConnection',
        #     cortex_exc_l4,
        #     cortex_inh_l4,
        #     self.parameters.l4_cortex_exc.L4ExcL4InhConnection
        # ).connect()

        # ModularSamplingProbabilisticConnector(
        #     self,
        #     'V1L4InhL4ExcConnection',
        #     cortex_inh_l4,
        #     cortex_exc_l4,
        #     self.parameters.l4_cortex_inh.L4InhL4ExcConnection
        # ).connect()

        # ModularSamplingProbabilisticConnector(
        #     self,
        #     'V1L4InhL4InhConnection',
        #     cortex_inh_l4,
        #     cortex_inh_l4,
        #     self.parameters.l4_cortex_inh.L4InhL4InhConnection
        # ).connect()


        ########################################################
        # # CORTICO-THALAMIC
        # ModularSamplingProbabilisticConnector(
        #     self,
        #     'V1EffConnectionOn',
        #     cortex_exc_l4,
        #     self.input_layer.sheets['X_ON'],
        #     self.parameters.l4_cortex_exc.EfferentConnection
        # ).connect()

        # ModularSamplingProbabilisticConnector(
        #     self,
        #     'V1EffConnectionOff',
        #     cortex_exc_l4,
        #     self.input_layer.sheets['X_OFF'],
        #     self.parameters.l4_cortex_exc.EfferentConnection
        # ).connect()
