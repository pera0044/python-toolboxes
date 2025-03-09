# -*- coding: utf-8 -*-

import arcpy
import fc_lister

class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Feature Class Lister"
        self.alias = "FCLister"

        # List of tool classes associated with this toolbox
        self.tools = [FCLister]


class FCLister:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Feature Class Lister"
        self.description = ""

    def getParameterInfo(self):
        """Define the tool parameters."""
        params = []
        root_folder = arcpy.Parameter(name="root_folder", 
                                      displayName="Root Folder", 
                                      direction = "Input", 
                                      datatype = "DEFolder", 
                                      parameterType = "Required")
        shp_type = arcpy.Parameter(name="shp_type", 
                                   displayName="Shape Type", 
                                   direction = "Input", 
                                   datatype = "GPString", 
                                   parameterType = "Required")
        shp_type.filter.type = "ValueList"
        shp_type.filter.list = ["Point", "Polyline", "Polygon"]
        out_filename = arcpy.Parameter(name="out_filename", 
                                       displayName="Output File Name", 
                                       direction = "Input", 
                                       datatype = "GPString", 
                                       parameterType = "Required")
        params.append(root_folder)
        params.append(shp_type)
        params.append(out_filename)
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        root_folder = parameters[0].valueAsText
        shp_type = parameters[1].valueAsText
        out_filename = parameters[2].valueAsText
        fc_lister.lister_fc(root_folder, shp_type, out_filename)

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
