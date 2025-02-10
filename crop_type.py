import pandas as pd
import numpy as np 
import geopandas as gpd 
import shapely as shp 
import os
import operator
from shapely import wkt
import operator
import ast
from shapely.validation import make_valid




def most_value_frequent(List):
    return List.count(max(set(List), key = List.count))


def most_frequent2(col1, col2):
    """

    Args:
        col1 (_type_): [Beet, Poppy, Beet,   Beet, Beet, Beet]
        col2 (_type_): |[0.41, 0.12, 0.41, 0.41, 0.41, 0.41 ]
             my_dict = {
                 Beet: 2.05
                 Poppy: 0.12
             }

    Returns:
        _type_: Beet
    """
    
    my_dict = {}
    for s, t in zip(col1, col2):
            #print(s)
            my_dict[s] = my_dict.get(s, 0) + t
    return max(my_dict.items() , key=operator.itemgetter(1))[0]




def main(field_path,crop_path):
    field_data = gpd.read_file(field_path)
    crop_data = gpd.read_file(crop_path)
    crop_data = crop_data[['cromeid', 'prob', 'county',  'lucode', 'geometry']] # selecting only required columns from the crop data where 'cromeid' is unique ID, 'prob' is probability for the classified crop, 'county' county of the field, 'lucode' type of crop
    # calculating intersection between crome shapes and field
    a = gpd.sjoin(field_data,crop_data, predicate='intersects') 
    a = a.reset_index(drop=True)
    # computing the percentage overlap between the crome map geometry and field geometry
    geo_idx = 0
    for idx, col_n in enumerate(a.columns):
        if col_n=='geometry':
            geo_idx = idx
    # Apply this to the geometries that might be invalid
    a['geometry'] = a['geometry'].apply(lambda geom: make_valid(geom) if not geom.is_valid else geom)
    crop_data['geometry'] = crop_data['geometry'].apply(lambda geom: make_valid(geom) if not geom.is_valid else geom)# making all geometries valid if by any chance some geometry have issues
    a['per_over_lap'] = a.apply(lambda row: (row[geo_idx].intersection(crop_data.iloc[row[geo_idx+1]].geometry).area / row[geo_idx].area) * 100, axis=1)
    a = a.reset_index(drop=True)

    a['area_over_lap'] = (a["per_over_lap"]*0.41)/100  # here the area of each crome shape is 0.41hec so based on percentage we are calculating how much area of one shape falls in the field
    dict = {
    "AC01": "Spring Barley" ,"AC03" :"Beet","AC04" :"Borage","AC05" :"Buckwheat", "AC06" :"Canary Seed", "AC07" :"Carrot","AC09" :"Chicory","AC10" :"Daffodil","AC14" :"Hemp","AC15" :"Lettuce","AC16" :"Spring Linseed","AC17" :"Maize","AC18" :"Millet","AC19" :"Spring Oats","AC20" :"Onions","AC22" :"Parsley","AC23" :"Parsnips","AC24" :"Spring Rye","AC26" :"Spinach","AC27" :"Strawberry","AC30" :"Spring Triticale", "AC32" :"Spring Wheat","AC34" :"Spring Cabbage", "AC35" :"Turnip","AC36" :"Spring Oilseed","AC37" :"Brown Mustard",
    "AC38" :"Mustard","AC41" :"Radish","AC44" :"Potato","AC45" :"Tomato","AC50" :"Squash","AC52" :"Siam Pumpkin","AC58" :"Mixed Crop-Group","AC59" :"Mixed Crop-Group","AC60" :"Mixed Crop-Group","AC61" :"Mixed Crop-Group", "AC62" :"Mixed Crop-Group",  "AC63" :"Winter Barley","AC64" :"Winter Linseed", "AC65" :"Winter Oats","AC66" :"Winter Wheat","AC67" :"Winter Oilseed", "AC68" :"Winter Rye","AC69" :"Winter Triticale", "AC70" :"Winter Cabbage","AC71" :"Coriander","AC72" :"Corn gromwell", "AC74" :"Phacelia",
    "AC81" :"Poppy","AC88" :"Sunflower","AC90" :"Gladioli","AC92" :"Sorghum","AC94" :"Sweet William", "AC100": "Italian Ryegrass","CA02" :"Cover Crop","LG01" :"Chickpea","LG02" :"Fenugreek","LG03" :"Spring Field beans", "LG04" :"Green Beans","LG06" :"Lupins","LG07" :"Spring Peas","LG09" :"Cowpea","LG08" :"Soya","LG11" :"Lucerne","LG13" :"Sainfoin","LG14" :"Clover","LG15" :"Mixed Crops–Group 1 Leguminous", "LG16" :"Mixed Crops–Group 2 Leguminous","LG20" :"Winter Field beans","LG21" :"Winter Peas","SR01" :"Short Rotation Coppice","FA01" :"Fallow Land",
    "HE02" :"Heathland and Bracken","PG01" :"Grass","NA01" :"Non-vegetated or sparsely-vegetated Land", "WA01" :"Water","TC01" :"Perennial Crops and Isolated Trees","NU01" :"Nursery Crops","WO12" :"Trees and Scrubs, short Woody plants, hedgerows","AC00" :"Unknown or Mixed Vegetation",
    "NA01":"Non agriculture land"}

    field_with_multiple_crop = a.replace({"lucode": dict}) # replacing all the crome lucode with crop name
    
    """ Now one field can intersect with multiple crome polygon so we are going to group them based on fid which is unique for each field and make the list of rest of the attributes for field area we going to pick only one since it is repeated
     so the output will look like
    field  |        lucode         | Area(hec)   |            area_over_lap            |
    osgb001| [Beet, Poppy, Beet,   |  2.17 hec   |[0.41, 0.12, 0.41, 0.41, 0.41, 0.41 ]
              Beet, Beet, Beet]
    
    """
    field_with_crop = (field_with_multiple_crop.groupby('fid')
        .agg({            
                'lucode'	: lambda x: (x.tolist()),
                'Area(hec)': lambda x: x.tolist()[0],
                 
                'area_over_lap':lambda x: (x.tolist())
        }).reset_index())

    field_with_crop['max_lucode_occurance'] = field_with_crop['lucode'].apply(most_value_frequent) # getting the frequency of crop occurred
     
    field_with_crop['crop_maxA']=field_with_crop.apply(lambda x: most_frequent2(x['lucode'],x['Crom_area_lap']), axis=1) # if all crop are unique it is picking based on max area overlapping with field
    
    # saving files:
    
    field_with_crop.to_excel(field_path)
 




if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <file_path>")
    else:
        field_path = sys.argv[1]
        crop_path = sys.argv[2]
        
        main(field_path,crop_path)