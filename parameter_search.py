# Parameter search for Naka-Rushton Gain control
#
# the function LocalSequentialBackend takes a model with parameters 
# and executes the simulation replacing the parameters listed in the CombinationParameterSearch
#
# usage:
# python parameter_search.py run.py nest param/defaults

from mozaik.meta_workflow.parameter_search import CombinationParameterSearch
from mozaik.meta_workflow.parameter_search import LocalSequentialBackend
import numpy

CombinationParameterSearch(
	LocalSequentialBackend( num_threads=1 ),
	{
		# 'retina_lgn.params.gain_control.gain' : [60],
  		# 'retina_lgn.params.gain_control.non_linear_gain.luminance_gain' : [80.0],#[30.0, 50.0, 80.0, 100.0],
  		# 'retina_lgn.params.gain_control.non_linear_gain.luminance_scaler' : [0.08], #[0.01, 0.05, 0.08, 0.15],
  		# 'retina_lgn.params.gain_control.non_linear_gain.contrast_scaler' : [0.01], #[0.001, 0.01, 0.05, 0.08, 0.15]

  		# 'pgn.LGN_PGN_ConnectionOn.base_weight' : [0.023,0.23],
  		# 'pgn.LGN_PGN_ConnectionOff.base_weight' : [0.023,0.23],
  		# 'pgn.PGN_LGN_ConnectionOn.base_weight' : [0.36,3.6],
  		# 'pgn.PGN_LGN_ConnectionOff.base_weight' : [0.36,3.6],

      # n1 + (K1 * exp(-c1*t))
      #'retina_lgn.params.receptive_field.func_params.K1' : [0.0],#0.8
      'retina_lgn.params.receptive_field.func_params.c1' : [0.01, 0.05, 0.1, 0.5],#
      #'retina_lgn.params.receptive_field.func_params.n1' : [0.01, 0.1],#

    }
).run_parameter_search()

# T05_ParameterSearch_____num_samples:15_num_samples:10_num_samples:10_num_samples:10
# T05_ParameterSearch_____num_samples:15_num_samples:10_num_samples:15_num_samples:10

# T05_ParameterSearch_____base_weight:0.23_base_weight:0.23_base_weight:0.36_base_weight:0.36


# gain		luminance_gain		luminance_scaler		contrast_scaler
# 10 		30.0 	 			0.001										On: 0-140
# 10 		50.0 	 			0.01										On: 0-80
# 30 		50.0 	 			0.01										On: 0-80  
# 60 		50.0 	 			0.01										On: 0-80
# 60 		80.0 	 			0.08										On: 0-80  <<<<<<< we use this
# 60 		80.0 	 			0.08					0.01				On: 0-80  <<<<<<< we use this


# 1 Step: retinal drive
#         Without the complete temporal envelope and without the inhibitory influence of PGN
#         The response of LGN cell should be like the one coming from retina
#
#         1.1 Spontaneous
#         SakmannCreutzfeldt1969: fig2 20 sp/s
#         FreemanGranaPassaglia2010: fig1 20 sp/s
#
#         1.2 Luminance
#         SakmannCreutzfeldt1969: fig2 min ~20 sp/s,  max 60-100 sp/s
#
#         1.3 Contrast
#         SakmannCreutzfeldt1969: fig6 no saturation in contrast (up to refractory period interval)
#         SakmannCreutzfeldt1969: fig8 300 sp/s phasic response
#         FreemanGranaPassaglia2010


# 2 step: introduce PGN
#         match the spatio temporal filter
#
#         CaiDeangelisFreeman1997
