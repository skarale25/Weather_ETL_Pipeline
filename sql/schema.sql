Create table if not exists weather_data(
    id serial primary key,
    city varchar(100),
    country varchar(100),
    latitude float,
    longitude float,
    weather_condition varchar(100),
    weather_description varchar(255),
    temperature_celsius float,
    feels_like_temp_celsius float,
    humidity_percent int,
    pressure_hpa int,
    wind_speed_mps float,
    time_stamp timestamp
    created_at timestamp default current_timestamp
);