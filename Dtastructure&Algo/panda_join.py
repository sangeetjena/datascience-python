import pandas as pd

flight_path = pd.DataFrame(([['f001','blr','bbsr','f001_01']
                                            ,['f001','bbsr','blr','f001_02']
                                            ,['f002','blr','kol','f002_01']
                                            ,['f002','kol','blr','f002_02']])
                                            ,columns=['flight_id','arrive_state','depart_state','tran_id'])

flight_details = pd.DataFrame(([['f001','Indigo','Ind'],['f002','air_asia','ind']]),columns=['flight_code','Company_Name','Contry_code'])
state_details = pd.DataFrame([['bbsr','Bhubaneswar'],['kol','Kolkata'],['blr','Bangalore']],columns=['state_code','State_name'])
flight_arrival_depart = pd.DataFrame(([['f001_01','30-11-2018 10:00:00','30-11-2018 13:00:00',]
                                                       ,['f001_02','30-11-2018 15:00:00','30-11-2018 18:00:00']
                                                        , [ 'f002_01', '30-11-2018 10:00:00', '30-11-2018 13:00:00' ]
                                                         , [ 'f002_02', '31-11-2018 10:00:00', '31-11-2018 13:00:00' ]])
                                                        ,columns=['flight_tran_id','arrive','depart'])
#flight with its name and arrival and departire

flight_hist_stg1 = flight_path.merge(flight_details, how='left',left_on='flight_id',right_on='flight_code')\
    .merge(state_details,how='left',left_on='arrive_state',right_on='state_code')\
    .merge(flight_arrival_depart,how='left',left_on='tran_id',right_on='flight_tran_id')[['flight_id','Company_Name','Contry_code','State_name','tran_id','arrive','depart']]

flight_hist_stg1.rename(columns={'State_name' : 'arriving_State_name'},inplace=True)