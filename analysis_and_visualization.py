import numpy
import mozaik
import pylab
from mozaik.visualization.plotting import *
from mozaik.analysis.technical import NeuronAnnotationsToPerNeuronValues
from mozaik.analysis.analysis import *
from mozaik.analysis.vision import *
from mozaik.storage.queries import *
from mozaik.storage.datastore import PickledDataStore


def perform_analysis_and_visualization(data_store):
    analog_PGN_ids = sorted( param_filter_query(data_store,sheet_name="PGN").get_segments()[0].get_stored_vm_ids() )
    print analog_PGN_ids
    analog_Xon_ids = sorted( param_filter_query(data_store,sheet_name="X_ON").get_segments()[0].get_stored_vm_ids() )
    print analog_Xon_ids
    analog_Xoff_ids = sorted( param_filter_query(data_store,sheet_name="X_OFF").get_segments()[0].get_stored_vm_ids() )
    print analog_Xoff_ids

    # CONNECTIVITY PLOT
    # # LGN On -> PGN: 'LGN_PGN_ConnectionOn'
    # ConnectivityPlot(
    #     data_store,
    #     ParameterSet({
    #         'neuron': analog_Xon_ids[0],  # the target neuron whose connections are to be displayed
    #         'reversed': False,  # False: outgoing connections from the given neuron are shown. True: incoming connections are shown
    #         'sheet_name': 'X_ON',  # for neuron in which sheet to display connectivity
    #     }),
    #     fig_param={'dpi':100, 'figsize': (10,12)},
    #     plot_file_name='LGN_On_'+str(analog_Xon_ids[0])+'_outgoing.png'
    # ).plot({})    
    # # LGN Off -> PGN: 'LGN_PGN_ConnectionOff'
    # ConnectivityPlot(
    #     data_store,
    #     ParameterSet({
    #         'neuron': analog_Xoff_ids[0],  # the target neuron whose connections are to be displayed
    #         'reversed': False,  # False: outgoing connections from the given neuron are shown. True: incoming connections are shown
    #         'sheet_name': 'X_OFF',  # for neuron in which sheet to display connectivity
    #     }),
    #     fig_param={'dpi':100, 'figsize': (10,12)},
    #     plot_file_name='LGN_Off_'+str(analog_Xoff_ids[0])+'_outgoing.png'
    # ).plot({})    
    
    # # PGN lateral: 'PGN_PGN_Connection'
    # ConnectivityPlot(
    #     data_store,
    #     ParameterSet({
    #         'neuron': analog_PGN_ids[0],  # the target neuron whose connections are to be displayed
    #         'reversed': False,  # False: outgoing connections from the given neuron are shown. True: incoming connections are shown
    #         'sheet_name': 'PGN',  # for neuron in which sheet to display connectivity
    #     }),
    #     fig_param={'dpi':100, 'figsize': (24,12)},
    #     plot_file_name='PGN_Connections.png'
    # ).plot({})    

    # # PGN -> LGN On: 'PGN_LGN_ConnectionOn'
    # ConnectivityPlot(
    #     data_store,
    #     ParameterSet({
    #         'neuron': analog_Xon_ids[0],  # the target neuron whose connections are to be displayed
    #         'reversed': True,  # False: outgoing connections from the given neuron are shown. True: incoming connections are shown
    #         'sheet_name': 'X_ON',  # for neuron in which sheet to display connectivity
    #     }),
    #     fig_param={'dpi':100, 'figsize': (10,12)},
    #     plot_file_name='LGN_On_'+str(analog_Xon_ids[0])+'_incoming.png'
    # ).plot({})    
    # # PGN -> LGN On: 'PGN_LGN_ConnectionOff'
    # ConnectivityPlot(
    #     data_store,
    #     ParameterSet({
    #         'neuron': analog_Xoff_ids[0],  # the target neuron whose connections are to be displayed
    #         'reversed': True,  # False: outgoing connections from the given neuron are shown. True: incoming connections are shown
    #         'sheet_name': 'X_OFF',  # for neuron in which sheet to display connectivity
    #     }),
    #     fig_param={'dpi':100, 'figsize': (10,12)},
    #     plot_file_name='LGN_Off_'+str(analog_Xoff_ids[0])+'_incoming.png'
    # ).plot({})    


 
    if True: # ---- ANALYSIS ----
        
        # SPONTANEOUS ACTIVITY, LUMINANCE SENSITIVITY
        # dsv01 = param_filter_query( data_store, st_name='Null', sheet_name='X_ON' )  
        # TrialAveragedFiringRate( dsv01, ParameterSet({}) ).analyse()
        # dsv02 = param_filter_query( data_store, st_name='Null', sheet_name='X_OFF' )  
        # TrialAveragedFiringRate( dsv02, ParameterSet({}) ).analyse()

        # CONTRAST SENSITIVITY, SPATIAL AND TEMPORAL FREQUENCY TUNING, SPARSENESS
        # dsv10 = param_filter_query( data_store, st_name='FullfieldDriftingSinusoidalGrating', sheet_name='X_ON' )  
        # TrialAveragedFiringRate( dsv10, ParameterSet({}) ).analyse() # on responses
        # dsv11 = param_filter_query( data_store, st_name='FullfieldDriftingSinusoidalGrating', sheet_name='X_OFF' )  
        # TrialAveragedFiringRate( dsv11, ParameterSet({}) ).analyse() # on responses
        # dsv10 = param_filter_query( data_store, st_name='FullfieldDriftingSquareGrating', sheet_name='X_ON' )  
        # TrialAveragedFiringRate( dsv10, ParameterSet({}) ).analyse() # on responses
        # dsv11 = param_filter_query( data_store, st_name='FullfieldDriftingSquareGrating', sheet_name='X_OFF' )  
        # TrialAveragedFiringRate( dsv11, ParameterSet({}) ).analyse() # on responses
        ## X ON cell 
        # TrialAveragedSparseness( dsv10, ParameterSet({}) ).analyse() # on responses: Sparseness
        # Analog_MeanSTDAndFanoFactor( dsv10, ParameterSet({}) ).analyse() # on Vm: FanoFactor

        # SIZE TUNING
        dsv10 = param_filter_query( data_store, st_name='DriftingSinusoidalGratingDisk', sheet_name='X_ON' )  
        TrialAveragedFiringRate( dsv10, ParameterSet({}) ).analyse() # on responses
        dsv11 = param_filter_query( data_store, st_name='DriftingSinusoidalGratingDisk', sheet_name='X_OFF' )  
        TrialAveragedFiringRate( dsv11, ParameterSet({}) ).analyse() # on responses
        dsv12 = param_filter_query( data_store, st_name='FlatDisk', sheet_name='X_ON' )  
        TrialAveragedFiringRate( dsv12, ParameterSet({}) ).analyse() # on responses
        dsv13 = param_filter_query( data_store, st_name='FlatDisk', sheet_name='X_OFF' )  
        TrialAveragedFiringRate( dsv13, ParameterSet({}) ).analyse() # on responses
        
        # ORIENTATION TUNING
        # dsv20 = param_filter_query( data_store, st_name='FullfieldDriftingSinusoidalGrating', sheet_name='X_ON' ) 
        # TrialAveragedFiringRate( dsv20, ParameterSet({}) ).analyse()
        # dsv21 = param_filter_query( data_store, st_name='FullfieldDriftingSinusoidalGrating', sheet_name='X_OFF' ) 
        # TrialAveragedFiringRate( dsv21, ParameterSet({}) ).analyse()

        # CONTOUR COMPLETION
        # dsv30 = param_filter_query( data_store, st_name='FullfieldDriftingSquareGrating', sheet_name='X_ON')
        # TrialAveragedCorrectedCrossCorrelation( dsv30, ParameterSet({'bins':35,'bin_length':5.0,'neurons':analog_Xon_ids,'size':0.1}) ).analyse()
        # dsv31 = param_filter_query( data_store, st_name='FlashingSquares', sheet_name='X_ON')
        # TrialAveragedCorrectedCrossCorrelation( dsv31, ParameterSet({'bins':35,'bin_length':5.0,'neurons':analog_Xon_ids,'size':0.1}) ).analyse()


    if True: # ---- PLOTTING ----
        activity_plot_param = {
            'frame_rate' : 5,
            'bin_width' : 5.0,
            'scatter' :  True,
            'resolution' : 0
        }
        data_store.print_content( full_ADS=True )

        #----------------------
        # LUMINANCE SENSITIVITY  
        # firing rate against luminance levels              
        # #RetinalInputMovie( data_store, ParameterSet({}), plot_file_name="FlatLuminanceSensitivity_LGN",frame_duration=100).plot({'*.fontsize':7})
        # dsv = param_filter_query( data_store, st_name='Null', analysis_algorithm=['TrialAveragedFiringRate'] )
        # PlotTuningCurve(
        #   dsv,
        #   ParameterSet({
        #         'polar': False,
        #         'pool': False,
        #         'centered': False,
        #         'mean': False,
        #         'parameter_name' : 'background_luminance', 
        #         'neurons': list(analog_Xon_ids[0:1]), 
        #         'sheet_name' : 'X_ON'
        #   }), 
        #   fig_param={'dpi' : 100,'figsize': (8,8)}, 
        #   plot_file_name="FlatLuminanceSensitivity_LGN_On.png"
        # ).plot({
        #   '*.y_lim':(0,100), 
        #   #'*.y_lim':(0,30), 
        #   # '*.x_lim':(-10,100), 
        #   '*.fontsize':17
        # })
        # PlotTuningCurve(
        #   dsv,
        #   ParameterSet({
        #         'polar': False,
        #         'pool': False,
        #         'centered': False,
        #         'mean': False,
        #         'parameter_name' : 'background_luminance', 
        #         'neurons': list(analog_Xoff_ids[0:1]), 
        #         'sheet_name' : 'X_OFF'
        #   }), 
        #   fig_param={'dpi' : 100,'figsize': (8,8)}, 
        #   plot_file_name="FlatLuminanceSensitivity_LGN_Off.png"
        # ).plot({
        #   '*.y_lim':(0,100), 
        #   #'*.y_lim':(0,30), 
        #   # '*.x_lim':(-10,100), 
        #   '*.fontsize':17
        # })


        #--------------------
        ## CONTRAST SENSITIVITY
        ## firing rate against contrast levels
        # #RetinalInputMovie( data_store, ParameterSet({}), plot_file_name="ContrastSensitivity_LGN",frame_duration=100).plot({'*.fontsize':7})
        # dsv = param_filter_query( data_store, st_name='FullfieldDriftingSinusoidalGrating', analysis_algorithm=['TrialAveragedFiringRate'] )
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #         'polar': False,
        #         'pool': False,
        #         'centered': False,
        #         'mean': False,
        #         'parameter_name' : 'contrast', 
        #         'neurons': list(analog_Xon_ids[0:1]), 
        #         'sheet_name' : 'X_ON'
        #    }), 
        #    fig_param={'dpi' : 100,'figsize': (8,8)}, 
        #    plot_file_name="ContrastSensitivity_LGN_On.png"
        # ).plot({
        #    '*.y_lim':(0,100), 
        #    # '*.x_scale':'log', '*.x_scale_base':10,
        #    '*.fontsize':17
        # })
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #         'polar': False,
        #         'pool': False,
        #         'centered': False,
        #         'mean': False,
        #         'parameter_name' : 'contrast', 
        #         'neurons': list(analog_Xoff_ids[0:1]), 
        #         'sheet_name' : 'X_OFF'
        #    }), 
        #    fig_param={'dpi' : 100,'figsize': (8,8)}, 
        #    plot_file_name="ContrastSensitivity_LGN_Off.png"
        # ).plot({
        #    '*.y_lim':(0,100), 
        #    # '*.x_scale':'log', '*.x_scale_base':10,
        #    '*.fontsize':17
        # })

        # -----------------
        # SPATIAL FREQUENCY TUNING
        # firing rate against spatial frequencies
        # RetinalInputMovie( data_store, ParameterSet({}), plot_file_name="SpatialFrequencyTuning_LGN",frame_duration=100).plot({'*.fontsize':7})
        # dsv = param_filter_query( data_store, st_name='FullfieldDriftingSinusoidalGrating', analysis_algorithm=['TrialAveragedFiringRate'] )
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #        'polar': False,
        #        'pool': False,
        #        'centered': False,
        #        'mean': False,
        #        'parameter_name' : 'spatial_frequency', 
        #        'neurons': list(analog_Xon_ids[0:1]), 
        #        'sheet_name' : 'X_ON'
        #    }), 
        #    fig_param={'dpi' : 100,'figsize': (8,8)}, 
        #    plot_file_name="SpatialFrequencyTuning_LGN_On.png"
        # ).plot({
        #    '*.y_lim':(0,100), 
        #    '*.x_scale':'log', '*.x_scale_base':2,
        #    '*.fontsize':17
        # })
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #        'polar': False,
        #        'pool': False,
        #        'centered': False,
        #        'mean': False,
        #        'parameter_name' : 'spatial_frequency', 
        #        'neurons': list(analog_Xoff_ids[0:1]), 
        #        'sheet_name' : 'X_OFF'
        #    }), 
        #    fig_param={'dpi' : 100,'figsize': (8,8)}, 
        #    plot_file_name="SpatialFrequencyTuning_LGN_Off.png"
        # ).plot({
        #    '*.y_lim':(0,100), 
        #    '*.x_scale':'log', '*.x_scale_base':2,
        #    '*.fontsize':17
        # })

        #-----------------
        # TEMPORAL FREQUENCY TUNING                
        # RetinalInputMovie( data_store, ParameterSet({}), plot_file_name="TemporalFrequencyTuning_LGN",frame_duration=100).plot({'*.fontsize':7})
        # dsv = param_filter_query( data_store, st_name='FullfieldDriftingSinusoidalGrating', analysis_algorithm=['TrialAveragedFiringRate'] )
        # dsv = param_filter_query( data_store, st_name='FullfieldDriftingSquareGrating', analysis_algorithm=['TrialAveragedFiringRate'] )
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #        'polar': False,
        #        'pool': False,
        #        'centered': False,
        #        'mean': False,
        #        'parameter_name' : 'temporal_frequency', 
        #        'neurons': list(analog_Xon_ids[0:1]), 
        #        'sheet_name' : 'X_ON'
        #   }), 
        #   fig_param={'dpi' : 100,'figsize': (8,8)}, 
        #   plot_file_name="TemporalFrequencyTuning_LGN_On.png"
        # ).plot({
        #     '*.y_lim':(0,100), 
        #     '*.x_scale':'log', '*.x_scale_base':2,
        #     '*.fontsize':17
        # })
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #        'polar': False,
        #        'pool': False,
        #        'centered': False,
        #        'mean': False,
        #        'parameter_name' : 'temporal_frequency', 
        #        'neurons': list(analog_Xoff_ids[0:1]), 
        #        'sheet_name' : 'X_OFF'
        #   }), 
        #   fig_param={'dpi' : 100,'figsize': (8,8)}, 
        #   plot_file_name="TemporalFrequencyTuning_LGN_Off.png"
        # ).plot({
        #     '*.y_lim':(0,100), 
        #     '*.x_scale':'log', '*.x_scale_base':2,
        #     '*.fontsize':17
        # })

        #------------
        # SIZE TUNING
        # firing rate against sizes
        # RetinalInputMovie( data_store, ParameterSet({}), plot_file_name="SizeTuning_LGN",frame_duration=100).plot({'*.fontsize':7})
        dsv = param_filter_query( data_store, st_name='DriftingSinusoidalGratingDisk', analysis_algorithm=['TrialAveragedFiringRate'] )
        PlotTuningCurve(
            dsv,
            ParameterSet({
                'polar': False,
                'pool': False,
                'centered': False,
                'mean': False,
                'parameter_name' : 'radius', 
                'neurons': list(analog_Xon_ids[0:1]), 
                'sheet_name' : 'X_ON'
            }), 
            fig_param={'dpi' : 100,'figsize': (8,8)}, 
            plot_file_name="SizeTuning_Grating_LGN_On.png"
        ).plot({
            '*.y_lim':(0,100), 
            '*.x_scale':'log', '*.x_scale_base':2,
            '*.fontsize':17
        })
        PlotTuningCurve(
            dsv,
            ParameterSet({
                'polar': False,
                'pool': False,
                'centered': False,
                'mean': False,
                'parameter_name' : 'radius', 
                'neurons': list(analog_Xoff_ids[0:1]), 
                'sheet_name' : 'X_OFF'
            }), 
            fig_param={'dpi' : 100,'figsize': (8,8)}, 
            plot_file_name="SizeTuning_Grating_LGN_Off.png"
        ).plot({
            '*.y_lim':(0,100), 
            '*.x_scale':'log', '*.x_scale_base':2,
            '*.fontsize':17
        })
        dsv = param_filter_query( data_store, st_name='FlatDisk', analysis_algorithm=['TrialAveragedFiringRate'] )
        PlotTuningCurve(
           dsv,
           ParameterSet({
                'polar': False,
                'pool': False,
                'centered': False,
                'mean': False,
                'parameter_name' : 'radius', 
                'neurons': list(analog_Xon_ids[0:1]), 
                'sheet_name' : 'X_ON'
           }), 
            fig_param={'dpi' : 100,'figsize': (8,8)}, 
           plot_file_name="SizeTuning_Disk_LGN_On.png"
        ).plot({
           #'*.y_lim':(0,100), 
           '*.x_scale':'log', '*.x_scale_base':2,
           '*.fontsize':17
        })
        PlotTuningCurve(
           dsv,
           ParameterSet({
                'polar': False,
                'pool': False,
                'centered': False,
                'mean': False,
                'parameter_name' : 'radius', 
                'neurons': list(analog_Xoff_ids[0:1]), 
                'sheet_name' : 'X_OFF'
           }), 
            fig_param={'dpi' : 100,'figsize': (8,8)}, 
           plot_file_name="SizeTuning_Disk_LGN_Off.png"
        ).plot({
           '*.y_lim':(0,100), 
           '*.x_scale':'log', '*.x_scale_base':2,
           '*.fontsize':17
        })
                
        #--------------------
        # LIFELONG SPARSENESS
        # # per neuron FanoFactor level
        # dsv = param_filter_query(data_store, analysis_algorithm=['Analog_MeanSTDAndFanoFactor'], sheet_name=['X_ON'], value_name='FanoFactor(VM)')   
        # PerNeuronValuePlot(
        #    dsv,
        #    ParameterSet({'cortical_view':True}),
        #    fig_param={'dpi' : 100,'figsize': (6,6)}, 
        #    plot_file_name="FanoFactor_LGN_On.png"
        # ).plot({
        #    '*.x_axis' : None, 
        #    '*.fontsize':17
        # })
        # # # per neuron Activity Ratio
        # dsv = param_filter_query(data_store, analysis_algorithm=['TrialAveragedSparseness'], sheet_name=['X_ON'], value_name='Sparseness')   
        # PerNeuronValuePlot(
        #     dsv,
        #     ParameterSet({'cortical_view':True}),
        #     fig_param={'dpi' : 100,'figsize': (6,6)}, 
        #     plot_file_name="Sparseness_LGN_On.png"
        # ).plot({
        #     '*.x_axis' : None, 
        #     '*.fontsize':17
        # })

        #-------------------
        # ORIENTATION TUNING
        # firing rate against stimulus orientations
        # RetinalInputMovie( data_store, ParameterSet({}), plot_file_name="OrientationTuning_LGN",frame_duration=100).plot({'*.fontsize':7})
        # dsv = param_filter_query( data_store, st_name='FullfieldDriftingSinusoidalGrating', analysis_algorithm=['TrialAveragedFiringRate'] )
        # PlotTuningCurve( 
        #   dsv, 
        #   ParameterSet({
        #         'polar': False,
        #         'pool': False,
        #        'centered': False,
        #        'mean': False,
        #       'parameter_name':'orientation', 
        #       'neurons':list(analog_Xon_ids), 
        #       'sheet_name':'X_ON'
        #   }), 
        #   fig_param={'dpi' : 100,'figsize': (6,6)}, 
        #   plot_file_name="OrientationTuning_LGN_On.png"
        # ).plot({
        #   '*.y_lim' : (0,100),
        #    '*.fontsize':17
        # })
        # PlotTuningCurve( 
        #   dsv, 
        #   ParameterSet({
        #         'polar': False,
        #         'pool': False,
        #        'centered': False,
        #        'mean': False,
        #       'parameter_name':'orientation', 
        #       'neurons':list(analog_Xoff_ids), 
        #       'sheet_name':'X_OFF'
        #   }), 
        #   fig_param={'dpi' : 100,'figsize': (6,6)}, 
        #   plot_file_name="OrientationTuning_LGN_Off.png"
        # ).plot({
        #   '*.y_lim' : (0,100),
        #    '*.fontsize':17
        # })
        
        #-----------
        ## CONTOUR COMPLETION
        ## firing rate against square frequencies
        # RetinalInputMovie( data_store, ParameterSet({}), plot_file_name="Squares_LGN",frame_duration=100).plot({'*.fontsize':7})
        # ## Square Grating
        # dsv = param_filter_query( data_store, st_name='FullfieldDriftingSquareGrating', analysis_algorithm=['TrialAveragedCorrectedCrossCorrelation'] )
        # PerNeuronPairAnalogSignalListPlot(
        #     dsv,
        #     ParameterSet({
        #         'sheet_name' : 'X_ON', 
        #     }),
        #     fig_param={'dpi' : 100,'figsize': (14,14)}, 
        #     plot_file_name='SquareGrating_XCorr_LGN_On.png'
        # ).plot({
        #     '*.y_lim':(-30,30), 
        #     '*.fontsize':17
        # })
        # ## Flashing squares
        # dsv = param_filter_query( data_store, st_name='FlashingSquares', analysis_algorithm=['TrialAveragedCorrectedCrossCorrelation'] )
        # PerNeuronPairAnalogSignalListPlot(
        #     dsv,
        #     ParameterSet({
        #         'sheet_name' : 'X_ON', 
        #     }),
        #     fig_param={'dpi' : 100,'figsize': (14,14)}, 
        #     plot_file_name='FlashingSquare_XCorr_LGN_On.png'
        # ).plot({
        #     '*.y_lim':(-30,30), 
        #     '*.fontsize':17
        # })



        # ---- OVERVIEW LGN0 ----

        OverviewPlot(
           data_store,
           ParameterSet({
               # 'centered': False,
               # 'mean': False,
               'spontaneous': False,
               'sheet_name' : 'X_OFF', 
               'neuron' : analog_Xoff_ids[0], 
               'sheet_activity' : {}
           }),
           fig_param={'dpi' : 100,'figsize': (14,12)},
           plot_file_name="LGN_Off.png"
        ).plot({
            'Vm_plot.*.y_lim' : (-100,-40),
            '*.fontsize':7
        })

        OverviewPlot(
           data_store,
           ParameterSet({
               # 'centered': False,
               # 'mean': False,
               'spontaneous': False,
               'sheet_name' : 'X_ON', 
               'neuron' : analog_Xon_ids[0], 
               'sheet_activity' : {}
           }),
           fig_param={'dpi' : 100,'figsize': (14,12)},
           plot_file_name="LGN_On.png"
        ).plot({
            'Vm_plot.*.y_lim' : (-100,-40),
            '*.fontsize':7
        })

        OverviewPlot(
           data_store,
           ParameterSet({
               # 'centered': False,
               # 'mean': False,
               'spontaneous': False,
               'sheet_name' : 'PGN', 
               'neuron' : analog_PGN_ids[0], 
               'sheet_activity' : {}
           }),
           fig_param={'dpi' : 100,'figsize': (14,12)},
           plot_file_name="PGN.png"
        ).plot({
            'Vm_plot.*.y_lim' : (-100,-40),
            '*.fontsize':7
        })

        # SHOW PLOTS
        #import pylab
        #pylab.show()

# TODO: add a script to visualize all the phenomena together
