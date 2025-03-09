import os
import sys
import arcpy


def lister_fc(root_folder, shp_type, out_filename):

    out_filename = out_filename +'.txt'
 
    msg = f'Writing {shp_type} feature class names '
    msg += f'under {root_folder} to {out_filename} ...'
    arcpy.AddMessage(msg)
    with open(out_filename, 'w') as outfile:
        walk = arcpy.da.Walk(root_folder, datatype="FeatureClass", type=shp_type)
        for ws, _, fc_list in walk:
            for fc in fc_list:
                arcpy.AddMessage(os.path.join(os.path.abspath(ws), fc))
                outfile.write(os.path.join(os.path.abspath(ws), fc) + '\n')
    arcpy.AddMessage('Done')