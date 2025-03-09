import arcpy

def describe_fc(in_fc):
    
    dsc = arcpy.da.Describe(in_fc)

    arcpy.AddMessage(f'{"Field Name":15}{"Field Type":15}{"Length"}')
    arcpy.AddMessage(f'{"----------":15}{"----------":15}{"------"}')

    fields = dsc['fields']
    for field in fields:
        arcpy.AddMessage(f'{field.name:15} {field.type:15} {field.length:>3}')
