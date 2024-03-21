import pandas as pd
from asammdf import MDF

def convert_mdf_to_csv(mdf_file_path):
    print("Loading MDF file...")
    mdf = MDF(mdf_file_path)

    # Log the groups and channels in the MDF file
    for i, group in enumerate(mdf.groups):
        print(f"Group {i} contains the following channels:")
        for channel in group.channels:
            print(f" - {channel.name}")

    try:
        print("Converting MDF to DataFrame...")
        df = mdf.to_dataframe(time_from_zero=True)

        # Handling the time index
        if df.index.name is None or df.index.name == 'index':
            print("Resetting index to create a 'time' column...")
            df.reset_index(inplace=True)
            df.rename(columns={'index': 'time'}, inplace=True)
        elif df.index.name == 'time':
            df.reset_index(inplace=True)
        
        # Log the DataFrame columns after conversion
        print("DataFrame columns after conversion:", df.columns.tolist())

        # Ensure we include only the channels from the last group plus the 'time' column
        last_group_channels = [ch.name for ch in mdf.groups[-1].channels]
        if 'time' not in df.columns:
            print("'time' column is missing after conversion.")
            return pd.DataFrame()
        
        selected_columns = ['time'] + last_group_channels
        df = df[selected_columns]

        print("Final DataFrame columns:", df.columns.tolist())
        return df
    except Exception as e:
        print(f"Error during MDF to DataFrame conversion: {e}")
        return pd.DataFrame()


def clean_and_transform_data(df):
    # Renaming columns based on your SQL script
    column_renames = {
        'time': 'recording_time',
        'map_sp': 'manifold_pressure_setpoint',
        'map_mes': 'measured_manifold_pressure',
        'tia': 'throttle_inlet_pressure_or_temperature',
        'iga_av_mv': 'avg_ignition_advance_multivalve',
        'N': 'engine_rpm',
        'vs': 'vehicle_speed',
        'LAMB_LS_UP[1]': 'oxygen_sensor_upstream_bank1',
        'gear': 'current_gear',
        'iga_ad_1_knk[0]': 'ignition_advance_knock_sensor_0',
        'iga_ad_1_knk[1]': 'ignition_advance_knock_sensor_1',
        'iga_ad_1_knk[2]': 'ignition_advance_knock_sensor_2',
        'iga_ad_1_knk[3]': 'ignition_advance_knock_sensor_3',
        'iga_ad_1_knk[4]': 'ignition_advance_knock_sensor_4',
        'iga_ad_1_knk[5]': 'ignition_advance_knock_sensor_5',
        'rfp_sp': 'ref_fuel_pressure_setpoint',
        'LAMB_LS_UP[2]': 'oxygen_sensor_upstream_bank2',
        'fup': 'fuel_pressure_upstream',
        'fup_sp': 'fuel_pressure_setpoint',
        'pump_vol_vcv': 'pump_volume_valve_control',
        'fup_efp': 'fuel_pressure_electronic_fuel_pump',
        'efppwm': 'fuel_pump_pulse_width_modulation',
        'Short Term Fuel Trim - Bank 1': 'short_term_fuel_trim_bank1',
        'Short Term Fuel Trim - Bank 2': 'short_term_fuel_trim_bank2',
        'Long Term Fuel Trim - Bank 1': 'long_term_fuel_trim_bank1',
        'Long Term Fuel Trim - Bank 2': 'long_term_fuel_trim_bank2',
        'pv_av': 'purge_valve_average',
        'tqi_av': 'torque_request_average',
        'maf': 'mass_air_flow',
        'Ambient air temperature': 'ambient_air_temp',
        'amp_mes': 'amperage_measurement',
        'pdt_mes': 'pedal_position_measurement',
        'map_1_mes': 'manifold_pressure_1_measurement',
        'map_2_mes': 'manifold_pressure_2_measurement',
        'Commanded Throttle Actuator Control': 'commanded_throttle_position',
        'CAM_SP_IVVT_IN': 'camshaft_position_intake_valve_timing_setpoint',
        'lamb_sp[1]': 'lambda_setpoint_sensor1',
        'LAMB_SP[2]': 'lambda_setpoint_sensor2',
        'TI_1_HOM[0]': 'homogeneous_charge_injection_timing_0',
        'TI_1_HOM[3]': 'homogeneous_charge_injection_timing_3',
        'state_eng': 'engine_state',
    }
    df.rename(columns=column_renames, inplace=True)
    
    print(df.columns)

    # Convert vehicle speed from km/h to mph
    df['vehicle_speed'] = df['vehicle_speed'].apply(lambda x: x * 0.621371)

    # Example of data type conversion for numerical columns
    # df['engine_rpm'] = pd.to_numeric(df['engine_rpm'], errors='coerce')

    # Add any other data transformation or cleaning operations here

    return df

def generate_output_files(df_cleaned):
    if df_cleaned.empty:
        print("Cleaned DataFrame is empty, skipping file generation.")
        return
        
    # Generating a CSV file with one record per second
    df_one_per_second = df_cleaned.set_index('recording_time').resample('S').nearest().reset_index()
    df_one_per_second.to_csv('one_per_second.csv', index=False)

    # Generating a full dataset CSV file
    df_cleaned.to_csv('full_dataset.csv', index=False)

# Replace 'your_mdf_file.mf4' with the path to your MDF file
mdf_file_path = 'input.mdf'
df = convert_mdf_to_csv(mdf_file_path)

if not df.empty:
    print(df.head())
    df_cleaned = clean_and_transform_data(df)
    generate_output_files(df_cleaned)
