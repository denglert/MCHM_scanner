#!/usr/bin/env python

import sys
import mg5_utils as mg5
import utils as utils
import math
import shutil
import os


MCHM_scanner_dir = os.environ['MCHM_scanner_dir']

##################

# - 1. Run tag
# - 2. Component (triangle, box, ..)
# - 3. shat value
# - 4. f value

tag  = sys.argv[1]
comp = sys.argv[2]
shat = float(sys.argv[3])
f    = float(sys.argv[4])

##################

plot_topdraw = False

process_dir = '{}/mg5_processes/CHM_gg_Zh_{}'.format(MCHM_scanner_dir, comp)
####

# - Path to the input parameter cards
param_card_path = os.path.join( './mg5_cards', 'param_card.dat' )
run_card_path   = os.path.join( './mg5_cards', 'run_card.dat' )

# - MG5 prompt
madevent_prompt = {'tri': None, 'box': None, 'int' : None, 'all': None}
xsec            = {'tri': None, 'box': None, 'int' : None, 'all': None}



# - Path to the process parameter cards
process_param_card_path = os.path.join( process_dir, './Cards/param_card.dat')
process_run_card_path   = os.path.join( process_dir, './Cards/run_card.dat')
process_plot_card_path  = os.path.join( process_dir, './Cards/plot_card.dat' )

# - Copying cards over
shutil.copy2( param_card_path , process_param_card_path )
shutil.copy2( run_card_path,    process_run_card_path   )

if not plot_topdraw:
    utils.silentrm( process_plot_card_path)

madevent_prompt[comp] = mg5.get_ME5_cmd_line( process_dir )

# - Card writers
param_card = mg5.get_param_card( '/scratch/de3u14/CHM/cross_section_scan/mg5_processes/CHM_gg_Zh_tri', param_card_path )
run_card   = mg5.get_run_card( run_card_path )

################

v = 246.0 # GeV

#################

outfile_name = 'xsec_info_f_shat_{}.dat'.format(comp)
with open(outfile_name, 'a') as f_out:

    #header = 'shat f xi k_hzz k_hqq xsec_{}\n'.format(comp)
    #f_out.write(header)

    process_param_card_path = os.path.join( process_dir, './Cards/param_card.dat')
    process_run_card_path   = os.path.join( process_dir, './Cards/run_card.dat')

    # - Calc
    xi = (v**2)/(f**2)
    k_hzz = math.sqrt(1.0-xi)
    k_hqq = (1.0-2.0*xi)/math.sqrt(1.0-xi)
    gstar = 1.0
    
    #full_tag = '{}_{}'.format( tag, k )
    full_tag = '{}_{}_{}'.format( tag, shat, f )
    
    # - Param card settings
    param_card[ 'chm' ].param_dict[ (1,)   ].value = xi
    param_card[ 'chm' ].param_dict[ (2,)   ].value = gstar
    param_card.write( process_param_card_path )
    
    # - Run card settings
    run_card['ebeam1'] = shat/2.0
    run_card['ebeam2'] = shat/2.0
    
    run_card.write( process_run_card_path )
    
    madevent_prompt[comp].run_cmd( 'generate_events -f {}'.format(full_tag) )
    
    xsec[comp] = madevent_prompt[comp].results.current['cross']
    
    row = '{:.3e} {:.3e} {:.3e} {:.3e} {:.3e} {:.3e}\n'.format(shat, f, xi, k_hzz, k_hqq,
            xsec[comp])
    f_out.write( row )
    f_out.flush()

    shutil.rmtree(os.path.join( process_dir, 'HTML', full_tag), ignore_errors=True )
