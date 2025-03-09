# -*- coding: utf-8 -*-

import arcpy
import batch_clipper

class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Batch Clipper"
        self.alias = "BatchClipper"

        # List of tool classes associated with this toolbox
        self.tools = [BatchClipper]


class BatchClipper:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Batch Clipper"
        self.description = ""

    def getParameterInfo(self):
        """Define the tool parameters."""
        params = []
        in_ws = arcpy.Parameter(name="in_ws", 
                                displayName="Input Workspace", 
                                direction = "Input", 
                                datatype = "DEWorkspace", 
                                parameterType = "Required")
        clip_ws = arcpy.Parameter(name="clip_ws", 
                                  displayName="Clip Workspace", 
                                  direction = "Input", 
                                  datatype = "DEWorkspace", 
                                  parameterType = "Required")
        out_ws = arcpy.Parameter(name="out_ws", 
                                 displayName="Output Workspace", 
                                 direction = "Input", 
                                 datatype = "DEWorkspace", 
                                 parameterType = "Required")
        params.append(in_ws)
        params.append(clip_ws)
        params.append(out_ws)
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
        in_ws = parameters[0].valueAsText
        clip_ws = parameters[1].valueAsText
        out_ws = parameters[2].valueAsText
        batch_clipper.clipper(in_ws, clip_ws, out_ws)

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
