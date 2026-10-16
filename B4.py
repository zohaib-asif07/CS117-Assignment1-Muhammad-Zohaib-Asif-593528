# B4.py | Continuous Discharge Analysis   [10 marks]

voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9,
            12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

#reference values / initialization
current_streak = 1
longest_streak = 1
start_voltage = 0
end_voltage = 0
streak_start_voltage = 0

for position in range(1, len(voltages)):
    if voltages[position] < voltages[position - 1]:
        current_streak = current_streak + 1
    else:
        current_streak = 1
        streak_start_voltage = voltages[position]

    if current_streak > longest_streak:
        longest_streak = current_streak
        start_voltage = streak_start_voltage
        end_voltage = voltages[position]

print("Longest continuous drop:", longest_streak, "minutes")
print("Started at:", start_voltage, "V")
print("Ended at:", end_voltage, "V")