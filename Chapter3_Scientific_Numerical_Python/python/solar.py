def solar(year, month, day, hour, lat_deg, lon_deg, minute=0, second=0):
    '''Return solar zenith and clear sky radiation
       for given lat, lon and time/date
    '''
    from datetime import datetime
    import Pysolar
    
    d = datetime(year, month, day, hour, minute, second) 
    altitude_deg = Pysolar.GetAltitude(lat_deg, lon_deg, d)
    # W m^-2
    solar_rad = Pysolar.solar.radiation.GetRadiationDirect(d, altitude_deg)
    return 90. - altitude_deg,solar_rad

