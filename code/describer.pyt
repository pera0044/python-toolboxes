# -*- coding: utf-8 -*-

import arcpy
import fc_describer

class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Feature Class Describer"
        self.alias = "FCDescriber"

        # List of tool classes associated with this toolbox
        self.tools = [FCDescriber]


class FCDescriber:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Feature Class Describer"
        self.description = "Describes the fields including name, type and length"

    def getParameterInfo(self):
        """Define the tool parameters."""
        params = []
        message = arcpy.Parameter(name="fc", 
                                  displayName="Feature Class", 
                                  direction = "Input", 
                                  datatype = "DEFeatureClass", 
                                  parameterType = "Required")
        params.append(message)
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
        in_fc = parameters[0].valueAsText
        fc_describer.describe_fc(in_fc)
        

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
