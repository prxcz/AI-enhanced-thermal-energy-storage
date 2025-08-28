# VERSION 2 
energy_sources_v2 = [
  "solar_pv", "wind", "battery", "grid", "biomass"
]

sensors_v2 = ["temp", "flow", "power", "weather", "price_feed"]

ai_tasks_v2 = {
  "demand_forecast": "guess heat need next 24h",
  "solar_forecast": "predict sun",
  "maintenance": "spot problems",
  "control": "when to charge/discharge"
}

steps_v2 = ["collect_data()", "train_forecasts()", "optimise_charging()"]

print("v2: more tasks but still not complete")
