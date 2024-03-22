import os
import pandas as pd
from asammdf import MDF
import argparse

def convert_mdf_to_csv(mdf_file_path):
    print("Loading MDF file...")
    try:
        mdf = MDF(mdf_file_path)
    except Exception as e:
        print(f"Failed to load MDF file: {e}")
        return None  # Return None to indicate failure

    # Identify the last group number
    last_group_number = len(mdf.groups) - 1
    output_file_path = os.path.splitext(mdf_file_path)[0] + '_FullOutput.csv'
    print(f"Intending to do a full output at {output_file_path}")
    print(f"Identified the last group, this is the one that we want to use: Group {last_group_number}")

    # Export only the last group to CSV
    mdf.export(fmt='csv', filename=output_file_path, single_time_base=True, channels=None, time_from_zero=False, empty_channels='skip', keep_same_value=False, raster=None, comment=None, compression=0, ignore_value2text_conversions=False, time_as_date=False, oned_as='column', display_base='physical', reduce_memory_usage=False, format_version='5.30', filter=None, remove_source_from_channel_names=False, master_channel=None, group=last_group_number)
    
    print(f"Exported the last group (Group {last_group_number}) to {output_file_path}")
    return pd.read_csv(output_file_path)


def clean_and_transform_data(df):
    print("Starting data cleaning and transformation...")
    print("Columns before renaming:", df.columns)
    # Renaming columns based on your SQL script
    column_renames = {
        'time': 'timestamps',
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
    print("Columns after renaming:", df.columns.tolist())

    # Convert vehicle speed from km/h to mph
    if 'vehicle_speed' in df.columns:
        df['vehicle_speed'] = df['vehicle_speed'].apply(lambda x: x * 0.621371)
        print("Converted vehicle speed from km/h to mph.")

    return df

def generate_output_files(mdf_file_path, df_cleaned):
    if df_cleaned.empty:
        print("Cleaned DataFrame is empty, skipping file generation.")
        return
    
    print("Generating output files...")
    
    output_file_path = os.path.splitext(mdf_file_path)[0] + '_OnePerSecond.csv'

    # Convert 'timestamps' to a DatetimeIndex
    df_cleaned['timestamps'] = pd.to_datetime(df_cleaned['timestamps'], unit='s')
    print("Converted 'timestamps' to datetime format.")

    # Generating a CSV file with one record per second
    df_one_per_second = df_cleaned.set_index('timestamps').resample('1S').nearest().reset_index()
    df_one_per_second.to_csv(output_file_path, index=False)
    print("Generated one record per second CSV.")

    # Generating a full dataset CSV file
    #df_cleaned.to_csv('full_dataset.csv', index=False)
    print("Generated full dataset CSV.")

def main():
    parser = argparse.ArgumentParser(description='Convert MDF to CSV and perform data cleaning.')
    parser.add_argument('input_file', type=str, help='Input MDF file path')

    args = parser.parse_args()

    df = convert_mdf_to_csv(args.input_file)
    if df is not None and not df.empty:
        print(df.head())
        df_cleaned = clean_and_transform_data(df)
        generate_output_files(args.input_file, df_cleaned)
    else:
        print("Data frame is empty or not created.")

if __name__ == "__main__":
    main()
