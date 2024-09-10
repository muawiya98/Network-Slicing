import random
import os

root_path = os.getcwd()
codes_path = os.path.join(root_path, 'src')
results_path = os.path.join(root_path, 'Results')

# ========================================================
number_of_steps = 15
services_types = ['Safety', 'Entertainment', 'AutonomousDrivin']
communication_units_types = ['Satellites', 'Wi-Fi', '3G', '4G', '5G']
number_of_request = random.randint(20, 100)
number_of_units = 20 # random.randint(5, 20)
units_for_service = (1, 5)
requests_for_units = (5, 10)

