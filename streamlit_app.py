import pickle

with open('all results.pkl', 'rb') as all_results_file:
    new_data = pickle.load(all_results_file)

print(new_data)
