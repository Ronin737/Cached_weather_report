'''Utility functions for modifying the data'''

def istemp(info):
    if '/' not in info:
        return False
    if info[info.index('/')+1]=='M':
        return True
    vals=info.split('/')
    vals=[val.isdigit() for val in vals]
    if all(vals):
        return True
    return False


def serialize(data):
    '''Function to serialise the data into a suitable dictionary'''
    data=data.split()
    data_dict=dict(station=f'{data[2]}',
                   last_observation=f'{data[0]} at {data[1]} G.M.T')
    data=data[3:]
    wind_info=''
    temp_info=''
    for info in data:
        if 'KT' in info:
            wind_info=info
        if istemp(info):
            temp_info=info
    if(wind_info==''):
        data_dict['wind']='No data available'
    else:
        gust_info=''
        if('G' in wind_info):
            gust=wind_info[wind_info.index('G')+1:-2]
            gust_info=f' with {int(gust)}-knot gusts'
            wind_info=wind_info[:wind_info.index('G')]+'KT'
        
        direction=int(wind_info[0:3])
        speed=int(wind_info[3:-2])
        data_dict['wind']=f'The wind is blowing from {direction} degrees(true) at a sustained speed of {speed} knots'+gust_info
    
    if(temp_info==''):
        data_dict['temperature_&_dewpoint']='No data available'
    else:
        temp_info=temp_info.split('/')
        temp_info=[int(info[1:])*(-1) if info[0]=='M' else int(info) for info in temp_info]
        data_dict['temperature_&_dewpoint']=f'{temp_info[0]} C with {temp_info[1]} C dewpoint'
    return data_dict
