#!/usr/bin/env python


import mg5_utils as mg5


# - Create MG5 process code for Composite Higgs Model gg -> Zh
# - Usage: create_MG5_process_dir(model, process, dir)
mg5.create_MG5_process_dir('loop_chm', 'g g > z h [noborn=QCD]',          './mg5_processes/CHM_gg_Zh_all/'  )
mg5.create_MG5_process_dir('loop_chm', 'g g > z h [noborn=QCD] HZZ^2==0', './mg5_processes/CHM_gg_Zh_box/'  )
mg5.create_MG5_process_dir('loop_chm', 'g g > z h [noborn=QCD] HZZ^2==1', './mg5_processes/CHM_gg_Zh_int/'  )
mg5.create_MG5_process_dir('loop_chm', 'g g > z h [noborn=QCD] HZZ^2==2', './mg5_processes/CHM_gg_Zh_tri/'  )
 

# - Testing
# - SM: gg -> Zh
# mg5.create_MG5_process_dir('loop_sm', 'g g > z h [noborn=QCD]','./mg5_processes/SM_gg_Zh_SM/'  ) 
