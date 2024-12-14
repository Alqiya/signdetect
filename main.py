#0....Setup path
WORKSPACE_PATH = 'Tensorflow/workspace'
SCRIPTS_PATH = 'Tensorflow/scripts'
APIMODEL_PATH = 'Tensorflow/models'
ANNOTATION_PATH = WORKSPACE_PATH+'/annotations'
IMAGE_PATH = WORKSPACE_PATH+'/images'
MODEL_PATH = WORKSPACE_PATH+'/models'
PRETRAINED_MODEL_PATH = WORKSPACE_PATH+'/pre-trained-models'
CONFIG_PATH = MODEL_PATH+'/my_ssd_mobnet/pipeline.config'
CHECKPOINT_PATH = MODEL_PATH+'/my_ssd_mobnet/'

#1..Create label map

labels = [ {'name':'Help', 'id':1}, 
    {'name':'ok', 'id':2},
    {'name':'You', 'id':3},
    {'name':'Mine', 'id':4},
    {'name':'Say', 'id':5},
    {'name':'Equal', 'id':6}
]

with open(ANNOTATION_PATH + '\label_map.pbtxt', 'w') as f:
    for label in labels:
        f.write('item { \n')
        f.write('\tname:\'{}\'\n'.format(label['name']))
        f.write('\tid:{}\n'.format(label['id']))
        f.write('}\n')

#2..Create TF Records

import subprocess

# Define paths
SCRIPTS_PATH = 'Tensorflow/scripts'  # Replace with your actual path
IMAGE_PATH = WORKSPACE_PATH+'/images'   # Replace with your actual path
ANNOTATION_PATH = WORKSPACE_PATH+'/annotations' # Replace with your actual path

# Define the commands
train_command = [
    "python", f"{SCRIPTS_PATH}/generate_tfrecord.py",
    "-x", f"{IMAGE_PATH}/train",
    "-l", f"{ANNOTATION_PATH}/label_map.pbtxt",
    "-o", f"{ANNOTATION_PATH}/train.record"
]

test_command = [
    "python", f"{SCRIPTS_PATH}/generate_tfrecord.py",
    "-x", f"{IMAGE_PATH}/test",
    "-l", f"{ANNOTATION_PATH}/label_map.pbtxt",
    "-o", f"{ANNOTATION_PATH}/test.record"
]

# Execute the commands
try:
    print("Running train command...")
    subprocess.run(train_command, check=True)
    print("Train command completed successfully.")

    print("Running test command...")
    subprocess.run(test_command, check=True)
    print("Test command completed successfully.")

except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")