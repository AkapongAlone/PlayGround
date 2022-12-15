from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Model, Pattern,Work,Tool
# # Register your models here.
class Designadmin(admin.ModelAdmin):
    ordering = ['wid']
    list_display=['wid','partname',"model" 
      ,'tooltype'
      ,'excel'
      ,'img'
      ,'point'
      ,'toolname'
      ,'shift'
      ,'machine_line'
      ,'machine_no'
      ,'machine_process'
      ,'processname'
      ,'point_no'
      ,'sheet'
      ,'min'
      ,'max'
      ]
    list_editable=["model"
      ,'tooltype'
      
      ,'excel'
      ,'img' 
      ,'point'
      ,'toolname'
      
      ,'machine_line'
      ,'machine_no'
      ,'machine_process'
      ,'processname'
      
     
      
      ,'sheet'
      ,'min'
      ,'max'
      ]
    list_filter=['partname',"model",'toolname','tooltype' ]
    
    
admin.site.register(Model,Designadmin)
class Designtool(admin.ModelAdmin):
    
    list_display=['tid','toolname',"tooltype"  ]
    list_editable=['toolname',"tooltype"]
    list_filter=["tooltype" ]
admin.site.register(Tool,Designtool) 

class Designpattern(admin.ModelAdmin):
    
    list_display=['pattern_id','direction',"cstart",'rstart','name','name_shift','num_shift','shift_type','timestart','timeend'  ]
    list_editable=['direction',"cstart",'rstart','name','name_shift','num_shift','shift_type','timestart','timeend']
    # list_filter=["tooltype" ]
admin.site.register(Pattern,Designpattern)  