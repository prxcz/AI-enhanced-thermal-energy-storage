# VERSION 3 (final full solution)
import json

energy_sources_v3 = [
  "solar_pv", # daytime charge
  "wind", # good at night
  "battery", # short backup
  "grid", # buy cheap times
  "biomass", # backup
  "waste_heat", # reuse heat
  "gas_boiler" # last backup
]

storage_types = ["water_tank", "molten_salt", "rocks", "pcm"]

sensors_v3 = ["temp", "flow", "power", "weather", "price_feed", "demand"]

ai_tasks_v3 = {
  "demand_forecast": "guess heat need next 24h",
  "solar_forecast": "predict sun hours",
  "wind_forecast": "predict wind power",
  "maintenance": "spot problems early",
  "control": "when to charge/discharge"
}

steps_v3 = [
  "collect_data()",
  "train_forecasts()",
  "run_mpc() # model predictive control",
  "optimise_charging()",
  "check_faults()"
]

# saving data
save_file = "tes_data.json"

def save_data(data):
with open(save_file, "w") as f:
  json.dump(data, f)
print("data saved!")

example_data = {"temp": 75, "demand": 300, "source": "solar_pv"}
save_data(example_data)

quick_wins = [
  "charge at midday solar",
  "shift work when power cheap",
  "use waste heat first",
  "only use gas in emergency"
]

print("v3: full AI-TES plan ready :)")
