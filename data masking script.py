from faker import Faker
import pandas as pd

# Initialize the faker
fake = Faker()
# India locale faker because default faker does not have bank() method.  See Faker documentation
fake_in = Faker('en_IN')

# User defined variables.
input_dir = './input_files/'  # input directory
output_dir = './output_files/'  # output directory
data_file = 'your_file.csv'  # input file name
masked_data_file = 'your_masked_file.csv'  # output masked file name

# Load the data from original file and store it in dataframe.
df = pd.read_csv(input_dir + data_file)

# Mask fields with sensitive information.
df['ssn'] = df['ssn'].apply(lambda x: fake.ssn())
df['bank'] = df['bank'].apply(lambda x: fake_in.bank())

# Save the masked data to a new file.
df.to_csv(output_dir + masked_data_file, index=False)
